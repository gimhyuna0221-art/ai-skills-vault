"""Bounded rectangular-strip UV construction; never changes mesh positions.
Derived from this conversation's verified boundary/MVC/UV-prolongation workflow.
"""
from __future__ import annotations
import warnings
import numpy as np
from scipy.sparse import coo_matrix,diags
from scipy.sparse.linalg import spsolve,MatrixRankWarning
from scipy.sparse.csgraph import connected_components,dijkstra
from shapely.geometry import Polygon
from mesh_io import StopUV


def components(q, n):
    e=np.concatenate([q[:,[0,1]],q[:,[1,2]],q[:,[2,3]],q[:,[3,0]]])
    g=coo_matrix((np.ones(len(e),np.uint8),(e[:,0],e[:,1])),shape=(n,n)).tocsr()
    count,labels=connected_components(g,directed=False)
    used=np.unique(q)
    if len(used)!=n:raise StopUV('LOOSE_VERTICES','Unreferenced vertices found. Export only the intended strip surfaces; do not weld automatically.')
    return [np.flatnonzero(labels[q[:,0]]==i) for i in range(count)]


def topology(q, n):
    """Check disk, edge orientations, boundary chain and a vertex-link manifold test."""
    # Face-major directed edges; the inverse table also serves the grid traversal.
    de=np.stack((q,np.roll(q,-1,axis=1)),axis=-1).reshape(-1,2)
    key=np.minimum(de[:,0],de[:,1]).astype(np.int64)*n+np.maximum(de[:,0],de[:,1])
    unique,idx,inv,cnt=np.unique(key,return_index=True,return_inverse=True,return_counts=True)
    if np.any(cnt>2):raise StopUV('NONMANIFOLD','An edge belongs to more than two faces.')
    orient=np.where(de[:,0]<de[:,1],1,-1)
    sums=np.bincount(inv,weights=orient,minlength=len(cnt))
    if np.any(sums[cnt==2]!=0):raise StopUV('INCONSISTENT_WINDING','Shared edges have inconsistent face winding.')
    edges=de[idx];bed=edges[cnt==1]
    if len(bed)<4:raise StopUV('NOT_OPEN_STRIP','No open strip boundary: closed/thick solids need an explicit seam workflow, not this skill.')
    if n-len(edges)+len(q)!=1:raise StopUV('NOT_DISK','Component is not a topological disk (hole, closed ring, or handle). No seams/holes are created automatically.')
    starts,cc=np.unique(bed[:,0],return_counts=True);ends,dd=np.unique(bed[:,1],return_counts=True)
    if np.any(cc!=1) or np.any(dd!=1) or not np.array_equal(starts,ends):
        raise StopUV('BOUNDARY_BRANCH','Boundary branches or has inconsistent directions.')
    nxt=dict(bed.tolist());loop=[];cur=int(starts[0]);start=cur
    while not loop or cur!=start:
        if len(loop)>len(bed):raise StopUV('BOUNDARY_BRANCH','Boundary traversal did not close.')
        loop.append(cur);cur=nxt[cur]
    if len(loop)!=len(bed):raise StopUV('MULTIPLE_BOUNDARIES','Multiple boundary loops. No automatic seam/hole repair.')
    # A disk with consistently oriented faces must also have one face fan per vertex.
    # Corner union across opposite edges; compare each vertex's fan representative.
    twins=np.full(len(de),-1,np.int32)
    order=np.argsort(inv,kind='stable');offset=np.r_[0,np.cumsum(cnt)[:-1]]
    paired=np.flatnonzero(cnt==2);a=order[offset[paired]];b=order[offset[paired]+1]
    twins[a]=b;twins[b]=a
    check_vertex_fans(q,twins,n)
    return {'edges':edges,'boundary':np.asarray(loop,np.int32),'valence':np.bincount(edges.ravel(),minlength=n),
            'twins':twins,'euler':1,'boundary_count':1}

# Compilation is optional; the uncompiled loop is fine on the bounded control mesh.
try:
    from numba import njit
except ImportError:
    def njit(*args,**kwargs):return lambda f:f

