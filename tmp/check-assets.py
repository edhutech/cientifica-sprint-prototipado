"""Temporary browser decoding check; not a presentation."""
import base64
import json
import subprocess
from pathlib import Path
from xml.etree import ElementTree as ET

root = Path(__file__).resolve().parents[1]
assets = []
for path in sorted((root / 'assets/institutional/originals').iterdir()):
    mime = 'image/svg+xml' if path.suffix == '.svg' else 'image/png'
    assets.append({'name': path.name, 'src': f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode()})
html = '''<!doctype html><meta charset="utf-8"><title>Resource decoding QA</title>
<pre id="result">PENDING</pre><script>
const assets = ASSETS;
Promise.all(assets.map(({name,src}) => new Promise(resolve => {
  const image = new Image();
  image.onload = () => resolve({name, ok:true, width:image.naturalWidth, height:image.naturalHeight});
  image.onerror = () => resolve({name, ok:false});
  image.src = src; document.body.append(image);
}))).then(results => document.querySelector('#result').textContent = JSON.stringify(results));
</script>'''.replace('ASSETS', json.dumps(assets))
page = root / 'tmp/asset-decoding-check.html'
page.write_text(html)
proc = subprocess.run([
    'chromium-browser', '--headless', '--no-sandbox', '--disable-gpu',
    '--user-data-dir=/tmp/opencode/proto-chromium-assets', '--no-first-run',
    '--virtual-time-budget=10000', '--dump-dom', page.as_uri(),
], capture_output=True, text=True, timeout=60)
(root / 'tmp/asset-decoding-browser.log').write_text(proc.stderr)
(root / 'tmp/asset-decoding-dom.html').write_text(proc.stdout)
import re
match = re.search(r'<pre id="result">(.*?)</pre>', proc.stdout, re.S)
if proc.returncode or not match or match.group(1) == 'PENDING':
    raise RuntimeError('Browser check failed; see tmp/asset-decoding-browser.log')
results = json.loads(match.group(1))
report = {'browser': subprocess.check_output(['chromium-browser', '--version'], text=True).strip(), 'method': 'HTML img load events and natural dimensions on embedded data URIs', 'results': results}
svg = ET.parse(root / 'assets/institutional/originals/image6.svg')
report['svg_element_types'] = sorted({e.tag.split('}')[-1] for e in svg.iter()})
report['svg_external_hrefs'] = [v for e in svg.iter() for k, v in e.attrib.items() if k.split('}')[-1] == 'href' and not v.startswith(('#', 'data:'))]
(root / 'output/asset-compatibility.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
assert all(r['ok'] for r in results)
