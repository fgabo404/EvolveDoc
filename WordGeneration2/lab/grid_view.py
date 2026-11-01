"""Render hexagonal 3:2 con relieve terrestre y mar azul provisional.
El océano es un percentil del campo de alturas, no corteza oceánica simulada.
Requiere Pillow y NumPy.
"""
import math
import numpy as np
from PIL import Image, ImageDraw

def render_grid(topo, relief, path, ocean_percent=60, width=2400):
    z=np.asarray(relief.elevation,dtype=float)
    sea=float(np.percentile(z,ocean_percent))
    high=float(np.percentile(z,99.7))
    low=float(np.percentile(z,.3))
    height=round(width*2/3)
    image=Image.new("RGB",(width,height),(14,63,142))
    draw=ImageDraw.Draw(image)
    root3=math.sqrt(3)
    pw=1.5*topo.columns+.5
    ph=root3*(topo.rows+.5)
    xs=1.5*ph/pw
    px=width/(pw*xs)
    py=height/ph
    offsets=[(math.cos(i*math.pi/3),math.sin(i*math.pi/3)) for i in range(6)]
    for r in range(topo.rows):
        for c in range(topo.columns):
            idx=r*topo.columns+c
            cx=(1+1.5*c)*xs*px
            cy=root3*(r+.5*(c&1)+.5)*py
            polygon=[(cx+dx*xs*px,cy+dy*py) for dx,dy in offsets]
            v=z[idx]
            if v<sea:
                depth=(v-low)/max(1e-6,sea-low)
                fill=(14,63,142) if depth<.25 else (23,91,177) if depth<.65 else (40,133,199)
            else:
                t=(v-sea)/max(1e-6,high-sea)
                fill=((217,205,142) if t<.06 else (105,159,85) if t<.25
                      else (151,174,90) if t<.43 else (184,151,106) if t<.61
                      else (133,105,91) if t<.78 else (241,237,226))
            outline=tuple(int(k*.82) for k in fill)
            draw.polygon(polygon,fill=fill,outline=outline,width=1)
    image.save(path,optimize=True)
    return {"sea_threshold":sea,"ocean_percent":float((z<sea).mean()*100)}
