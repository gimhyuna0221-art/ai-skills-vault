"""Strict quad OBJ I/O. Geometry/normal records are copied, never regenerated."""
from __future__ import annotations
import hashlib, json, os
from pathlib import Path
import numpy as np

class StopUV(RuntimeError):
    def __init__(self, code: str, message: str):
        super().__init__(message); self.code = code

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(4*1024*1024), b''): h.update(block)
    return h.hexdigest()

def json_write(path: Path, data) -> None:
    tmp=path.with_suffix(path.suffix+'.part')
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    os.replace(tmp,path)

def np_save(path: Path, array) -> None:
    tmp=path.with_suffix(path.suffix+'.part')
    with tmp.open('wb') as f: np.save(f,array,allow_pickle=False)
    os.replace(tmp,path)

def record(line: bytes):
    clean=line.strip()
    if not clean or clean.startswith(b'#') or clean.strip(b'\x00')==b'':return b'',[]
    parts=clean.split(b'#',1)[0].split()
    return parts[0],parts[1:]

def index(value: bytes, seen: int, total: int, kind: str) -> int:
    i=int(value); j=i-1 if i>0 else seen+i
    if i==0 or not 0<=j<total:
        raise StopUV('INVALID_INDEX',f'Invalid {kind} index {i}.')
    return j

def read_obj(path: Path, *, max_faces: int=3_000_000, with_uv: bool=False):
    counts={b'v':0,b'vt':0,b'vn':0,b'f':0}; warnings=[]
    # Do not trust an exported count comment. Count actual records.
    with path.open('rb') as f:
        for line_no,line in enumerate(f,1):
            # Fast path for large vertex tables.
            tag=line.lstrip().split(None,1)[0] if line.strip() else b''
            if tag in counts: counts[tag]+=1
            if tag==b'f':
                _,p=record(line)
                if len(p)!=4: raise StopUV('QUADS_REQUIRED',f'Line {line_no}: found {len(p)}-gon. This version accepts quad-only open strips; no automatic triangulation/remeshing.')
            if tag in {b'l',b'p',b'curv',b'curv2',b'surf',b'vp',b'csh',b'call'}:
                raise StopUV('UNSUPPORTED_OBJ_RECORD',f'Line {line_no}: unsupported OBJ record {tag!r}.')
    N,F,T,M=[counts[k] for k in [b'v',b'f',b'vt',b'vn']]
    if not N or not F: raise StopUV('EMPTY_MESH','No polygon mesh found.')
    if F>max_faces: raise StopUV('RESOURCE_LIMIT',f'{F} faces exceeds --max-faces={max_faces}. Source remains untouched.')
    if N>=2**31:raise StopUV('RESOURCE_LIMIT','Vertex indices exceed int32 range.')
    v=np.empty((N,3),np.float64);q=np.empty((F,4),np.int32);fn=np.full((F,4),-1,np.int32)
    uv=np.empty((T,2),np.float64) if with_uv else None
    ft=np.full((F,4),-1,np.int32) if with_uv else None
    seen={k:0 for k in counts}; vh=hashlib.sha256();nh=hashlib.sha256(); metadata=[];mtllibs=[]
    with path.open('rb') as f:
        for lineno,line in enumerate(f,1):
            tag,p=record(line)
            try:
                if tag==b'v':
                    if len(p)<3: raise ValueError('vertex needs x y z')
                    v[seen[b'v']]=[float(t) for t in p[:3]];vh.update(line)
                elif tag==b'vn': nh.update(line)
                elif tag==b'vt' and with_uv:
                    uv[seen[b'vt']]=[float(p[0]),float(p[1]) if len(p)>1 else 0.]
                elif tag==b'f':
                    fi=seen[b'f']
                    for k,tok in enumerate(p):
                        t=tok.split(b'/')
                        if len(t)>3:raise ValueError('invalid face token')
                        q[fi,k]=index(t[0],seen[b'v'],N,'v')
                        if len(t)>2 and t[2]:fn[fi,k]=index(t[2],seen[b'vn'],M,'vn')
                        if with_uv and len(t)>1 and t[1]:ft[fi,k]=index(t[1],seen[b'vt'],T,'vt')
                elif tag in {b'g',b'o',b's',b'usemtl',b'mtllib'}:
                    metadata.append([seen[b'f'],line.decode('utf-8','replace').rstrip('\r\n')])
                    if tag==b'mtllib':mtllibs.append(b' '.join(p).decode('utf-8','replace'))
                if tag in seen:seen[tag]+=1
            except (ValueError,IndexError) as exc:raise StopUV('MALFORMED_OBJ',f'Line {lineno}: {exc}') from exc
    if not np.isfinite(v).all():raise StopUV('NONFINITE_GEOMETRY','NaN/Inf in source positions.')
    if np.any(np.diff(np.sort(q,axis=1),axis=1)==0):raise StopUV('DEGENERATE_TOPOLOGY','A face repeats a vertex. No repair will be applied.')
    info={'vertices':N,'faces':F,'source_uv_vertices':T,'normals':M,'vertex_record_sha256':vh.hexdigest(),
          'normal_record_sha256':nh.hexdigest(),'metadata_records':metadata,'mtllibs':mtllibs,
          'quad_indices_sha256':hashlib.sha256(q.tobytes()).hexdigest()}
    return v,q,fn,info,uv,ft

def export_obj(source: Path, dest: Path, q, fn, uv) -> None:
    if source.resolve()==dest.resolve():raise StopUV('OVERWRITE_SOURCE','Never overwrite the input OBJ.')
    part=dest.with_suffix('.obj.part');inserted=False;face=0
    try:
        with source.open('rb') as inp, part.open('wb') as out:
            out.write(b'# rect-strip-uv: UV-only edit; original vertices, faces, normals and groups preserved.\n')
            for line in inp:
                tag,p=record(line)
                if tag==b'vt':continue
                if line.lstrip().startswith(b'#UV Vertex Count'):
                    out.write(f'#UV Vertex Count {len(uv)}\n'.encode('ascii'));continue
                if line.strip() and line.strip().strip(b'\x00')==b'':continue
                if tag!=b'f':out.write(line);continue
                if not inserted:
                    for start in range(0,len(uv),100_000):
                        text=''.join(f'vt {u:.16g} {v:.16g}\n' for u,v in uv[start:start+100_000])
                        out.write(text.encode('ascii'))
                    inserted=True
                parts=[]
                for vi,ni in zip(q[face],fn[face]):
                    i=int(vi)+1
                    parts.append(f'{i}/{i}/{int(ni)+1}' if ni>=0 else f'{i}/{i}')
                suffix=b''
                if b'#' in line:suffix=b' #'+line.split(b'#',1)[1].rstrip(b'\r\n')
                out.write(('f '+' '.join(parts)).encode('ascii')+suffix+b'\n');face+=1
        if face!=len(q):raise StopUV('SOURCE_CHANGED','Source face count changed while exporting.')
        os.replace(part,dest)
    except BaseException:
        # Incomplete .part is deliberately not promoted to a finished OBJ.
        raise
