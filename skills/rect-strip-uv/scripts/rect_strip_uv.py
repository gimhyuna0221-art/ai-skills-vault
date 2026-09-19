#!/usr/bin/env python3
"""Reproducible UV-only workflow: inspect -> unwrap -> export -> verify -> preview.
Run --help for commands. Requires no Blender, cloud API, or model inside the solver.
"""
from __future__ import annotations
import os
# Avoid multiplying CPU/memory use on agent runners. Set externally to override.
for _var in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:
    os.environ.setdefault(_var,'2')
import argparse,hashlib,json,sys,time,socket,zipfile,platform,shutil
from pathlib import Path
try:
    import numpy as np
    from mesh_io import StopUV,sha256,json_write,np_save,read_obj,export_obj
    from parameterize import components,topology,coarse_levels,unwrap,prolong,validate_island
except ImportError as exc:
    print(f'MISSING_DEPENDENCY: {exc}\nInstall: python -m pip install -r "{Path(__file__).resolve().parents[1]/"requirements.txt"}"',file=sys.stderr)
    raise SystemExit(3)

VERSION='1.0.0'
STAGES=['inspect','unwrap','export','verify','preview','package']

def code_hash():
    h=hashlib.sha256()
    for p in sorted(Path(__file__).parent.glob('*.py')):h.update(p.name.encode());h.update(p.read_bytes())
    return h.hexdigest()

