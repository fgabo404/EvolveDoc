"""G-Evolve | world generationfractal. Prototipo independiente inspirado en Civ VI."""
import argparse
from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
from matplotlib.collections import PatchCollection

@dataclass
class Config:
    width:int=70
    height:int=44
    seed:int=1001
    world:str="continents"
    sea_level:float=.61
    world_age:str="normal"
    rainfall:str="normal"
    temperature:str="normal"

WORLDS=("continents","pangaea","archipelago","fractal")

def smooth_noise(rng,h,w,scale):
    ny=max(2,int(np.ceil(h/scale))+1)
    nx=max(2,int(np.ceil(w/scale)))
    nodes=rng.random((ny,nx))
    nodes=np.concatenate([nodes,nodes[:,0:1]],axis=1)
    yy=np.arange(h)/scale;xx=np.arange(w)/scale
    yi=np.minimum(np.floor(yy).astype(int),ny-2)
    xi=np.floor(xx).astype(int)%nx
    ty=yy-np.floor(yy);tx=xx-np.floor(xx)
    ty=ty*ty*(3-2*ty);tx=tx*tx*(3-2*tx)
    a=nodes[yi[:,None],xi[None,:]]
    b=nodes[yi[:,None],xi[None,:]+1]
    c=nodes[yi[:,None]+1,xi[None,:]]
    d=nodes[yi[:,None]+1,xi[None,:]+1]
    return ((1-ty[:,None])*((1-tx)[None,:]*a+tx[None,:]*b)
            +ty[:,None]*((1-tx)[None,:]*c+tx[None,:]*d))

def fbm(rng,h,w,scales=(36,18,9,4,2),persistence=.52):
    acc=np.zeros((h,w));weight=0
    for i,scale in enumerate(scales):
        amp=persistence**i
        acc+=amp*smooth_noise(rng,h,w,scale)
        weight+=amp
    return acc/weight

