"""UV evidence renders of the actual geometry; not generative images."""
from __future__ import annotations
import numpy as np
from numba import njit
from PIL import Image,ImageDraw,ImageFont

def font(size):
    for name in ['DejaVuSans.ttf','Arial.ttf']:
        try:return ImageFont.truetype(name,size)
        except OSError:pass
    return ImageFont.load_default(size=size)

@njit(cache=True)
def raster(P,T,N,UV,zbuf,img):
    h,w=zbuf.shape
    for fi in range(len(T)):
        a,b,c=T[fi];A=P[a];B=P[b];C=P[c]
        den=(B[1]-C[1])*(A[0]-C[0])+(C[0]-B[0])*(A[1]-C[1])
        if abs(den)<1e-12:continue
        xmin=max(0,int(np.floor(min(A[0],B[0],C[0]))));xmax=min(w-1,int(np.ceil(max(A[0],B[0],C[0]))))
        ymin=max(0,int(np.floor(min(A[1],B[1],C[1]))));ymax=min(h-1,int(np.ceil(max(A[1],B[1],C[1]))))
        for y in range(ymin,ymax+1):
            for x in range(xmin,xmax+1):
                xx=x+.5;yy=y+.5
                aa=((B[1]-C[1])*(xx-C[0])+(C[0]-B[0])*(yy-C[1]))/den
                bb=((C[1]-A[1])*(xx-C[0])+(A[0]-C[0])*(yy-C[1]))/den
                cc=1-aa-bb
                if aa< -1e-8 or bb< -1e-8 or cc< -1e-8:continue
                z=aa*A[2]+bb*B[2]+cc*C[2]
                if z<=zbuf[y,x]:continue
                zbuf[y,x]=z
                nx=aa*N[a,0]+bb*N[b,0]+cc*N[c,0];ny=aa*N[a,1]+bb*N[b,1]+cc*N[c,1];nz=aa*N[a,2]+bb*N[b,2]+cc*N[c,2]
                norm=max(1e-14,(nx*nx+ny*ny+nz*nz)**.5);nx/=norm;ny/=norm;nz/=norm
                if nz<0:nx=-nx;ny=-ny;nz=-nz
                shade=.38+.62*max(0.,-.3*nx+.4*ny+.866*nz)
                u=aa*UV[a,0]+bb*UV[b,0]+cc*UV[c,0];v=aa*UV[a,1]+bb*UV[b,1]+cc*UV[c,1]
                if (int(np.floor(u*8))+int(np.floor(v*8)))%2:r,g,b0=58.,79.,92.
                else:r,g,b0=222.,228.,232.
                img[y,x,0]=min(255.,r*shade);img[y,x,1]=min(255.,g*shade);img[y,x,2]=min(255.,b0*shade)
    return img

def render(v,q,uv,out,direction=(1,.7,1.5),size=(1200,900),title='UV CHECK'):
    t=np.r_[q[:,[0,1,2]],q[:,[0,2,3]]];n=np.zeros_like(v)
    for start in range(0,len(t),100_000):
        tt=t[start:start+100_000];fn=np.cross(v[tt[:,1]]-v[tt[:,0]],v[tt[:,2]]-v[tt[:,0]])
        for k in range(3):np.add.at(n,tt[:,k],fn)
    n/=np.maximum(np.linalg.norm(n,axis=1)[:,None],1e-14)
    d=np.asarray(direction,float);d/=np.linalg.norm(d);r=np.cross([0,1,0],d);r/=np.linalg.norm(r);up=np.cross(d,r)
    view=np.array([r,up,d]).T;vp=v@view;ns=n@view
    span=np.maximum(np.ptp(vp[:,:2],axis=0),1e-10);center=(vp[:,:2].max(0)+vp[:,:2].min(0))*.5
    scale=min((size[0]-100)/span[0],(size[1]-130)/span[1]);vp[:,:2]=(vp[:,:2]-center)*scale
    vp[:,0]+=size[0]/2;vp[:,1]=-vp[:,1]+size[1]/2+25
    z=np.full((size[1],size[0]),-np.inf);img=np.full((size[1],size[0],3),247.,dtype=np.float64)
    im=Image.fromarray(np.uint8(np.clip(raster(vp,t,ns,uv,z,img),0,255)))
    ImageDraw.Draw(im).text((22,20),title,fill=(35,39,45),font=font(20));im.save(out)

def layout(job,out):
    info=job.info();uv=job.load('uv_verified.npy');count=len(info['components']);W=1800
    scale=(W-90)/np.ptp(uv[:,0])
    heights=[float(np.ptp(uv[job.load(f'c{c}_boundary.npy'),1]))*scale for c in range(count)]
    rowH=max(100,int(np.ceil(max(heights,default=0)))+70)
    H=180+rowH*count+410*min(count,4)
    im=Image.new('RGB',(W,H),(250,250,248));d=ImageDraw.Draw(im)
    d.text((38,24),'RECTANGULAR STRIP UV | actual coordinates',fill=(24,29,35),font=font(28))
    d.text((38,70),'Uniform scale above; end details enlarged below. No change to the mesh topology.',fill=(65,71,78),font=font(19))
    y=150;shapes=[]
    for comp in info['components']:
        c=comp['component'];loop=job.load(f'c{c}_boundary.npy');uu=uv[loop];lo=uu.min(0);span=np.ptp(uu,axis=0)
        points=(uu-lo)*scale;points[:,0]+=42;points[:,1]=y+heights[c]-points[:,1]
        d.text((42,y-32),f'Strip {c+1}: U span {span[0]:.3f}, V span {span[1]:.3f}',fill=(50,55,61),font=font(17))
        d.polygon([tuple(p) for p in points],fill=(211,224,229));d.line([tuple(p) for p in np.r_[points,points[:1]]],fill=(45,66,76),width=2)
        shapes.append((c,loop,lo,span));y+=rowH
    for c,loop,lo,span in shapes[:4]:
        comp=info['components'][c];gq=job.load(f'c{c}_level{comp["subdivision_levels"]}.npy')
        for end in [0,1]:
            x0=42+end*(W//2);pw=W//2-85;ph=350
            panel=Image.new('RGB',(pw,ph),'white');pd=ImageDraw.Draw(panel)
            show_width=min(span[0],1.65*span[1]);left=lo[0] if end==0 else lo[0]+span[0]-show_width
            sc=min((pw-32)/show_width,(ph-60)/span[1])
            def project(a):
                p=a.copy();p[:,0]=(p[:,0]-left)*sc+16;p[:,1]=(lo[1]+span[1]-p[:,1])*sc+35;return p
            p=project(uv[loop]);pd.polygon([tuple(x) for x in p],fill=(226,234,237))
            centre=uv[gq].mean(1);selected=gq[(centre[:,0]>left-.04*span[1])&(centre[:,0]<left+show_width+.04*span[1])]
            stride=max(1,len(selected)//2500)
            for face in selected[::stride]:
                fp=project(uv[face]);pd.line([tuple(x) for x in np.r_[fp,fp[:1]]],fill=(161,179,186),width=1)
            pd.line([tuple(x) for x in np.r_[p,p[:1]]],fill=(44,65,76),width=2)
            pd.text((12,8),f'Strip {c+1} | '+('start' if end==0 else 'end'),fill=(35,40,48),font=font(18))
            im.paste(panel,(x0,y));d.rectangle((x0,y,x0+pw,y+ph),outline=(194,204,210),width=1)
        y+=410
    d.text((42,H-33),'Control wires shown only for readability. The OBJ keeps every original quad.',fill=(65,71,78),font=font(17))
    im.save(out)
