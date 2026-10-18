"""Record source integrity, contrast and corroborative header comparison."""
import hashlib
import json
import math
from pathlib import Path
from PIL import Image, ImageChops, ImageStat

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/brand-proof'
inventory = json.loads((ROOT / 'output/resource-inventory.json').read_text())
checks = json.loads((OUT / 'composition-checks.json').read_text())


def luminance(rgb):
    channels = [c / 255 for c in rgb]
    channels = [c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in channels]
    return sum(c * weight for c, weight in zip(channels, [.2126, .7152, .0722]))


def contrast(a, b):
    low, high = sorted([luminance(bytes.fromhex(value[1:])) for value in (a, b)])
    return (high + .05) / (low + .05)


reference = Image.open(ROOT / 'output/template-slide-3.png').convert('RGB').crop((0, 0, 1920, 215))
proof = Image.open(OUT / 'layout-c-1920x1080.png').convert('RGB').crop((0, 0, 1920, 215))
source = Image.open(ROOT / 'assets/institutional/originals/image2.png').convert('RGB')
cover = next(r for r in checks['results'] if r['layout'] == 'A' and r['viewport']['width'] == 1920)
text_contrast = {}
for text in cover['text']:
    b = text['box']
    area = source.crop((math.floor(b['x'] * 1.6), math.floor(b['y'] * 1.6),
                        math.ceil(b['right'] * 1.6), math.ceil(b['bottom'] * 1.6)))
    max_luminance = max(luminance(pixel) for pixel in area.get_flattened_data())
    text_contrast[text['id']] = 1.05 / (max_luminance + .05)

report = {
    'source_unchanged': hashlib.sha256((ROOT / inventory['source']).read_bytes()).hexdigest() == inventory['source_sha256'],
    'original_assets_unchanged': all(hashlib.sha256((ROOT / a['path']).read_bytes()).hexdigest() == a['sha256'] for a in inventory['assets']),
    'contrast_ratios': {f'{a} on {b}': contrast(a, b) for a, b in [('#00358E', '#FFFFFF'), ('#000000', '#FFFFFF'), ('#F68D20', '#FFFFFF'), ('#F68D20', '#00358E')]},
    'cover_min_white_text_contrast_over_entire_text_boxes': text_contrast,
    'header_comparison': {
        'region': [0, 0, 1920, 215],
        'reference': 'output/template-slide-3.png (LibreOffice, not PowerPoint)',
        'mean_absolute_rgb_difference_0_255': sum(ImageStat.Stat(ImageChops.difference(reference, proof)).mean) / 3,
        'interpretation': 'Corroborative only; resampling, antialiasing and vector rendering differ. No claim of pixel-identical PowerPoint output.',
    },
}
(OUT / 'visual-measurements.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
assert report['source_unchanged'] and report['original_assets_unchanged']
