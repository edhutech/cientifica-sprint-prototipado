"""Prepare traceable presenter derivatives and original educational diagrams."""
from pathlib import Path
import hashlib
import re
from PIL import Image, ImageChops

ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'assets/content/presenter'
D=P/'derived'
D.mkdir(exist_ok=True)
records=[]
for source,name in [('HUB-UDEP_logo.svg','hub-udep-dark.svg'),('LOGOTIPO-NEXUM.svg','nexum-dark.svg')]:
    data=(P/'logos'/source).read_text()
    changed,count=re.subn(r'(?i)(fill|stroke)="(?:white|#fff|#ffffff)"',lambda m:f'{m[1]}="#00358E"',data)
    assert count>0,source
    (D/name).write_text(changed)
    records.append((source,name,f'{count} atributos de blanco a #00358E; geometría y viewBox intactos.'))
source='logo-horizontal-blanco-web.fw-455x128.png'
im=Image.open(P/'logos'/source).convert('RGBA')
pixels=[(0,53,142,a) if r>220 and g>220 and b>220 else (r,g,b,a) for r,g,b,a in im.get_flattened_data()]
im.putdata(pixels)
bbox=im.getchannel('A').getbbox()
im.crop((max(0,bbox[0]-4),max(0,bbox[1]-4),min(im.width,bbox[2]+4),min(im.height,bbox[3]+4))).save(D/'senati-dark.png')
records.append((source,'senati-dark.png','Píxeles blancos a #00358E, alfa conservado; recorte de margen transparente con 4 px de respiro.'))
im=Image.open(P/'logos/basf-new.png').convert('RGB')
mask=ImageChops.difference(im,Image.new('RGB',im.size,'white')).convert('L').point(lambda p:255 if p>15 else 0)
b=mask.getbbox(); b=(max(0,b[0]-8),max(0,b[1]-8),min(im.width,b[2]+8),min(im.height,b[3]+8))
im.crop(b).save(D/'basf-trimmed.png')
records.append(('basf-new.png','basf-trimmed.png',f'Recorte exclusivo de margen blanco exterior, caja {b}; conserva logo, colores y leyenda.'))
manifest='# Derivados usados en «Sobre mí»\n\nAdaptaciones autorizadas previamente por el usuario para fondo blanco y encuadre. Los originales no cambian. No son nuevas versiones oficiales de las marcas.\n\n| Original en `../logos/` | Derivado | Operación |\n| --- | --- | --- |\n'
for source,name,op in records:manifest+=f'| `{source}` | `{name}` | {op} |\n'
manifest+='\nSe usan sin alterar Startup Perú, ProInnóvate, la insignia completa Microsoft for Startups, Fundación Romero (WebP en color), Nutri H y la fotografía. Foto mostrada a 400 × 400 px Full HD, sin ampliación ni recorte necesario. Wichay no está disponible y se omite conforme a la decisión previa. No se incluyen CIDE ni logos de empleadores adicionales. La insignia Microsoft conserva «Proud to partner with»; comprobar que corresponde al contexto del presentador antes de exponer.\n\nTodos son archivos proporcionados por el usuario; URLs de origen no aportadas. Las adaptaciones de color siguen la autorización específica del manifiesto del presentador; no se aplican a la identidad de Científica Sprint.\n'
(D/'manifest.md').write_text(manifest)
I=ROOT/'assets/content/illustrations';I.mkdir(parents=True,exist_ok=True)
art={
'paper':'<path d="M105 20h235v240H105z" fill="#fff" stroke="#00358e" stroke-width="5"/><path d="M135 60h130m-130 35h165m-165 25h125" stroke="#00358e" stroke-width="7"/><rect x="135" y="160" width="165" height="52" fill="none" stroke="#00358e" stroke-width="4"/><path d="m295 220 70-130 16 9-70 130-23 22z" fill="#f68d20"/>',
'digital':'<rect x="60" y="30" width="330" height="220" rx="8" fill="#fff" stroke="#00358e" stroke-width="5"/><path d="M60 70h330" stroke="#00358e" stroke-width="4"/><circle cx="82" cy="50" r="5" fill="#00358e"/><circle cx="102" cy="50" r="5" fill="#00358e"/><path d="M95 105h135m-135 25h100" stroke="#00358e" stroke-width="7"/><rect x="95" y="164" width="125" height="45" rx="3" fill="#00358e"/><path d="m268 140 55 45-26 4-14 31z" fill="#f68d20"/>',
'physical':'<path d="m95 95 130-65 130 65v125l-130 45-130-45z" fill="#fff" stroke="#00358e" stroke-width="5"/><path d="m95 95 130 55 130-55m-130 55v115" fill="none" stroke="#00358e" stroke-width="5"/><path d="m160 63 128 56v45l-40 14v-45L125 80z" fill="#f68d20"/><path d="m122 160 65 24m-65-2 45 17" stroke="#00358e" stroke-width="5"/>',
'visual':'<rect x="90" y="40" width="270" height="200" fill="none" stroke="#00358e" stroke-width="6"/><circle cx="155" cy="105" r="25" fill="#f68d20"/><path d="m110 214 90-90 70 60 45-45 25 75" fill="none" stroke="#00358e" stroke-width="6"/>',
'interactive':'<rect x="90" y="55" width="250" height="155" rx="8" fill="none" stroke="#00358e" stroke-width="6"/><path d="m225 125 70 55-35 10-15 35z" fill="#f68d20"/><path d="M130 100h130" stroke="#00358e" stroke-width="10"/>',
'simulated':'<path d="M70 140h85m-25-22 25 22-25 22m170-22h85m-25-22 25 22-25 22" fill="none" stroke="#00358e" stroke-width="6"/><rect x="175" y="75" width="100" height="130" rx="8" fill="none" stroke="#00358e" stroke-width="6" stroke-dasharray="12 8"/><path d="m200 140 18 20 34-44" fill="none" stroke="#f68d20" stroke-width="8"/>'}
for name,drawing in art.items():
    (I/f'{name}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 280">{drawing}</svg>')
(I/'README.md').write_text('# Ilustraciones educativas\n\nSVG originales creados para este taller: boceto, interfaz, maqueta física y símbolos visual/interactivo/simulado. Son representaciones esquemáticas, no fotografías ni evidencia de productos reales. Colores tomados de la identidad institucional; sin marcas ajenas. Reproducir con `python tmp/prepare-deck-assets.py`.\n')
print('4 presenter derivatives; 6 original educational illustrations')
