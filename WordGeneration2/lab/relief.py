"""Capa 02 experimental: relieve tectónico a partir de placas existentes.
Requiere plates.py. No simula evolución temporal ni distingue corteza continental/oceánica.
"""
from collections import deque
from dataclasses import dataclass
import math
from plates import SplitMix64, noise, i32

@dataclass
class Relief:
    elevation: list
    convergence: list
    divergence: list
    shear: list
    mountains: list
    rifts: list
    trench_candidates: list
    volcano_candidates: list

def generate_relief(topo, owner, seed, radius=7):
    n=topo.count
    w,h=topo.columns,topo.rows
    rng=SplitMix64(seed,0x4D4F5431)
    motion=[]
    for _ in range(max(owner)+1):
        angle=2*math.pi*rng.real()
        speed=1+7*rng.real()
        motion.append((speed*math.cos(angle),speed*math.sin(angle)))
    sources=[{} for _ in range(3)]
    for a in range(n):
        ac,ar=a%w,a//w
        for b in topo.neighbors(a):
            if b<=a or owner[a]==owner[b]: continue
            bc,br=b%w,b//w
            dx=bc-ac
            if dx>w//2: dx-=w
            if dx< -w//2: dx+=w
            x=1.5*dx
            y=math.sqrt(3)*(br-ar+.5*((bc&1)-(ac&1)))
            length=math.hypot(x,y)
            if not length: continue
            nx,ny=x/length,y/length
            va,vb=motion[owner[a]],motion[owner[b]]
            vx,vy=vb[0]-va[0],vb[1]-va[1]
            normal=vx*nx+vy*ny
            components=(max(0,-normal),max(0,normal),abs(-vx*ny+vy*nx))
            for channel,amount in enumerate(components):
                if amount<=0: continue
                for cell in (a,b):
                    sources[channel][cell]=max(amount,sources[channel].get(cell,0))
    def diffuse(source):
        out=[0.]*n
        weights=[math.exp(-(d/radius)**2) for d in range(radius*2+1)]
        for start,amount in source.items():
            queue=deque([(start,0)])
            visited={start}
            while queue:
                cell,d=queue.popleft()
                out[cell]=max(out[cell],amount*weights[d])
                if d>=radius*2: continue
                for neighbor in topo.neighbors(cell):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor,d+1))
        return out
    convergence,divergence,shear=(diffuse(s) for s in sources)
    elevation=[]; mountains=[]; rifts=[]; trenches=[]; volcanoes=[]
    for cell in range(n):
        x,y=cell%w,cell//w
        c,d,s=convergence[cell],divergence[cell],shear[cell]
        broad=noise(x,y,w,h,3,i32(seed^0xAE144))
        fine=noise(x,y,w,h,17,i32(seed^0x814C9))
        elevation.append(.20*broad+.07*fine+.13*c-.09*d+.018*s)
        mountains.append(c>2.2 and c>=1.3*d)
        rifts.append(d>2.2 and d>=1.25*c)
        trenches.append(c>3.5)
        if (c>3.8 or d>4.5) and s<=1.6*max(c,d):
            if cell%37==0 and noise(x,y,w,h,29,i32(seed^0xB01CA))>.34:
                volcanoes.append(cell)
    return Relief(elevation,convergence,divergence,shear,mountains,rifts,trenches,volcanoes)

def render_relief(topo, relief, output):
    """Diagnóstico 3:2; la malla subyacente sigue siendo hexagonal."""
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.colors import TwoSlopeNorm
    w,h=topo.columns,topo.rows
    arr=np.asarray(relief.elevation).reshape(h,w)
    lo,hi=np.percentile(arr,[3,97])
    mid=max(lo,min(0.,hi))
    if not lo<mid<hi: lo,mid,hi=float(arr.min())-.001,float(np.median(arr)),float(arr.max())+.001
    fig,ax=plt.subplots(figsize=(15,10))
    ax.imshow(arr,cmap="terrain",norm=TwoSlopeNorm(vmin=lo,vcenter=mid,vmax=hi),
              aspect="auto",interpolation="nearest",extent=(0,w,h,0))
    ax.contour(np.asarray(relief.mountains).reshape(h,w).astype(float),
               levels=[.5],colors=["#f5f3ee"],linewidths=.45,extent=(0,w,h,0))
    ax.contour(np.asarray(relief.rifts).reshape(h,w).astype(float),
               levels=[.5],colors=["#49358c"],linewidths=.45,extent=(0,w,h,0))
    if relief.volcano_candidates:
        import numpy as np
        ids=np.asarray(relief.volcano_candidates)
        ax.scatter(ids%w+.5,ids//w+.5,c="#c62b24",marker="^",s=7)
    ax.set(xlim=(0,w),ylim=(h,0))
    ax.axis("off")
    fig.subplots_adjust(0,0,1,1)
    fig.savefig(output,dpi=120)
    plt.close(fig)

if __name__=="__main__":
    import argparse, secrets
    from plates import generate, validate
    p=argparse.ArgumentParser()
    p.add_argument("--seed",type=int)
    p.add_argument("--png",default="relieve.png")
    args=p.parse_args()
    seed=args.seed if args.seed is not None else secrets.randbelow(1<<32)-(1<<31)
    topo,owner,_,kinds=generate(seed=seed)
    validate(topo,owner)
    relief=generate_relief(topo,owner,seed)
    render_relief(topo,relief,args.png)
    print(f"Seed={seed}; placas={len(kinds)}; cordillera_celdas={sum(relief.mountains)}; rift_celdas={sum(relief.rifts)}; volcanes_candidatos={len(relief.volcano_candidates)}")