class Job:
    def __init__(self,work: Path, state: dict):self.work=work;self.state=state;self.source=Path(state['input']);self.out=work/'delivery';self.out.mkdir(exist_ok=True)
    def event(self,text,**extra):
        data={'time':time.strftime('%Y-%m-%dT%H:%M:%S%z'),'message':text,**extra}
        print(json.dumps(data,ensure_ascii=False),flush=True)
        with (self.work/'progress.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(data,ensure_ascii=False)+'\n')
    def save(self):json_write(self.work/'state.json',self.state)
    def load(self,name):return np.load(self.work/name,mmap_mode='r',allow_pickle=False)
    def info(self):return json.loads((self.work/'source_info.json').read_text(encoding='utf-8'))
    def execute(self,stop_after=None):
        if sha256(self.source)!=self.state['source_sha256']:raise StopUV('SOURCE_CHANGED','Input bytes changed. Use a NEW work directory; checkpoints cannot be reused.')
        if code_hash()!=self.state['code_sha256']:raise StopUV('CODE_CHANGED','Solver scripts changed. Use a NEW work directory; do not mix checkpoints.')
        for stage in STAGES:
            if stage in self.state['done']:
                for name,h in self.state['done'][stage]['artifacts'].items():
                    p=self.work/name
                    if not p.is_file() or sha256(p)!=h:raise StopUV('CHECKPOINT_CHANGED',f'Checkpoint/output missing or modified: {name}. Use a new work directory.')
                self.event('stage_reused',stage=stage)
            else:
                self.state['status']='RUNNING';self.state['current_stage']=stage;self.save();self.event('stage_started',stage=stage)
                started=time.monotonic();paths=getattr(self,'stage_'+stage)()
                self.state['done'][stage]={'seconds':round(time.monotonic()-started,3),
                    'artifacts':{str(p.relative_to(self.work)):sha256(p) for p in paths}}
                self.state['current_stage']=None;self.save();self.event('stage_saved',stage=stage,seconds=self.state['done'][stage]['seconds'])
            if stage==stop_after:
                self.state['status']='CHECKPOINT_SAVED';self.save();return
        self.state['status']='NUMERIC_PASS_VISUAL_REVIEW_REQUIRED';self.save()
        self.event('delivery_ready',directory=str(self.out),zip=str(self.work/'rect_strip_uv_delivery.zip'),visual_review='required')

    def stage_inspect(self):
        cfg=self.state['config'];v,q,fn,info,_,_=read_obj(self.source,max_faces=cfg['max_faces'])
        paths=[]
        for name,a in [('vertices.npy',v),('quads.npy',q),('normal_indices.npy',fn)]:
            p=self.work/name;np_save(p,a);paths.append(p)
        comps=components(q,len(v));report=[]
        if len(comps)>32:raise StopUV('TOO_MANY_COMPONENTS','More than 32 disconnected components; likely not a belt-only export.')
        for c,faceids in enumerate(comps):
            globalq=q[faceids];ids=np.unique(globalq);localq=np.searchsorted(ids,globalq).astype(np.int32)
            top=topology(localq,len(ids))
            levels=coarse_levels(globalq)
            for i,a in enumerate(levels):
                p=self.work/f'c{c}_level{i}.npy';np_save(p,a);paths.append(p)
            for suffix,a in [('faces',faceids),('boundary',ids[top['boundary']]),('base_ids',np.unique(levels[-1]))]:
                p=self.work/f'c{c}_{suffix}.npy';np_save(p,a);paths.append(p)
            item={'component':c,'faces':len(globalq),'vertices':len(ids),'subdivision_levels':len(levels)-1,
                  'control_vertices':len(np.unique(levels[-1])),'control_quads':len(levels[-1]),
                  'boundary_vertices':len(top['boundary']),'boundary_loops':1,'euler_characteristic':1,
                  'oriented_manifold':True,'bbox':[v[ids].min(0).tolist(),v[ids].max(0).tolist()]}
            if item['control_vertices']>cfg['max_base_vertices']:
                raise StopUV('RESOURCE_LIMIT',f'Component {c}: {item["control_vertices"]} control vertices exceeds {cfg["max_base_vertices"]}; no guessing or decimation.')
            report.append(item);self.event('component_inspected',**item)
        info['components']=report;info['source_sha256']=self.state['source_sha256']
        p=self.work/'source_info.json';json_write(p,info);paths.append(p)
        return paths

    def stage_unwrap(self):
        info=self.info();cfg=self.state['config'];v=self.load('vertices.npy');N=len(v);fulluv=np.full((N,2),np.nan)
        Wref=cfg.get('tile_width');voffset=0.;records=[];paths=[]
        endpoint_cfg=cfg.get('endpoints') or {}
        for comp in info['components']:
            c=comp['component'];ids=self.load(f'c{c}_base_ids.npy');baseq=self.load(f'c{c}_level{comp["subdivision_levels"]}.npy')
            localq=np.searchsorted(ids,baseq).astype(np.int32);endpoints=None
            if str(c) in endpoint_cfg:
                pair=np.asarray(endpoint_cfg[str(c)],np.int64)-1
                if len(pair)!=2 or not np.all(np.isin(pair,ids)):raise StopUV('INVALID_ENDPOINTS','Endpoints are 1-based OBJ vertex IDs and must survive the proven subdivision control hierarchy.')
                endpoints=np.searchsorted(ids,pair)
            self.event('component_solve',component=c,control_vertices=len(ids))
            u,meta,top=unwrap(v[ids],localq,endpoints=endpoints,max_base_vertices=cfg['max_base_vertices'])
            width=float(meta['reference_width']);Wref=width if Wref is None else Wref
            u*=width/Wref;u-=u.min(0);u[:,1]+=voffset
            levels=[self.load(f'c{c}_level{i}.npy') for i in range(comp['subdivision_levels']+1)]
            propagated=prolong(levels,ids,u,N);used=np.unique(levels[0]);fulluv[used]=propagated[used]
            if not np.isfinite(fulluv[used]).all():raise StopUV('MISSING_UV','UV prolongation left unmapped vertices.')
            voffset=float(np.ceil(fulluv[used,1].max()+.15))
            meta.update({'component':c,'uv_min':fulluv[used].min(0).tolist(),'uv_max':fulluv[used].max(0).tolist(),
                         'world_units_per_tile':Wref,'subdivision_levels_used':comp['subdivision_levels']})
            if 'endpoints_control_indices' in meta:
                meta['endpoints_source_obj_1based']=(ids[meta['endpoints_control_indices']]+1).tolist()
            records.append(meta)
            p=self.work/f'c{c}_base_uv.npy';np_save(p,u);paths.append(p)
            self.event('component_uv_ready',component=c,route=meta['route'],attempts=meta['attempts'])
        if not np.isfinite(fulluv).all():raise StopUV('MISSING_UV','Some original vertices lack UV.')
        for item in records:
            c=item['component'];item['full_resolution_checks']=validate_island(fulluv,self.load(f'c{c}_level0.npy'),self.load(f'c{c}_boundary.npy'))
        lo=fulluv.min(0);span=np.ptp(fulluv,axis=0);scale=.96/max(span)
        packed=(fulluv-lo)*scale
        packed+=(1-np.ptp(packed,axis=0))*.5
        meta={'components':records,'reference_width':Wref,'tile_bounds':[fulluv.min(0).tolist(),fulluv.max(0).tolist()],
              'packed_uniform_scale':scale,'uv_islands':len(records),'geometry_modified':False,
              'method':'Topology-only control recovery; regular quad grid OR convex caps + straight rails + checked mean-value solve; UV-only prolongation.'}
        for name,a in [('uv_tile.npy',fulluv),('uv_01.npy',packed)]:
            p=self.work/name;np_save(p,a);paths.append(p)
        p=self.work/'uv_manifest.json';json_write(p,meta);paths.append(p)
        return paths

    def stage_export(self):
        q=self.load('quads.npy');fn=self.load('normal_indices.npy');paths=[]
        modes=['tile','01'] if self.state['config']['also_01'] else ['tile']
        for mode in modes:
            p=self.out/f'{self.source.stem}_UV_{mode}.obj'
            export_obj(self.source,p,q,fn,self.load('uv_'+mode+'.npy'));paths.append(p)
            self.event('obj_exported',mode=mode,bytes=p.stat().st_size)
        return paths

    def stage_verify(self):
        src=self.info();v=self.load('vertices.npy');q=self.load('quads.npy');fn=self.load('normal_indices.npy')
        modes=['tile','01'] if self.state['config']['also_01'] else ['tile'];reports=[];actual=None
        for mode in modes:
            path=self.out/f'{self.source.stem}_UV_{mode}.obj';self.event('reloading_obj',file=path.name)
            ov,oq,on,oi,u,ft=read_obj(path,max_faces=self.state['config']['max_faces'],with_uv=True)
            checks={'vertex_coordinates_equal':np.array_equal(v,ov),'vertex_records_byte_identical':src['vertex_record_sha256']==oi['vertex_record_sha256'],
                    'face_connectivity_and_order_equal':np.array_equal(q,oq),'face_normal_indices_equal':np.array_equal(fn,on),
                    'normal_records_byte_identical':src['normal_record_sha256']==oi['normal_record_sha256'],
                    'object_group_smoothing_material_records_preserved':src['metadata_records']==oi['metadata_records'],
                    'all_corners_have_valid_uv':np.array_equal(ft,q) and len(u)==len(v),
                    'all_faces_quad':oq.shape==q.shape}
            if not all(checks.values()):raise StopUV('GEOMETRY_PRESERVATION_FAILED',str(checks))
            island_checks=[];ranges=[]
            for comp in src['components']:
                c=comp['component'];qq=self.load(f'c{c}_level0.npy');bd=self.load(f'c{c}_boundary.npy')
                island_checks.append(validate_island(u,qq,bd));used=np.unique(qq);ranges.append((u[used,1].min(),u[used,1].max()))
            if any(ranges[i][1]>=ranges[i+1][0] for i in range(len(ranges)-1)):raise StopUV('ISLAND_OVERLAP','Island V ranges are not disjoint.')
            reports.append({'file':path.name,'sha256':sha256(path),'bytes':path.stat().st_size,'checks':checks,'islands':island_checks,'island_bounds_disjoint':True})
            if mode=='tile':actual=u.copy()
            self.event('obj_verified',file=path.name,uv_islands=len(island_checks))
        manifest=json.loads((self.work/'uv_manifest.json').read_text())
        qa={'status':'NUMERIC_PASS_VISUAL_REVIEW_REQUIRED','skill_version':VERSION,'code_sha256':code_hash(),
            'source_sha256':self.state['source_sha256'],'source_vertices':src['vertices'],'source_quads':src['faces'],
            'source_normals':src['normals'],'geometry_modified':False,'uv_islands':len(src['components']),
            'files':reports,'mapping':manifest,'overlap_check':'Oriented manifold disk per component; positive triangles and strict convex quads; simple boundary; area match; disjoint island V ranges.',
            'limitations':['No DCC application round-trip was performed.','No distortion-free claim: curved surfaces and rounded caps retain local stretch.',
                'Endpoint selection is a geodesic heuristic, not semantic understanding. Inspect actual checker previews.',
                'No body collision/shape repair/thickness/hole cutting/topology changes are performed.','A lower-reasoning model evaluation is separate from testing this solver.'],
            'runtime':{'python':platform.python_version(),'platform':platform.platform(),'numpy':np.__version__}}
        missing=[]
        for name in src['mtllibs']:
            # Do not copy external, parent-traversing or ambiguous references automatically.
            p=Path(name)
            if p.name!=name or not (self.source.parent/p).is_file():missing.append(name)
        qa['material_assets_not_bundled']=src['mtllibs'];qa['missing_or_external_mtl']=missing
        p=self.out/'QA_report.json';json_write(p,qa)
        np_save(self.work/'uv_verified.npy',actual)
        return [p,self.work/'uv_verified.npy']

    def stage_preview(self):
        from preview import render,layout
        v=self.load('vertices.npy');q=self.load('quads.npy');u=self.load('uv_verified.npy')
        p1=self.out/'UV_checker.png';p2=self.out/'UV_checker_front.png';p3=self.out/'UV_layout.png'
        render(v,q,u,p1,title='UV CHECK | actual full-resolution geometry; UV only')
        self.event('preview_saved',file=p1.name)
        render(v,q,u,p2,direction=(0,.13,1),title='UV CHECK | front view; no geometry changes')
        layout(self,p3)
        return [p1,p2,p3]

    def stage_package(self):
        info=self.info();text=(f'UV-only results from rect-strip-uv {VERSION}\n\n'
          f'Input: {self.source.name}\nVertices: {info["vertices"]}; quad faces: {info["faces"]}\n'
          f'Main file: {self.source.stem}_UV_tile.obj\n'
          'U follows length; V follows width. The body rails are straight; ends remain attached.\n'
          'UVs outside 0-1 are intentional repeat coordinates, NOT a multi-image UDIM set.\n'
          'The optional 01 version uses ONE uniform scale; it does not squash the long strips into squares.\n'
          'Load one OBJ alternative, not both. Source geometry and normals are preserved.\n'
          'Only open quad disks are supported. No seams, holes, thickness or remeshing are created.\n'
          'Original material names are preserved; MTL/textures are not bundled or invented.\n'
          'Inspect UV_layout.png and both checker images. Numeric PASS is not visual approval.\n'
          'See QA_report.json for exact checks, source hash and limitations.\n')
        p=self.out/'README.txt';p.write_text(text,encoding='utf-8')
        dst=self.work/'rect_strip_uv_delivery.zip';temp=dst.with_suffix('.zip.part')
        allowed=[p]+[self.work/name for stage in ['export','verify','preview'] for name in self.state['done'][stage]['artifacts'] if Path(name).parent==Path('delivery')]
        with zipfile.ZipFile(temp,'w',zipfile.ZIP_DEFLATED,compresslevel=5,allowZip64=True) as z:
            for f in allowed:z.write(f,arcname=f.name)
        with zipfile.ZipFile(temp) as z:
            if z.testzip() is not None:raise StopUV('ZIP_INVALID','ZIP CRC validation failed.')
        os.replace(temp,dst)
        return [p,dst]


def parser():
    p=argparse.ArgumentParser(description=__doc__)
    sub=p.add_subparsers(dest='command',required=True)
    for cmd in ['run','inspect']:
        s=sub.add_parser(cmd);s.add_argument('--input',type=Path,required=True);s.add_argument('--work',type=Path,required=True)
        s.add_argument('--also-01',action='store_true',help='Also deliver a uniformly scaled 0-1 alternative.')
        s.add_argument('--max-faces',type=int,default=3_000_000);s.add_argument('--max-base-vertices',type=int,default=150_000)
        s.add_argument('--tile-width',type=float,default=None,help='Scene units per UV tile, not assumed cm. Default: first belt reference width.')
        s.add_argument('--endpoints',type=Path,help='Optional JSON {"0":[A,B]} of 1-based input OBJ vertex IDs on the control boundary.')
        s.add_argument('--stop-after',choices=STAGES,default=None)
    for cmd in ['resume','status']:
        s=sub.add_parser(cmd);s.add_argument('--work',type=Path,required=True)
        if cmd=='resume':s.add_argument('--stop-after',choices=STAGES,default=None)
    sub.add_parser('doctor')
    return p


def main():
    args=parser().parse_args()
    if args.command=='doctor':
        import scipy,shapely,PIL,numba
        print(json.dumps({'status':'READY','python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,
                          'shapely':shapely.__version__,'Pillow':PIL.__version__,'numba':numba.__version__,'skill':VERSION},indent=2));return 0
    work=args.work.resolve();state_path=work/'state.json'
    if args.command=='status':
        print(state_path.read_text(encoding='utf-8') if state_path.exists() else '{"status":"NOT_STARTED"}');return 0
    work.mkdir(parents=True,exist_ok=True)
    if args.command in ['run','inspect']:
        source=args.input.resolve()
        if not source.is_file():raise StopUV('INPUT_MISSING',str(source))
        if source.suffix.lower()!='.obj':raise StopUV('OBJ_REQUIRED','Use an OBJ file, not a screenshot or .max file.')
        if work==source or work in source.parents:raise StopUV('UNSAFE_WORK_PATH','Keep input outside the job work directory.')
        ep=json.loads(args.endpoints.read_text()) if args.endpoints else None
        cfg={'also_01':args.also_01,'max_faces':args.max_faces,'max_base_vertices':args.max_base_vertices,'tile_width':args.tile_width,'endpoints':ep}
        if args.tile_width is not None and args.tile_width<=0:raise StopUV('INVALID_OPTION','--tile-width must be positive.')
        if state_path.exists():
            state=json.loads(state_path.read_text())
            if state['input']!=str(source) or state['config']!=cfg:raise StopUV('CONFIG_CHANGED','Use resume for the previous job, or a NEW work directory for changed input/options.')
        else:
            state={'version':VERSION,'input':str(source),'source_sha256':sha256(source),'code_sha256':code_hash(),
                   'config':cfg,'done':{},'status':'NEW','current_stage':None}
            json_write(state_path,state)
    else:
        if not state_path.exists():raise StopUV('NO_CHECKPOINT','state.json does not exist. Start with run.')
        state=json.loads(state_path.read_text())
    lock=work/'run.lock'
    if lock.exists():
        content=json.loads(lock.read_text())
        stale=False
        if content.get('host')==socket.gethostname() and os.name=='posix':
            try:os.kill(int(content['pid']),0)
            except ProcessLookupError:stale=True
            except PermissionError:pass
        if stale:lock.unlink()
        else:raise StopUV('JOB_LOCKED',f'Job lock: {content}. Do not start a duplicate worker. Check whether that process is still running.')
    fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY)
    with os.fdopen(fd,'w') as f:json.dump({'pid':os.getpid(),'host':socket.gethostname()},f)
    job=Job(work,state)
    try:
        stop='inspect' if args.command=='inspect' else args.stop_after
        job.execute(stop);return 0
    except (StopUV,Exception) as exc:
        code=getattr(exc,'code','INTERNAL_ERROR');state['status']='STOPPED';state['error']={'code':code,'message':str(exc)};job.save()
        job.event('stopped',code=code,detail=str(exc));return 2
    finally:
        if lock.exists():lock.unlink()

if __name__=='__main__':
    try:raise SystemExit(main())
    except StopUV as exc:
        print(json.dumps({'status':'STOPPED','code':exc.code,'message':str(exc)},ensure_ascii=False),file=sys.stderr);raise SystemExit(2)
