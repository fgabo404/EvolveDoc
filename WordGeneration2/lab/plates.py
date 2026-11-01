"""Laboratorio WordGeneration2: port del generador tectonic-plates-2 de Evolve.
Solo biblioteca estándar. Grid flat-top odd-q, periódico en X, abierto en Y.
La comparación bit a bit con C# sigue pendiente de una prueba cruzada.
"""
from __future__ import annotations
import argparse
import hashlib
import heapq
import math
import secrets
import struct
from collections import Counter, deque

MASK = (1 << 64) - 1
UINT = (1 << 32) - 1
COSTS = [.58,.64,.72,.79,.88,.97,1.05,1.14,1.24,1.35,1.48,1.62,1.79,1.97,2.17,2.40]
STREAM = 0x54454331
MIN_PLATES = 10
MAX_PLATES = 14
MIN_MAIN = 6
MAX_MAIN = 10
BORDER_IRREGULARITY = 1.90

def i32(v):
    v &= UINT
    return v if v < 1 << 31 else v - (1 << 32)

def u32(v): return v & UINT

def f32(v): return struct.unpack("<f", struct.pack("<f", v))[0]

class SplitMix64:
    def __init__(self, seed, stream=STREAM):
        self.state = u32(seed) | (stream << 32)
    def next64(self):
        self.state = (self.state + 0x9E3779B97F4A7C15) & MASK
        z = self.state
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & MASK
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & MASK
        return z ^ (z >> 31)
    def integer(self, maximum): return self.next64() % maximum
    def real(self): return (self.next64() >> 11) / (1 << 53)

def lattice_hash(x,y,seed):
    h = (u32(seed) ^ u32(x * 0x9E3779B9) ^ u32(y * 0x85EBCA6B)) & UINT
    h = u32((h ^ (h >> 16)) * 0x7FEB352D)
    h = u32((h ^ (h >> 15)) * 0x846CA68B)
    h ^= h >> 16
    return 2.0 * h / UINT - 1.0

def lattice(x,y,period,seed):
    ix,iy = math.floor(x),math.floor(y)
    fx,fy = x-ix,y-iy
    fx,fy = fx*fx*(3-2*fx),fy*fy*(3-2*fy)
    a=lattice_hash(ix%period,iy,seed)
    b=lattice_hash((ix+1)%period,iy,seed)
    c=lattice_hash(ix%period,iy+1,seed)
    d=lattice_hash((ix+1)%period,iy+1,seed)
    return (a+(b-a)*fx)*(1-fy)+(c+(d-c)*fx)*fy

def noise(x,y,columns,rows,frequency,seed):
    value,amp,total=0.,1.,0.
    for octave in range(3):
        periods=frequency<<octave
        value+=amp*lattice(x*periods/columns,y*periods/rows,periods,i32(seed+octave*7919))
        total+=amp
        amp*=.5
    return value/total

