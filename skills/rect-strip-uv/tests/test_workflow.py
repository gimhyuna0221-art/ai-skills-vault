"""Run: python -m unittest discover -s tests -v (from skill folder)."""
from __future__ import annotations
import json,subprocess,sys,tempfile,unittest
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from mesh_io import read_obj,export_obj,StopUV,sha256
from parameterize import unwrap,validate_island,topology,components,coarse_levels,prolong


def strip(nx=40,ny=8,bent=False):
    v=np.array([[i/nx*12,j/ny,0.] for i in range(nx+1) for j in range(ny+1)])
    if bent:
        x=v[:,0].copy();y=v[:,1].copy();r=3.
        v=np.c_[r*np.sin(x/r),y,r*np.cos(x/r)+.04*np.sin(3*x)]
    q=np.array([[i*(ny+1)+j,(i+1)*(ny+1)+j,(i+1)*(ny+1)+j+1,i*(ny+1)+j+1]
                for i in range(nx) for j in range(ny)],np.int32)
    return v,q

def subdivision(v,q):
    verts=list(v.copy());edge={};faces=[]
    for a,b,c,d in q:
        mids=[]
        for i,j in [(a,b),(b,c),(c,d),(d,a)]:
            key=tuple(sorted([int(i),int(j)]))
            if key not in edge:edge[key]=len(verts);verts.append((v[i]+v[j])*.5)
            mids.append(edge[key])
        m=len(verts);verts.append((v[a]+v[b]+v[c]+v[d])*.25);ab,bc,cd,da=mids
        faces.extend([[a,ab,m,da],[ab,b,bc,m],[m,bc,c,cd],[da,m,cd,d]])
    return np.array(verts),np.array(faces,np.int32)

def write(path,v,q,negative=False,normals=False,old_uv=False):
    with path.open('w',encoding='utf-8') as f:
        f.write('# test OBJ; not user geometry\nmtllib not-supplied.mtl\n')
        for p in v:f.write('v '+' '.join(f'{x:.12g}' for x in p)+'\n')
        if normals:f.write('vn 0 0 1\n')
        if old_uv:f.write('vt 0 0\n')
        f.write('o Strap\ng StrapGroup\ns 1\nusemtl leather\n')
        for qq in q:
            parts=[]
            for i in qq:
                a=str(int(i)-len(v) if negative else int(i)+1)
                if normals:a+='/1/1' if old_uv else '//1'
                elif old_uv:a+='/1'
                parts.append(a)
            f.write('f '+' '.join(parts)+'\n')