@njit(cache=True)
def _fan_ok(q,twins,n):
    m=len(q)*4;first=np.full(n,-1,np.int64);cnt=np.zeros(n,np.int64)
    # For a boundary fan, begin at the corner whose preceding edge is boundary.
    for i in range(m):
        vi=q[i//4,i%4];cnt[vi]+=1
        prev=(i//4)*4+(i+3)%4
        if first[vi]<0 or twins[prev]<0:first[vi]=i
    for v in range(n):
        c=first[v]
        if c<0:return False
        start=c;visited=0
        while True:
            visited+=1
            t=twins[c]
            if t<0:break
            c=(t//4)*4+(t+1)%4
            if c==start:break
            if visited>cnt[v]:return False
        if visited!=cnt[v]:return False
    return True

def check_vertex_fans(q,twins,n):
    if not _fan_ok(q,twins,n):raise StopUV('NONMANIFOLD_VERTEX','A vertex has disconnected face fans.')


def coarse_levels(global_q, *, max_levels=12):
    """Recognize exact ordered 4-child subdivision blocks. NOT geometric decimation."""
    levels=[global_q]
    for _ in range(max_levels):
        f=levels[-1]
        if len(f)%4:break
        a=f.reshape(-1,4,4)
        checks=[a[:,0,2]==a[:,1,3],a[:,0,2]==a[:,2,0],a[:,0,2]==a[:,3,1],
                a[:,0,1]==a[:,1,0],a[:,1,2]==a[:,2,1],a[:,2,3]==a[:,3,2],a[:,3,0]==a[:,0,3]]
        if not all(np.all(z) for z in checks):break
        parent=a[:,np.arange(4),np.arange(4)]
        centre=a[:,0,2]
        # Reject forged/degenerate child patterns. Prolongation relies on disjoint roles.
        mids=np.stack([a[:,0,1],a[:,1,2],a[:,2,3],a[:,3,0]],axis=1)
        if len(np.unique(centre))!=len(centre):break
        if np.intersect1d(centre,parent).size or np.intersect1d(centre,mids).size or np.intersect1d(parent,mids).size:break
        if np.any(np.diff(np.sort(parent,axis=1),axis=1)==0):break
        levels.append(parent)
    return levels


def prolong(levels, coarse_ids, base_uv, n):
    result=np.full((n,2),np.nan);result[coarse_ids]=base_uv
    for fine in reversed(levels[:-1]):
        a=fine.reshape(-1,4,4);p=a[:,np.arange(4),np.arange(4)];u=result[p]
        if not np.isfinite(u).all():raise StopUV('PROLONGATION_FAILED','Missing parent UV.')
        for k,mid in enumerate([a[:,0,1],a[:,1,2],a[:,2,3],a[:,3,0]]):
            result[mid]=(u[:,k]+u[:,(k+1)%4])*.5
        result[a[:,0,2]]=u.mean(1)
    return result


def area_and_signs(uv,q,chunk=80_000):
    result={'nonpositive_triangles':0,'nonconvex_quads':0,'triangle_double_area_min':float('inf'),'uv_area':0.}
    for start in range(0,len(q),chunk):
        u=uv[q[start:start+chunk]];e=np.roll(u,-1,axis=1)-u;en=np.roll(e,-1,axis=1)
        corners=e[:,:,0]*en[:,:,1]-e[:,:,1]*en[:,:,0]
        a=u[:,1]-u[:,0];b=u[:,2]-u[:,0];c=u[:,3]-u[:,0]
        a1=a[:,0]*b[:,1]-a[:,1]*b[:,0];a2=b[:,0]*c[:,1]-b[:,1]*c[:,0]
        result['nonpositive_triangles']+=int(np.count_nonzero(a1<=0)+np.count_nonzero(a2<=0))
        result['nonconvex_quads']+=int(np.any(corners<=0,axis=1).sum())
        result['triangle_double_area_min']=min(result['triangle_double_area_min'],float(min(a1.min(),a2.min())))
        result['uv_area']+=float(np.sum(a1+a2)*.5)
    return result


def _solve(lap, uv, fixed):
    free=np.ones(len(uv),bool);free[fixed]=False;free=np.flatnonzero(free)
    if not len(free):return uv.copy()
    with warnings.catch_warnings():
        warnings.simplefilter('error',MatrixRankWarning)
        out=uv.copy();out[free]=spsolve(lap[free][:,free].tocsc(),-(lap[free][:,fixed]@uv[fixed]))
    if not np.isfinite(out).all():raise StopUV('SOLVE_FAILED','Nonfinite harmonic solution.')
    return out


def weights(v,q,kind):
    t=np.concatenate([q[:,[0,1,2]],q[:,[0,2,3]]]);n=len(v);rr=[];cc=[];vv=[]
    for k in range(3):
        i=t[:,k];j=t[:,(k+1)%3];h=t[:,(k+2)%3]
        a=v[j]-v[i];b=v[h]-v[i];la=np.linalg.norm(a,axis=1);lb=np.linalg.norm(b,axis=1)
        cross=np.linalg.norm(np.cross(a,b),axis=1);dot=np.einsum('ij,ij->i',a,b)
        if np.any(la==0) or np.any(lb==0) or np.any(cross==0):
            raise StopUV('ZERO_AREA_GEOMETRY','Zero-area control triangle; source was not modified.')
        if kind=='mean-value':
            half=np.clip(cross/np.maximum(la*lb+dot,np.finfo(float).tiny),1e-6,1e5)
            rr.extend([i,i]);cc.extend([j,h]);vv.extend([half/la,half/lb])
        else: # symmetric cotangent Laplacian; used only for tentative U relaxation.
            cot=dot/cross*.5
            rr.extend([j,h]);cc.extend([h,j]);vv.extend([cot,cot])
    mat=coo_matrix((np.concatenate(vv),(np.concatenate(rr),np.concatenate(cc))),shape=(n,n)).tocsr()
    if kind=='mean-value':mat=diags(1/np.asarray(mat.sum(1)).ravel())@mat
    return diags(np.asarray(mat.sum(1)).ravel())-mat


def try_grid(v,q,top):
    boundary=top['boundary'];val=top['valence'];inner=np.ones(len(v),bool);inner[boundary]=False
    if np.any(val[inner]!=4) or np.count_nonzero(val[boundary]==2)!=4:return None
    ij=np.full((len(v),2),2**30,np.int32);ij[q[0]]=[[0,0],[1,0],[1,1],[0,1]]
    done=np.zeros(len(q),bool);done[0]=True;queue=[0];twins=top['twins']
    for fi in queue:
        for k in range(4):
            tt=int(twins[fi*4+k])
            if tt<0:continue
            fj=tt//4;kk=tt%4
            if done[fj]:continue
            a,b=q[fj,kk],q[fj,(kk+1)%4];step=ij[b]-ij[a];rot=np.array([-step[1],step[0]])
            for vid,point in [(q[fj,(kk+2)%4],ij[b]+rot),(q[fj,(kk+3)%4],ij[a]+rot)]:
                if ij[vid,0]!=2**30 and not np.array_equal(ij[vid],point):return None
                ij[vid]=point
            done[fj]=True;queue.append(fj)
    if not np.all(done):return None
    ij-=ij.min(0);span=ij.max(0)
    if np.prod(span+1)!=len(v):return None
    # Choose long physical axis, not merely the higher polygon count.
    lengths=[];axes=[]
    ed=top['edges']
    for k in range(2):
        edk=ed[np.abs(ij[ed[:,0],k]-ij[ed[:,1],k])==1]
        col=np.minimum(ij[edk[:,0],k],ij[edk[:,1],k]);dist=np.linalg.norm(v[edk[:,1]]-v[edk[:,0]],axis=1)
        dd=np.bincount(col,weights=dist)/np.bincount(col)
        coord=np.r_[0,np.cumsum(dd)];axes.append(coord[ij[:,k]]);lengths.append(coord[-1])
    long=int(np.argmax(lengths));short=1-long;L=lengths[long];W=lengths[short]
    if L/W<4:return None
    uv=np.c_[axes[long]/W,axes[short]/W]
    if area_and_signs(uv,q)['nonpositive_triangles']:uv[:,1]=1-uv[:,1]
    if area_and_signs(uv,q)['nonpositive_triangles']:return None
    return uv,{'route':'regular-quad-grid','reference_width':W,'length':L,'endpoint_mode':'four-existing-corners',
               'rectangular_body':True,'cap_mode':'original-square-grid-ends','attempts':1}


def choose_ends(v,top,endpoints=None):
    loop=top['boundary'];ed=top['edges'];d=np.linalg.norm(v[ed[:,1]]-v[ed[:,0]],axis=1)
    if np.any(d<=0):raise StopUV('ZERO_LENGTH_EDGE','Zero-length edge.')
    graph=coo_matrix((np.r_[d,d],(np.r_[ed[:,0],ed[:,1]],np.r_[ed[:,1],ed[:,0]])),shape=(len(v),len(v))).tocsr()
    if endpoints is not None:
        A,B=map(int,endpoints)
        if A==B or A not in loop or B not in loop:raise StopUV('INVALID_ENDPOINTS','Both endpoints must be different boundary vertices.')
    else:
        A=int(loop[0])
        for _ in range(4):
            dist=dijkstra(graph,directed=False,indices=A);B=int(loop[np.argmax(dist[loop])]);A,B=B,A
        # A stable direction; not tied to world Y, belt position, or prior vertex IDs.
        A,B=sorted([A,B])
    rotated=np.roll(loop,-int(np.flatnonzero(loop==A)[0]));ib=int(np.flatnonzero(rotated==B)[0])
    p0=rotated[:ib+1];p1=np.r_[rotated[0],rotated[:ib-1:-1]]
    arcs=[np.r_[0,np.cumsum(np.linalg.norm(np.diff(v[p],axis=0),axis=1))] for p in [p0,p1]]
    if min(len(p0),len(p1))<3:raise StopUV('ENDPOINT_AMBIGUITY','Too few boundary samples at an end.')
    return [p0,p1],arcs,[A,B]


def unwrap(v,q, *, endpoints=None, max_base_vertices=150_000):
    if len(v)>max_base_vertices:
        raise StopUV('RESOURCE_LIMIT',f'Control mesh has {len(v)} vertices; limit={max_base_vertices}. No proven subdivision ordering was available to reduce the UV solve. Original geometry remains intact.')
    top=topology(q,len(v))
    if endpoints is None:
        regular=try_grid(v,q,top)
        if regular is not None:return regular[0],regular[1],top
    paths,arcs,ends=choose_ends(v,top,endpoints)
    t=np.r_[q[:,[0,1,2]],q[:,[0,2,3]]]
    area=float(np.linalg.norm(np.cross(v[t[:,1]]-v[t[:,0]],v[t[:,2]]-v[t[:,0]]),axis=1).sum()*.5)
    perimeter_half=sum(a[-1] for a in arcs)*.5
    W=area/perimeter_half
    W=area/max(perimeter_half-(np.pi/2-1)*W,1e-12)
    L=perimeter_half-(np.pi/2-1)*W
    if W<=0 or L/W<4:raise StopUV('NOT_LONG_STRIP',f'Estimated length/width={L/W:.3g}; requires at least 4.0.')
    if max(a[-1] for a in arcs)/min(a[-1] for a in arcs)>1.65:
        raise StopUV('ENDPOINT_AMBIGUITY','Boundary paths have very different lengths; specify physical end vertices, do not force the UV.')
    # Keep valence-2 boundary turns inside the attached caps, never flatten them on a rail.
    ca=cb=np.pi*.25*W
    for p,s in zip(paths,arcs):
        for i in np.flatnonzero(top['valence'][p]==2):
            nearA=s[i]<=s[-1]/2;distance=s[i] if nearA else s[-1]-s[i]
            if distance>2.5*W:raise StopUV('ENDPOINT_AMBIGUITY','A topological boundary corner is far from both ends.')
            pad=max(.08*W, float(np.max(np.diff(s[max(0,i-1):min(len(s),i+2)])))*1.2)
            if nearA:ca=max(ca,distance+pad)
            else:cb=max(cb,distance+pad)
    mvc=weights(v,q,'mean-value');cot=None;history=[]
    for capmult in [1.,1.2,1.5]:
        capA=ca*capmult;capB=cb*capmult
        if capA+capB>.35*min(a[-1] for a in arcs):continue
        base=np.zeros((len(v),2));rail_lists=[]
        for side,(p,s) in enumerate(zip(paths,arcs)):
            aa=s<capA;bb=(s>s[-1]-capB)&~aa;mm=~(aa|bb)
            u=np.empty(len(p));vv=np.empty(len(p))
            angle=s[aa]/capA*np.pi/2
            u[aa]=.5*(1-np.cos(angle));vv[aa]=.5-.5*np.sin(angle)
            u[mm]=.5+(s[mm]-capA)/(s[-1]-capA-capB)*(L/W-1);vv[mm]=0.
            angle=(s[bb]-(s[-1]-capB))/capB*np.pi/2
            u[bb]=L/W-.5+.5*np.sin(angle);vv[bb]=.5-.5*np.cos(angle)
            if side:vv=1-vv
            base[p]=np.c_[u,vv];rail_lists.append(p[mm])
        raw=_solve(mvc,base,top['boundary'])
        if area_and_signs(raw,q)['nonpositive_triangles']>len(q):
            base[:,1]=1-base[:,1];raw[:,1]=1-raw[:,1]
        # Tentative free-sliding longitudinal cotangent relaxation. Never export it unchecked.
        try:
            if cot is None:cot=weights(v,q,'cotangent')
            fixed=top['boundary'][(base[top['boundary'],1]>1e-12)&(base[top['boundary'],1]<1-1e-12)]
            relaxed=_solve(cot,base[:,0],fixed)
        except Exception:
            relaxed=base[:,0].copy()
        for alpha in [1.,.5,.25,0.]:
            boundary_uv=base.copy();valid=True
            for ids in rail_lists:
                s=base[ids,0];dist=np.maximum(np.minimum(s-.5,L/W-.5-s),0.)
                end_pin=1-np.exp(-(dist/.80)**2)
                proposed=s+alpha*end_pin*(relaxed[ids]-s)
                if np.any(np.diff(proposed)<=0) or np.any(proposed<=.5) or np.any(proposed>=L/W-.5):valid=False;break
                boundary_uv[ids,0]=proposed
            if not valid:history.append({'cap_multiplier':capmult,'alpha':alpha,'result':'rail-order-rejected'});continue
            uv=_solve(mvc,boundary_uv,top['boundary'])
            checks=area_and_signs(uv,q);poly=Polygon(uv[top['boundary']])
            okay=checks['nonpositive_triangles']==0 and checks['nonconvex_quads']==0 and poly.is_valid
            history.append({'cap_multiplier':capmult,'alpha':alpha,'result':'pass' if okay else 'uv-sign-rejected'})
            if okay:
                if abs(checks['uv_area']-poly.area)>max(1e-10,poly.area*1e-9):continue
                return uv,{'route':'capsule-boundary-mean-value','reference_width':W,'length':L,
                    'endpoint_mode':'explicit' if endpoints is not None else 'geodesic-boundary-heuristic',
                    'endpoints_control_indices':ends,'rectangular_body':True,'attached_end_count':2,
                    'cap_mode':'rounded-UV-only','cap_arc_lengths':[capA,capB],'relax_alpha':alpha,
                    'attempts':len(history),'attempt_history':history},top
    raise StopUV('UV_FOLDOVER','All bounded cap/rail candidates failed the convex-quad or orientation test. No finished OBJ is produced; do not disable QA.')


def validate_island(uv,q,boundary):
    if not np.isfinite(uv).all():raise StopUV('NONFINITE_UV','Missing or nonfinite UV.')
    checks=area_and_signs(uv,q);poly=Polygon(uv[boundary]);gap=abs(poly.area-checks['uv_area'])
    checks.update({'boundary_simple':bool(poly.exterior.is_simple),'boundary_valid':bool(poly.is_valid),
                   'boundary_area':float(poly.area),'surface_boundary_area_gap':gap})
    if checks['nonpositive_triangles'] or checks['nonconvex_quads'] or not poly.is_valid or gap>max(1e-10,poly.area*1e-9):
        raise StopUV('UV_QA_FAILED',str(checks))
    return checks
