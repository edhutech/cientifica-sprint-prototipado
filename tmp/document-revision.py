from pathlib import Path
import json
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1]
base=json.loads((root/'deck/content.json').read_text());r=json.loads((root/'deck/revisions.json').read_text())
seq=[]
for s in base:
 k=str(s['number'])
 if k in r['before']:seq.append({**r['before'][k],'notes':'Mostrar la apertura y dar paso a la sección. En las preguntas, invitar a inferir la respuesta observando la ilustración. Tiempo incluido en el bloque existente.'})
 seq.append({**s,**r['updates'].get(k,{})})
text='# Revisión vigente — 22 diapositivas\n\nEsta revisión sustituye las decisiones de la versión inicial únicamente en los puntos solicitados. Las definiciones y demás slides se conservan. Las cuatro aperturas se integran en los tiempos existentes, sin añadir actividades. Fuentes de reconstrucción: `content.json` (base) + `revisions.json` (inserciones/cambios), `deck.css` + `revision.css`, y `../tmp/build-deck.py`.\n\n## Layouts nuevos\n\nCabecera C original intacta. Aperturas: cuerpo azul #00358E, título blanco a la izquierda, ilustración o logo a la derecha. Actividades: cuerpo naranja institucional #F68D20, texto azul oscuro #00275F. Sin modificar brand-spec.md.\n\nPerfil: iconos originales Guayerd, AI PlayGrounds y LetyMind junto a sus respectivos roles. Nube inferior sin cambios. Cierre: Muchas gracias y tres enlaces reales proporcionados por el usuario.\n\n## Orden y contenido vigente\n\n'
notes='# Notas del facilitador — versión vigente (22 diapositivas)\n\nLas aperturas consumen parte del tiempo de sus bloques, sin ampliar los 120 minutos. Navegación sin cambios: →/espacio, ←, R, F, Home/End. Preparar Google Docs y acceso a AI Studio antes de compartir pantalla.\n\n'
for i,s in enumerate(seq,1):
 text+=f'### {i:02} — {s["title"]}\n\nReferencia base: `{s["number"]}`. Tema: {s.get("theme","institucional original")}.\n\n'
 text+='\n'.join('- '+t for t in s.get('text',[]))+'\n\n'
 if s.get('image'):text+='Imagen: `'+s['image']+'`.\n\n'
 note=s.get('notes','')
 if s['number']==18:note='Agradecer y mostrar LinkedIn, correo y web. Los enlaces son interactivos y se abren sin avanzar la presentación.'
 if s['number']==15:note='Actividad individual: cada participante sigue paso a paso al facilitador usando los insumos de su equipo. Mantener la demostración de Tanda y los 38 minutos del bloque original.'
 notes+=f'## {i:02} · {s["title"]}\n\n{note}\n\n'
text+='## Revelaciones\n\nLas antiguas slides 12 y 13 ocupan ahora los lugares 14 y 15. Conservan seis y cinco estados, respectivamente: nueve avances internos totales.\n'
(root/'deck/revision-spec.md').write_text(text)
(root/'deck/presenter-notes.md').write_text(notes)
for file,notice in [('deck/deck-spec.md','> **Versión vigente: 22 diapositivas.** Ver [revision-spec.md](revision-spec.md) y `revisions.json` para el orden y los cambios solicitados. El documento siguiente conserva la especificación base de 18 slides como referencia histórica.\n\n'),('README.md','> **Actualización vigente:** 22 diapositivas, 9 avances internos. Nuevas aperturas azules y actividades naranjas; ver [revisión](deck/revision-spec.md) y [QA actualizado](output/qa-revision.md). Para reconstruir: `python tmp/build-deck.py`; verificar: `node tmp/qa-revision.mjs`. Los scripts QA anteriores corresponden a la versión histórica de 18 slides.\n\n'),('output/qa.md','> **Reporte histórico de la versión de 18 diapositivas.** Para el HTML vigente de 22, consultar [QA de revisión](qa-revision.md).\n\n')]:
 p=root/file
 if not p.read_text().startswith(notice):p.write_text(notice+p.read_text())
canvas=Image.new('RGB',(1920,8*390),'#e5e7eb');draw=ImageDraw.Draw(canvas)
for i in range(22):
 x=i%3*640;y=i//3*390;draw.text((x+10,y+8),str(i+1),fill='black')
 canvas.paste(Image.open(root/f'output/qa/revision/1920x1080/slide-{i+1:02}.png').resize((640,360)),(x,y+30))
canvas.save(root/'output/deck-contact-sheet.png')
print('Revision specification, current notes, report pointers and contact sheet updated')