class SolverTests(unittest.TestCase):
    def test_regular_strip_rectangular_exact(self):
        v,q=strip();u,m,t=unwrap(v,q)
        self.assertEqual(m['route'],'regular-quad-grid')
        self.assertTrue(np.allclose(np.ptp(u,axis=0),[12,1]))
        self.assertEqual(validate_island(u,q,t['boundary'])['nonpositive_triangles'],0)

    def test_folded_shape_unchanged(self):
        v,q=strip(bent=True);original=v.copy();faces=q.copy();u,m,t=unwrap(v,q)
        self.assertTrue(np.array_equal(v,original));self.assertTrue(np.array_equal(q,faces))
        self.assertEqual(validate_island(u,q,t['boundary'])['nonconvex_quads'],0)

    def test_geodesic_caps_with_explicit_endpoints(self):
        v,q=strip(bent=True);u,m,t=unwrap(v,q,endpoints=[4,40*9+4])
        self.assertEqual(m['route'],'capsule-boundary-mean-value')
        self.assertEqual(m['attached_end_count'],2)
        self.assertTrue(validate_island(u,q,t['boundary'])['boundary_simple'])

    def test_two_components(self):
        v,q=strip();vv=np.r_[v,v+[0,4,0]];qq=np.r_[q,q+len(v)]
        self.assertEqual(len(components(qq,len(vv))),2)

    def test_subdivision_prolongation_preserves_all_quads(self):
        v,q=strip(20,4);fv,fq=subdivision(v,q);fv,fq=subdivision(fv,fq)
        levels=coarse_levels(fq);ids=np.unique(levels[-1]);uv,_,_=unwrap(fv[ids],np.searchsorted(ids,levels[-1]))
        full=prolong(levels,ids,uv,len(fv));top=topology(fq,len(fv))
        self.assertGreaterEqual(len(levels),3);self.assertTrue(np.isfinite(full).all())
        self.assertEqual(validate_island(full,fq,top['boundary'])['nonpositive_triangles'],0)

    def test_reordered_faces_no_assumed_subdivision(self):
        v,q=strip(20,4);v,q=subdivision(v,q);q=q[np.random.default_rng(10).permutation(len(q))]
        self.assertEqual(len(coarse_levels(q)),1)
        uv,_,t=unwrap(v,q);self.assertEqual(validate_island(uv,q,t['boundary'])['nonconvex_quads'],0)

    def test_negative_indices_normals_groups(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/'source.obj';out=Path(d)/'out.obj';v,q=strip(20,4)
            write(src,v,q,negative=True,normals=True,old_uv=True)
            a,b,n,info,_,_=read_obj(src);u,_,_=unwrap(a,b);before=sha256(src);export_obj(src,out,b,n,u)
            aa,bb,nn,after,uu,ft=read_obj(out,with_uv=True)
            self.assertEqual(sha256(src),before);self.assertTrue(np.array_equal(a,aa));self.assertTrue(np.array_equal(b,bb))
            self.assertTrue(np.array_equal(n,nn));self.assertTrue(np.array_equal(ft,b));self.assertEqual(info['metadata_records'],after['metadata_records'])
            self.assertEqual(info['vertex_record_sha256'],after['vertex_record_sha256'])

    def test_no_old_uv_export(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'in.obj';o=Path(d)/'out.obj';v,q=strip(20,4);write(p,v,q)
            vv,qq,nn,_,_,_=read_obj(p);uv,_,_=unwrap(vv,qq);export_obj(p,o,qq,nn,uv)
            *_,u,f=read_obj(o,with_uv=True);self.assertEqual(len(u),len(v));self.assertTrue(np.array_equal(f,q))

    def test_hole_stops(self):
        v,q=strip(20,4);q=np.delete(q,42,axis=0)
        with self.assertRaises(StopUV) as ex:topology(q,len(v))
        self.assertEqual(ex.exception.code,'NOT_DISK')

    def test_nonquad_stops(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'tri.obj';p.write_text('v 0 0 0\nv 1 0 0\nv 0 1 0\nf 1 2 3\n')
            with self.assertRaises(StopUV) as ex:read_obj(p)
            self.assertEqual(ex.exception.code,'QUADS_REQUIRED')

    def test_inconsistent_winding_stops(self):
        v,q=strip(20,4);q[5]=q[5,::-1]
        with self.assertRaises(StopUV) as ex:topology(q,len(v))
        self.assertEqual(ex.exception.code,'INCONSISTENT_WINDING')

    def test_uv_flip_is_not_approved(self):
        v,q=strip(20,4);u,_,t=unwrap(v,q);u[:,1]*=-1
        with self.assertRaises(StopUV):validate_island(u,q,t['boundary'])

    def test_full_cli_resume_and_source_guard(self):
        with tempfile.TemporaryDirectory() as d:
            d=Path(d);src=d/'sample.obj';work=d/'job';v,q=strip(20,4,True);write(src,v,q)
            cli=[sys.executable,str(ROOT/'scripts/rect_strip_uv.py')]
            def call(extra):return subprocess.run(cli+extra,capture_output=True,text=True,timeout=100)
            a=call(['run','--input',str(src),'--work',str(work),'--also-01','--stop-after','unwrap']);self.assertEqual(a.returncode,0,a.stdout+a.stderr)
            initial=json.loads((work/'state.json').read_text());b=call(['resume','--work',str(work)])
            self.assertEqual(b.returncode,0,b.stdout+b.stderr);final=json.loads((work/'state.json').read_text())
            self.assertEqual(initial['done']['inspect'],final['done']['inspect']);self.assertEqual(final['status'],'NUMERIC_PASS_VISUAL_REVIEW_REQUIRED')
            self.assertTrue((work/'rect_strip_uv_delivery.zip').is_file())
            (src).write_text(src.read_text()+'# source changed\n');c=call(['resume','--work',str(work)])
            self.assertEqual(c.returncode,2);self.assertIn('SOURCE_CHANGED',c.stdout+c.stderr)

    def test_checkpoint_tamper_guard(self):
        with tempfile.TemporaryDirectory() as d:
            d=Path(d);src=d/'sample.obj';work=d/'job';v,q=strip(20,4);write(src,v,q)
            cmd=[sys.executable,str(ROOT/'scripts/rect_strip_uv.py')]
            a=subprocess.run(cmd+['inspect','--input',str(src),'--work',str(work)],capture_output=True,text=True)
            self.assertEqual(a.returncode,0,a.stdout+a.stderr)
            with (work/'quads.npy').open('ab') as f:f.write(b'tamper')
            b=subprocess.run(cmd+['resume','--work',str(work)],capture_output=True,text=True)
            self.assertEqual(b.returncode,2);self.assertIn('CHECKPOINT_CHANGED',b.stdout+b.stderr)

if __name__=='__main__':unittest.main()