class HexTopology:
    DIRECTIONS=((1,0),(1,-1),(0,-1),(-1,0),(-1,1),(0,1))
    def __init__(self,columns,rows):
        if columns <= 0 or columns%2 or rows <= 0:
            raise ValueError("Se requieren columnas pares y filas positivas")
        self.columns,self.rows=columns,rows
        self.count=columns*rows
        self._neighbors=[self._build_neighbors(i) for i in range(self.count)]
    def axial(self,idx):
        x,y=idx%self.columns,idx//self.columns
        return x,y-(x//2)
    def distance(self,a,b):
        aq,ar=self.axial(a);bq,br=self.axial(b)
        def dist(q,r): return max(abs(aq-q),abs(ar-r),abs(aq+ar-q-r))
        n=self.columns
        return min(dist(bq,br),dist(bq+n,br-n//2),dist(bq-n,br+n//2))
    def _build_neighbors(self,idx):
        q,r=self.axial(idx)
        out=[]
        for dq,dr in self.DIRECTIONS:
            nq,nr=q+dq,r+dr
            wrapped=nq%self.columns
            nr+=(nq-wrapped)//self.columns*(self.columns//2)
            y=nr+wrapped//2
            if 0<=y<self.rows:
                out.append(y*self.columns+wrapped)
        return out
    def neighbors(self,idx): return self._neighbors[idx]

def generate(columns=400, rows=267, seed=2026):
    topology=HexTopology(columns,rows)
    count=topology.count
    rng=SplitMix64(seed)
    number_of_plates=MIN_PLATES+rng.integer(MAX_PLATES-MIN_PLATES+1)
    number_main=MIN_MAIN+rng.integer(min(MAX_MAIN,number_of_plates-1)-MIN_MAIN+1)
    if count<number_of_plates: raise ValueError("La malla tiene menos celdas que placas")
    origins=[rng.integer(count)]
    for plate in range(1,number_of_plates):
        best,best_dist=-1,-1
        for _ in range(160):
            candidate=rng.integer(count)
            separation=min(topology.distance(candidate,other) for other in origins)
            if separation>best_dist or (separation==best_dist and candidate<best):
                best,best_dist=candidate,separation
        origins.append(best)
    # Las principales reciben menores costes y las secundarias mayores.
    # Identidades aleatorias para no vincular categoria al ID.
    costs=[.50+i*.55/max(1,number_main-1) for i in range(number_main)] + [1.65+i*1.05/max(1,number_of_plates-number_main-1) for i in range(number_of_plates-number_main)]
    for i in range(len(costs)-1,0,-1):
        swap=rng.integer(i+1)
        costs[i],costs[swap]=costs[swap],costs[i]
    fields=[[0.0]*count for _ in range(6)]
    specs=((3,0x7B3741),(5,0x31CC2F),(9,0x47DA1E),
           (13,0x178CAB),(21,0x70A145),(29,0x2E91F4))
    for cell in range(count):
        x,y=cell%columns,cell//columns
        warp_x=noise(x,y,columns,rows,3,i32(seed^0x231A45))*columns*.055
        warp_y=noise(x,y,columns,rows,3,i32(seed^0x5E12AB))*rows*.055
        wx,wy=x+warp_x,y+warp_y
        for band,(frequency,salt) in enumerate(specs):
            fields[band][cell]=f32(noise(wx,wy,columns,rows,frequency,i32(seed^salt)))
    profiles=[]
    for plate in range(number_of_plates):
        a,b,c=(rng.real()*2*math.pi for _ in range(3))
        profiles.append((costs[plate],math.cos(a),math.sin(a),
                         math.cos(b),math.sin(b),math.cos(c),math.sin(c)))
    owner=bytearray([255])*count
    # heapq usa contador estable para empates; el heap interno de .NET
    # puede resolver empates en otro orden. Validar contra referencia C#.
    frontier=[]
    serial=0
    for plate,origin in enumerate(origins):
        heapq.heappush(frontier,(0.,serial,origin,plate));serial+=1
    while frontier:
        priority,_,cell,plate=heapq.heappop(frontier)
        if owner[cell]!=255: continue
        owner[cell]=plate
        cost,bx,by,mx,my,fx,fy=profiles[plate]
        for neighbor in topology.neighbors(cell):
            if owner[neighbor]!=255: continue
            broad=1.65*(bx*fields[0][neighbor]+by*fields[1][neighbor])
            medium=1.10*(mx*fields[2][neighbor]+my*fields[3][neighbor])
            fine=.44*(fx*fields[4][neighbor]+fy*fields[5][neighbor])
            resistance=max(.27,min(3.10,1-BORDER_IRREGULARITY*(broad+medium+fine)))
            heapq.heappush(frontier,(priority+cost*resistance,serial,neighbor,plate))
            serial+=1
    if 255 in owner: raise AssertionError("Celdas sin placa")
    counts=Counter(owner)
    main_ids=set(sorted(range(number_of_plates),key=lambda p:(-counts[p],p))[:number_main])
    kinds=["principal" if p in main_ids else "secundaria" for p in range(number_of_plates)]
    return topology,owner,origins,kinds

def validate(topo,owner):
    counts=Counter(owner)
    assert sorted(counts)==list(range(len(counts)))
    assert sum(counts.values())==topo.count
    for plate in range(len(counts)):
        start=owner.index(plate)
        seen={start}
        queue=deque([start])
        while queue:
            for n in topo.neighbors(queue.popleft()):
                if owner[n]==plate and n not in seen:
                    seen.add(n);queue.append(n)
        assert len(seen)==counts[plate],f"Placa desconectada: {plate}"
    return counts

def render(topo,owner,path,kinds=None):
    """Renderizar hexágonos flat-top reales, no una matriz de píxeles cuadrados."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.collections import PolyCollection
    except ImportError as exc:
        raise SystemExit("Para generar PNG: pip install matplotlib") from exc
    palette=plt.get_cmap("tab20").colors[:len(set(owner))]
    root3=math.sqrt(3)
    # Flat-top odd-q: centros x=1+1.5*c, y=sqrt(3)*(r+.5*(c&1)+.5).
    # Vértices apuntan al este y oeste; radio circunscrito 1.
    offsets=[(math.cos(i*math.pi/3),math.sin(i*math.pi/3)) for i in range(6)]
    vertices=[]
    colors=[]
    for r in range(topo.rows):
        for c in range(topo.columns):
            cx=1+1.5*c
            cy=root3*(r+.5*(c&1)+.5)
            vertices.append([(cx+dx,cy+dy) for dx,dy in offsets])
            colors.append(palette[owner[r*topo.columns+c]])
    # Proyección visual 3:2 de la malla 400x267. La topología no cambia.
    # Los hexágonos se escalan ligeramente en X para llenar 3:2.
    physical_width=1.5*topo.columns+.5
    physical_height=root3*(topo.rows+.5)
    x_scale=1.5*physical_height/physical_width
    projected=[[(x*x_scale,y) for x,y in polygon] for polygon in vertices]
    fig,ax=plt.subplots(figsize=(15,10))
    ax.add_collection(PolyCollection(projected,facecolors=colors,
                      edgecolors="none",linewidths=0))
    ax.set_xlim(0,physical_width*x_scale)
    ax.set_ylim(physical_height,0)
    ax.set_aspect("equal")
    ax.set_axis_off()
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    fig.savefig(path,dpi=140,pad_inches=0);plt.close(fig)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--seed",type=int,default=None,help="Semilla fija opcional; omitida = aleatoria")
    ap.add_argument("--columns",type=int,default=400)
    ap.add_argument("--rows",type=int,default=267)
    ap.add_argument("--png",default=None)
    args=ap.parse_args()
    seed=args.seed if args.seed is not None else secrets.randbelow(1 << 32) - (1 << 31)
    topo,owner,origins,kinds=generate(args.columns,args.rows,seed)
    counts=validate(topo,owner)
    digest=hashlib.sha256(owner).hexdigest()
    print("Versión base: tectonic-plates-2")
    print(f"Seed={seed} celdas={topo.count} placas={len(kinds)} principales={kinds.count('principal')} secundarias={kinds.count('secundaria')}")
    print("Categorias:", {p:kind for p,kind in enumerate(kinds)})
    print(f"SHA256 Python (no validado contra C#): {digest}")
    print("Áreas:",dict(sorted(counts.items())))
    print("Orígenes:",origins)
    if args.png:
        render(topo,owner,args.png,kinds)
        print("Imagen:",args.png)

if __name__=="__main__": main()
