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
    number_main=MIN_MAIN+rng.integer(min(MAX_MAIN,number_of_plates-3)-MIN_MAIN+1)
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
    # Áreas objetivo compatibles con la cantidad de placas en cada categoría.
    number_secondary=number_of_plates-number_main
    secondary_low=max(.14,.02*number_secondary,1-.18*number_main)
    secondary_high=min(.22,.06*number_secondary,1-.08*number_main)
    if secondary_low>secondary_high: raise ValueError("Distribución de áreas incompatible")
    secondary_total=(secondary_low+secondary_high)/2
    def quotas(n,total,minimum,maximum):
        weights=[.85+.30*rng.real() for _ in range(n)]
        values=[minimum]*n
        remaining=total-n*minimum
        for _ in range(40):
            if remaining<1e-12: break
            available=[max(0.,maximum-v) for v in values]
            eligible=[weights[i] if available[i]>1e-12 else 0. for i in range(n)]
            total_weight=sum(eligible)
            if not total_weight: break
            changes=[min(available[i],remaining*eligible[i]/total_weight) for i in range(n)]
            for i in range(n): values[i]+=changes[i]
            remaining-=sum(changes)
        if abs(sum(values)-total)>1e-8: raise ValueError("Cuotas incompatibles")
        return values
    main_quotas=quotas(number_main,1-secondary_total,.08,.18)
    secondary_quotas=quotas(number_secondary,secondary_total,.02,.06)
    pairs=[(v,"principal") for v in main_quotas]+[(v,"secundaria") for v in secondary_quotas]
    for i in range(len(pairs)-1,0,-1):
        swap=rng.integer(i+1)
        pairs[i],pairs[swap]=pairs[swap],pairs[i]
    kinds=[kind for _,kind in pairs]
    targets=[round(share*count) for share,_ in pairs]
    targets[0]+=count-sum(targets)
    costs=[.85+.3*rng.real() for _ in range(number_of_plates)]
    return topology,owner,origins,kinds

