"""Build two standalone technical specimens, never the workshop deck."""
import base64
import hashlib
import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TMP = ROOT / 'tmp'
FONTS = TMP / 'brand-proof-fonts'
FONTS.mkdir(exist_ok=True)
URLS = {
    'Montserrat-Regular.ttf': 'https://fonts.gstatic.com/s/montserrat/v31/JTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCtr6Ew-.ttf',
    'Montserrat-Bold.ttf': 'https://fonts.gstatic.com/s/montserrat/v31/JTUHjIg1_i6t8kCHKm4532VJOt5-QNFgpCuM70w-.ttf',
    'OFL.txt': 'https://raw.githubusercontent.com/google/fonts/main/ofl/montserrat/OFL.txt',
}
manifest = []
for name, url in URLS.items():
    path = FONTS / name
    if not path.exists():
        with urllib.request.urlopen(url, timeout=45) as response:
            path.write_bytes(response.read())
    manifest.append({'file': name, 'source': url, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
(FONTS / 'provenance.json').write_text(json.dumps(manifest, indent=2) + '\n')


def uri(path, mime):
    return f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode()


def image(name):
    return uri(ROOT / 'assets/institutional/originals' / name,
               'image/svg+xml' if name.endswith('.svg') else 'image/png')


font_css = '\n'.join(
    f'@font-face {{font-family: "Proof Montserrat"; font-style: normal; font-weight: {weight}; '
    f'font-display: block; src: url("{uri(FONTS / name, "font/ttf")}") format("truetype");}}'
    for weight, name in [(400, 'Montserrat-Regular.ttf'), (700, 'Montserrat-Bold.ttf')]
)
base_css = (ROOT / '.agents/skills/html-slides/assets/viewport-base.css').read_text()
proof_css = (TMP / 'brand-proof.css').read_text()
license_text = (FONTS / 'OFL.txt').read_text()

cover = f'''<section class="slide" aria-label="Prueba técnica A: portada">
<div class="canvas cover" data-layout="A">
  <img class="full-bleed" src="{image('image2.png')}" alt="Fondo institucional original de Científica Sprint">
  <h1 id="cover-title" data-text>Prototipado<br>Digital</h1>
  <div id="speaker" class="speaker">
    <p id="speaker-label" data-text>Ponente:</p>
    <p id="speaker-name" data-text>Edhú Nuñez Alvarado</p>
  </div>
</div></section>'''
educational = f'''<section class="slide" aria-label="Prueba técnica C: composición educativa">
<div class="canvas education" data-layout="C">
  <header id="institutional-header" aria-label="Identidad institucional">
    <div class="header-photo"><img class="institutional-fill" src="{image('image3.png')}" alt=""></div>
    <div id="sprint-logo" class="sprint-logo"><img class="institutional-fill" src="{image('image4.png')}" alt="Científica Sprint"></div>
    <picture id="institutional-signature" class="signature">
      <source type="image/svg+xml" srcset="{image('image6.svg')}">
      <img src="{image('image5.png')}" alt="Universidad Científica del Sur — Unidad de Empleabilidad y Emprendimiento">
    </picture>
  </header>
  <main id="body-content" class="body-content">
    <h1 id="education-title" data-text>Título de la diapositiva</h1>
    <div class="specimen-columns">
      <div class="text-specimen">
        <h2 id="sample-heading" data-text>Texto HTML editable</h2>
        <p id="sample-body" data-text>Muestra técnica para comprobar tipografía, contraste y espaciado.</p>
        <p id="sample-note" data-text>El contenido del taller se incorporará después.</p>
      </div>
      <div class="resource-specimen" id="resource-specimen">
        <p id="resource-label" data-text>Área de recurso visual</p>
        <p id="resource-note" data-text>Marcador de prueba</p>
      </div>
    </div>
  </main>
</div></section>'''

for layout, body in [('A', cover), ('C', educational)]:
    html = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Prueba técnica {layout} — Científica Sprint</title>
<!-- Specimen only. Montserrat is a provisional substitute, not Gotham.
{license_text}
-->
<style>{font_css}\n{base_css}\n{proof_css}</style></head><body>{body}</body></html>'''
    path = TMP / f'brand-proof-{layout.lower()}.html'
    path.write_text(html)
    print(path.relative_to(ROOT), path.stat().st_size, 'bytes; fully embedded')
