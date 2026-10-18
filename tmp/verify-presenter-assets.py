"""Inventory user-supplied resources and render diagnostic contact sheets."""
import base64
import hashlib
import html
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PRESENTER = ROOT / 'assets/content/presenter'
OUT = ROOT / 'output/presenter'
OUT.mkdir(parents=True, exist_ok=True)
MIME = {'.svg': 'image/svg+xml', '.png': 'image/png', '.webp': 'image/webp', '.jpeg': 'image/jpeg'}
resources = []
for path in sorted([* (PRESENTER / 'logos').iterdir(), * (PRESENTER / 'photo').iterdir()]):
    if path.suffix.lower() not in MIME:
        continue
    data = path.read_bytes()
    item = {'file': str(path.relative_to(ROOT)), 'name': path.name, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(), 'mime': MIME[path.suffix.lower()]}
    if path.suffix == '.svg':
        tree = ET.fromstring(data)
        item['svg_attributes'] = tree.attrib
        item['element_types'] = sorted({e.tag.split('}')[-1] for e in tree.iter()})
        item['external_references'] = [v for e in tree.iter() for k, v in e.attrib.items()
                                       if k.split('}')[-1] in ('href', 'src') and not v.startswith(('#', 'data:'))]
        item['css_urls'] = re.findall(r'url\(([^)]+)\)', data.decode())
    else:
        with Image.open(path) as im:
            im.load()
            rgba = im.convert('RGBA')
            item.update(width=im.width, height=im.height, format=im.format, mode=im.mode,
                        alpha_extrema=rgba.getchannel('A').getextrema(), decode_ok=True)
    resources.append(item)

protected = [ROOT / 'branding/brand-spec.md', * (ROOT / 'assets/institutional').rglob('*')]
protected = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in protected if p.is_file()}
(OUT / 'protected-files-hashes.json').write_text(json.dumps(protected, indent=2) + '\n')


def tag(item):
    data = (ROOT / item['file']).read_bytes()
    return f'<img data-name="{html.escape(item["name"])}" alt="{html.escape(item["name"])}" src="data:{item["mime"]};base64,{base64.b64encode(data).decode()}">'


cards = []
for i, item in enumerate((r for r in resources if '/logos/' in r['file']), 1):
    if 'svg_attributes' in item:
        dimensions = item['svg_attributes'].get('viewBox', '') + ' (viewBox)'
    else:
        dimensions = f'{item["width"]} × {item["height"]} px'
    cards.append(f'<article><div class="sample">{tag(item)}</div><h2>{i:02} · {html.escape(item["name"])}</h2><p>{html.escape(dimensions)}</p></article>')
photo = next(r for r in resources if '/photo/' in r['file'])
results = []
for theme in ['light', 'dark']:
    document = '''<!doctype html><html lang="es"><meta charset="utf-8">
<title>Verificación de recursos del presentador</title>
<style>*{box-sizing:border-box}body{margin:0;padding:24px;background:#e5e7eb;color:#111827;font:14px Arial,sans-serif}
h1{font-size:24px;margin:0 0 10px}header p{margin:0 0 20px}main{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
article{background:#fff;padding:12px;height:258px;border:1px solid #cbd5e1;overflow:hidden}
.sample{height:174px;display:flex;justify-content:center;align-items:center;background:BACKGROUND;padding:12px}
img{display:block;max-width:100%;max-height:150px;object-fit:contain}h2{font-size:13px;line-height:1.25;margin:10px 0 5px;overflow-wrap:anywhere}article p{font-size:12px;margin:0}
</style><header><h1>Logos recibidos · hoja de contacto · THEME</h1>
<p>Archivos originales sin recolorear ni recortar. Nombres y fondos solo para revisión; no es la diapositiva «Sobre mí».</p></header>
<main>CARDS</main><div hidden>PHOTO</div><pre hidden id="qa">PENDING</pre>
<script>addEventListener('load',()=>{document.querySelector('#qa').textContent=JSON.stringify([...document.images].map(im=>({name:im.dataset.name,loaded:im.complete&&im.naturalWidth>0,width:im.naturalWidth,height:im.naturalHeight,embedded:im.currentSrc.startsWith('data:')})));});</script></html>'''
    document = document.replace('BACKGROUND', '#ffffff' if theme == 'light' else '#202733')
    document = document.replace('THEME', 'fondo blanco' if theme == 'light' else 'fondo oscuro')
    document = document.replace('CARDS', ''.join(cards)).replace('PHOTO', tag(photo))
    path = ROOT / f'tmp/presenter-contact-{theme}.html'
    path.write_text(document)
    capture = OUT / f'logos-contact-sheet-{theme}.png'
    process = subprocess.run(['chromium-browser', '--headless', '--no-sandbox', '--disable-gpu',
                              '--hide-scrollbars', '--force-device-scale-factor=1', '--window-size=1600,1220',
                              '--user-data-dir=/tmp/opencode/presenter-assets-qa', '--no-first-run',
                              '--virtual-time-budget=5000', f'--screenshot={capture}', '--dump-dom', path.as_uri()],
                             capture_output=True, text=True, timeout=60)
    (ROOT / f'tmp/presenter-{theme}-browser.log').write_text(process.stderr)
    match = re.search(r'<pre[^>]*id="qa"[^>]*>(.*?)</pre>', process.stdout, re.S)
    if process.returncode or not match or match.group(1) == 'PENDING':
        raise RuntimeError(f'Chromium check failed: {theme}')
    loaded = json.loads(html.unescape(match.group(1)))
    assert len(loaded) == len(resources) and all(r['loaded'] and r['embedded'] for r in loaded)
    results.append({'theme': theme, 'screenshot': str(capture.relative_to(ROOT)), 'images': loaded})

for item in resources:
    assert hashlib.sha256((ROOT / item['file']).read_bytes()).hexdigest() == item['sha256']
report = {'source': 'User-supplied files; original web URLs not supplied.',
          'browser': subprocess.check_output(['chromium-browser', '--version'], text=True).strip(),
          'originals_unchanged': True, 'resources': resources, 'checks': results}
(OUT / 'resource-checks.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(f'{len(resources)} resources loaded successfully; 2 contact sheets generated; original bytes unchanged.')