def world_mask(cfg,rng):
    h,w=cfg.height,cfg.width
    ys,xs=np.mgrid[:h,:w];x=xs/w;y=ys/h
    noise=fbm(rng,h,w,(max(8,w//2),max(5,w//4),max(3,w//8),4,2))
    if cfg.world=="continents":
        anchor=(np.exp(-((x-.26)/.21)**2-((y-.47)/.40)**2)
                +.93*np.exp(-((x-.75)/.20)**2-((y-.51)/.39)**2))
        value=.57*noise+.43*(anchor/1.1)
    elif cfg.world=="pangaea":
        anchor=np.exp(-((x-.49)/.36)**2-((y-.5)/.40)**2)
        value=.42*noise+.58*anchor
    elif cfg.world=="archipelago":
        phase=3.5*x+.6*np.sin(y*11)
        ridges=np.exp(-((y-(.50+.22*np.sin(phase*3)))/.10)**2)
        ridges+=.65*np.exp(-((y-(.50+.20*np.cos(phase*4+1)))/.075)**2)
        value=.74*noise+.26*np.minimum(1,ridges)
    else:
        value=noise
    value-=.10*np.maximum(0,(np.abs(y-.5)-.38)/.12)
    target={"continents":.40,"pangaea":.44,"archipelago":.23,"fractal":.38}[cfg.world]
    target=np.clip(target+(.61-cfg.sea_level)*.9,.10,.70)
    return value,value>=np.quantile(value,1-target)

def generate(cfg):
    if cfg.width<12 or cfg.height<10:
        raise ValueError("Tamaño mínimo: 12x10")
    if cfg.world not in WORLDS:raise ValueError("Mundo inválido")
    rng=np.random.default_rng(cfg.seed)
    h,w=cfg.height,cfg.width
    elevation,land=world_mask(cfg,rng)
    relief=fbm(rng,h,w,(20,9,4,2))
    peak={"young":.79,"normal":.86,"old":.91}[cfg.world_age]
    hills=(relief>.66)&land
    mountains=(relief>peak)&land
    lat=np.abs((np.arange(h)[:,None]+.5)/h-.5)*2
    thermal=(1-lat)+.13*(fbm(rng,h,w,(25,10,3))-.5)
    thermal=thermal+{"cold":-.12,"normal":0,"hot":.12}[cfg.temperature]
    wet=fbm(rng,h,w,(24,11,5,2))
    wet=wet+{"arid":-.12,"normal":0,"wet":.12}[cfg.rainfall]
    shore=np.zeros((h,w),dtype=bool)
    for dy,dx in ((-1,0),(1,0),(0,-1),(0,1)):
        shore|=land&(~np.roll(land,(dy,dx),axis=(0,1)))
    wet=np.clip(wet+.12*shore,0,1)
    biome=np.full((h,w),"ocean",dtype=object)
    biome[land]="plains"
    biome[land&(thermal<.16)]="snow"
    biome[land&(thermal>=.16)&(thermal<.30)]="tundra"
    biome[land&(thermal>=.30)&(wet<.34)]="desert"
    biome[land&(thermal>=.30)&(wet>=.34)&(wet<.46)]="grassland"
    biome[land&(thermal>=.45)&(wet>.70)]="rainforest"
    biome[land&(thermal>=.30)&(wet>.55)&(wet<=.70)]="forest"
    biome[hills]="hills"
    biome[mountains]="mountain"
    return dict(biome=biome,land=land,elevation=elevation,
                rainfall=wet,temperature=thermal,mountains=mountains)

COLORS={"ocean":"#2365a2","grassland":"#a1bb64","plains":"#d6c484",
"desert":"#e2cf8d","forest":"#427c3d","rainforest":"#246d50",
"tundra":"#bbc1a7","snow":"#f0f5f0","hills":"#87915c","mountain":"#737681"}

def render(world,cfg,output=None,show=False):
    fig,ax=plt.subplots(figsize=(15,9),facecolor="#0b1722")
    patches=[];colors=[]
    for row in range(cfg.height):
        for col in range(cfg.width):
            px=col*1.03+(row%2)*.515
            py=row*.89
            patches.append(RegularPolygon((px,py),6,radius=.59,orientation=0))
            colors.append(COLORS[world["biome"][row,col]])
    collection=PatchCollection(patches,facecolor=colors,
                               edgecolor="#253542",linewidth=.27)
    ax.add_collection(collection)
    ax.set_aspect("equal");ax.autoscale_view();ax.invert_yaxis();ax.axis("off")
    ax.set_title(f"G-Evolve | {cfg.world} | semilla {cfg.seed} | {cfg.width}x{cfg.height}",
                 color="white",fontsize=15,pad=15)
    fig.tight_layout()
    if output:fig.savefig(output,dpi=170,facecolor=fig.get_facecolor(),bbox_inches="tight")
    if show:plt.show()
    plt.close(fig)

def main():
    p=argparse.ArgumentParser(description="Generador fractal hexagonal de G-Evolve")
    p.add_argument("--seed",type=int,default=1001)
    p.add_argument("--width",type=int,default=70)
    p.add_argument("--height",type=int,default=44)
    p.add_argument("--world",choices=WORLDS,default="continents")
    p.add_argument("--sea-level",type=float,default=.61)
    p.add_argument("--world-age",choices=["young","normal","old"],default="normal")
    p.add_argument("--temperature",choices=["cold","normal","hot"],default="normal")
    p.add_argument("--rainfall",choices=["arid","normal","wet"],default="normal")
    p.add_argument("--output",default="world_fractal.png")
    p.add_argument("--show",action="store_true")
    a=p.parse_args()
    cfg=Config(a.width,a.height,a.seed,a.world,a.sea_level,
               a.world_age,a.rainfall,a.temperature)
    result=generate(cfg)
    render(result,cfg,a.output,a.show)
    print(f"Generado: {a.output} | tierra: {result['land'].mean()*100:.1f}% | semilla {a.seed}")

if __name__=="__main__":
    main()
