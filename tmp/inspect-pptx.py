"""Extract original package resources and record DrawingML composition, read-only."""
import hashlib
import io
import json
import posixpath
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SOURCE = next((ROOT / 'sources').glob('*.pptx'))
OUT = ROOT / 'output'
ASSETS = ROOT / 'assets/institutional'
NS = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def attrs(node):
    return node.attrib if node is not None else None


def contact_sheet(paths, target, columns=2):
    sheet = Image.new('RGB', (columns * 640, ((len(paths) + columns - 1) // columns) * 400), '#e5e5e5')
    draw = ImageDraw.Draw(sheet)
    for i, path in enumerate(paths):
        image = Image.open(path).convert('RGBA')
        image.thumbnail((620, 350))
        x, y = (i % columns) * 640, (i // columns) * 400
        draw.text((x + 10, y + 8), path.name, fill='black')
        sheet.paste(image, (x + 10, y + 35), image)
    sheet.save(target)


def main():
    before = sha(SOURCE.read_bytes())
    report = {'source': str(SOURCE.relative_to(ROOT)), 'source_sha256': before, 'assets': [], 'slides': []}
    with zipfile.ZipFile(SOURCE) as z:
        def relationships(part):
            folder, name = posixpath.split(part)
            rel = f'{folder}/_rels/{name}.rels'
            if rel not in z.namelist():
                return {}
            return {r.get('Id'): {
                'target': r.get('Target') if r.get('TargetMode') == 'External' else posixpath.normpath(posixpath.join(folder, r.get('Target'))),
                'type': r.get('Type').split('/')[-1], 'external': r.get('TargetMode') == 'External',
            } for r in ET.fromstring(z.read(rel))}

        parts = {n: ET.fromstring(z.read(n)) for n in z.namelist() if n.endswith('.xml')}
        presentation = parts['ppt/presentation.xml']
        report['slide_size_emu'] = attrs(presentation.find('p:sldSz', NS))
        report['embedded_fonts'] = [ET.tostring(n, encoding='unicode') for n in presentation.findall('p:embeddedFontLst/p:embeddedFont', NS)]
        report['theme_xml'] = [n for n in parts if n.startswith('ppt/theme/')]
        report['master_and_layout_xml'] = {n: ET.tostring(t, encoding='unicode') for n, t in parts.items() if n.startswith(('ppt/slideMasters/', 'ppt/slideLayouts/'))}
        report['external_relationships'] = []
        for part in parts:
            report['external_relationships'].extend({'part': part, **r} for r in relationships(part).values() if r['external'])

        for name in z.namelist():
            if not name.startswith(('ppt/media/', 'ppt/fonts/')) or name.endswith('/'):
                continue
            data = z.read(name)
            dest = ASSETS / ('fonts' if name.startswith('ppt/fonts/') else 'originals') / Path(name).name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            item = {'source_part': name, 'path': str(dest.relative_to(ROOT)), 'bytes': len(data), 'sha256': sha(data), 'byte_identical': dest.read_bytes() == data, 'uses': []}
            if name.endswith('.png'):
                with Image.open(io.BytesIO(data)) as im:
                    im.load()
                    item.update(width=im.width, height=im.height, mode=im.mode, decode_ok=True)
            elif name.endswith('.svg'):
                svg = ET.fromstring(data)
                item.update(svg_attributes=svg.attrib, element_types=sorted({e.tag.split('}')[-1] for e in svg.iter()}))
            for part, tree in parts.items():
                rels = relationships(part)
                for node in tree.iter():
                    rid = node.get('{' + NS['r'] + '}embed') or node.get('{' + NS['r'] + '}id')
                    if rid in rels and rels[rid]['target'] == name:
                        item['uses'].append({'part': part, 'relationship': rid, 'element': node.tag.split('}')[-1]})
            report['assets'].append(item)

        pres_rels = relationships('ppt/presentation.xml')
        slide_parts = [pres_rels[n.get('{' + NS['r'] + '}id')]['target'] for n in presentation.findall('p:sldIdLst/p:sldId', NS)]
        for number, part in enumerate(slide_parts, 1):
            tree = parts[part]
            slide = {'number': number, 'part': part, 'relationships': relationships(part), 'shapes': [], 'transition': None}
            transition = tree.find('p:transition', NS)
            if transition is not None:
                slide['transition'] = ET.tostring(transition, encoding='unicode')
            def walk(parent, groups):
                for node in parent:
                    kind = node.tag.split('}')[-1]
                    if kind == 'grpSp':
                        transform = node.find('p:grpSpPr/a:xfrm', NS)
                        walk(node, groups + [ET.tostring(transform, encoding='unicode')])
                    elif kind in ('sp', 'pic', 'graphicFrame'):
                        identity = node.find('.//p:cNvPr', NS)
                        slide['shapes'].append({
                            'kind': kind, 'identity': attrs(identity), 'group_transforms': groups,
                            'text': [''.join(p.itertext()) for p in node.findall('.//a:t', NS)],
                            'xml': ET.tostring(node, encoding='unicode'),
                        })
            walk(tree.find('p:cSld/p:spTree', NS), [])
            report['slides'].append(slide)

    report['source_unchanged'] = before == sha(SOURCE.read_bytes())
    (OUT / 'resource-inventory.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
    contact_sheet(sorted((ASSETS / 'originals').glob('*.png')), OUT / 'assets-contact-sheet.png')
    print(json.dumps({k: v for k, v in report.items() if k in ('slide_size_emu', 'source_sha256', 'source_unchanged')}, indent=2))
    for a in report['assets']:
        print(a['path'], a.get('width'), a.get('height'), a.get('svg_attributes'), a['uses'])


if __name__ == '__main__':
    main()
