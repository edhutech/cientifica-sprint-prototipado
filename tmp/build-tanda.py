"""Create reproducible, explicitly fictitious mobile mockups with embedded fonts."""
import base64
import shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/content/tanda'
FONTS=ROOT/'assets/content/fonts'
OUT.mkdir(parents=True,exist_ok=True)
FONTS.mkdir(parents=True,exist_ok=True)
for name in ['Montserrat-Regular.ttf','Montserrat-Bold.ttf','OFL.txt','provenance.json']:
    target=FONTS/name
    data=(ROOT/'tmp/brand-proof-fonts'/name).read_bytes()
    if target.exists() and target.read_bytes()!=data: raise RuntimeError(f'Existing font differs: {target}')
    target.write_bytes(data)
fontcss='\n'.join(f'@font-face{{font-family:Montserrat;font-style:normal;font-weight:{weight};src:url(data:font/ttf;base64,{base64.b64encode((FONTS/name).read_bytes()).decode()}) format("truetype");}}' for weight,name in [(400,'Montserrat-Regular.ttf'),(700,'Montserrat-Bold.ttf')])
panels=[
'''<h1>Elige tu servicio</h1><div class="choices">
<div class="choice selected"><div><strong>Corte clásico</strong><p>30 min · S/ 35</p></div><span class="radio on" aria-label="Seleccionado"></span></div>
<div class="choice"><div><strong>Barba</strong><p>20 min · S/ 25</p></div><span class="radio"></span></div>
<div class="choice"><div><strong>Corte + barba</strong><p>50 min · S/ 55</p></div><span class="radio"></span></div>
</div><div class="action">Continuar <span>→</span></div>''',
'''<h1>Elige tu horario</h1><p class="month">Noviembre 2026</p>
<div class="dates"><div>Jue<strong>19</strong></div><div class="selected">Vie<strong>20</strong></div><div>Sáb<strong>21</strong></div></div>
<div class="times"><span>10:00</span><span>11:00</span><span class="selected">16:00</span><span>17:00</span></div>
<p class="summary">Corte clásico · 30 min</p><div class="action">Continuar <span>→</span></div>''',
'''<h1>Tus datos</h1><div class="fields"><div><span>Nombre</span><p>Alex Rivera</p></div><div><span>Correo</span><p>alex@example.com</p></div></div>
<div class="booking"><strong>Corte clásico</strong><p>Vie 20 nov · 16:00</p></div><div class="action">Revisar reserva <span>→</span></div>''',
'''<h1>Revisa tu reserva</h1><div class="review"><div><strong>Corte clásico</strong><p>30 min · S/ 35</p></div><div><strong>Vie 20 nov 2026</strong><p>16:00</p></div><div><strong>Alex Rivera</strong><p>alex@example.com</p></div></div><div class="action">Confirmar reserva <span>→</span></div>''',
'''<div class="success-symbol" aria-hidden="true"><svg viewBox="0 0 48 48"><path d="m12 25 8 8 17-20" fill="none" stroke="currentColor" stroke-width="4"/></svg></div>
<h1 class="success-title">¡Reserva realizada!</h1><div class="success-booking"><strong>Corte clásico</strong><p>Vie 20 nov · 16:00</p><p>Alex Rivera</p></div>
<p class="disclaimer">Reserva de demostración.<br>No se registró una cita real.</p><div class="action secondary">Volver al inicio <span>↺</span></div>'''
]
css='''*{box-sizing:border-box;margin:0;padding:0}html,body{width:390px;height:640px;overflow:hidden}body{font-family:Montserrat,sans-serif;background:#f7f6f0;color:#152c27;font-size:22px;line-height:1.35}
.app{height:640px;width:390px;background:#f7f6f0;position:relative}header{height:82px;display:flex;align-items:center;padding:0 24px;gap:12px;border-bottom:1px solid #d5ddd7;background:white}.wordmark{font-size:30px;font-weight:700;letter-spacing:-1px;color:#174c40}.demo{font-size:14px;font-weight:700;letter-spacing:1.5px;color:#174c40}.step{margin-left:auto;font-size:18px;color:#465c54}
main{position:absolute;left:24px;right:24px;top:108px;bottom:64px}section{height:100%;position:relative}section[hidden]{display:none}h1{font-size:30px;line-height:1.2;margin-bottom:26px;letter-spacing:-.7px}.choices{display:grid;gap:14px}.choice{background:#fff;padding:16px;border:1px solid #c3cfc7;min-height:86px;display:flex;justify-content:space-between;align-items:center}.choice strong{font-size:23px}.choice p{font-size:20px;margin-top:4px}.selected{background:#e8efe8!important;border:2px solid #174c40!important;color:#174c40}.radio{width:20px;height:20px;border:2px solid #9baea3;border-radius:50%;flex:none}.radio.on{border:6px solid #174c40}.action{position:absolute;bottom:0;left:0;right:0;background:#174c40;color:white;padding:16px 18px;display:flex;justify-content:space-between;align-items:center;min-height:64px;font-size:23px;font-weight:700}.action span{font-size:28px}.month{margin-bottom:14px;font-weight:700;font-size:22px}.dates{display:flex;gap:12px;margin-bottom:22px}.dates>div{background:white;border:1px solid #c3cfc7;text-align:center;flex:1;padding:9px;font-size:18px}.dates strong{display:block;font-size:28px}.times{display:grid;grid-template-columns:1fr 1fr;gap:12px}.times span{padding:10px;border:1px solid #c3cfc7;text-align:center;background:white;font-size:23px}.summary{margin-top:18px;font-size:20px}.fields{display:grid;gap:24px}.fields span{font-size:21px;font-weight:700}.fields p{padding:16px 12px;margin-top:8px;background:#fff;border:1px solid #c3cfc7;font-size:23px}.booking{margin-top:30px;font-size:22px}.booking p{margin-top:4px}.review{display:grid;gap:20px}.review>div{padding-bottom:17px;border-bottom:1px solid #c3cfc7}.review strong{font-size:23px}.review p{font-size:22px;margin-top:4px}.success-symbol{width:66px;height:66px;background:#e1ede2;color:#174c40;border-radius:50%;margin:0 auto 14px;padding:9px}.success-symbol svg{width:100%}.success-title{text-align:center;font-size:29px;margin-bottom:20px}.success-booking{text-align:center;font-size:23px;line-height:1.6}.disclaimer{margin-top:20px;text-align:center;font-size:18px;line-height:1.45;color:#465c54}.secondary{background:white;color:#174c40;border:1px solid #174c40}footer{position:absolute;bottom:20px;width:100%;text-align:center;color:#465c54;font-size:16px}
'''
html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Tanda — caso ficticio</title><!-- {(FONTS/'OFL.txt').read_text()} --><style>{fontcss}{css}</style></head><body><div class="app"><header><span class="wordmark">Tanda</span><span class="demo">DEMO</span><span class="step" id="step">1 / 5</span></header><main>{''.join(f'<section data-screen="{i}" hidden>{p}</section>' for i,p in enumerate(panels,1))}</main><footer>Simulación · Datos ficticios</footer></div><script>const n=Math.max(1,Math.min(5,Number(new URLSearchParams(location.search).get('screen'))||1));document.querySelector(`[data-screen="${{n}}"]`).hidden=false;document.querySelector('#step').textContent=n+' / 5';</script></body></html>'''
(OUT/'mockup.html').write_text(html)
(OUT/'tanda-mark.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect width="100" height="100" rx="24" fill="#174c40"/><path d="M24 28h52v14H57v35H43V42H24z" fill="#f7f6f0"/></svg>')
(OUT/'README.md').write_text('''# Tanda — recursos originales del caso ficticio

Cinco vistas completas de una única reserva simulada, no una aplicación ni una barbería real. Generación: `python tmp/build-tanda.py`; capturas: `node tmp/render-tanda.mjs`. Abrir `mockup.html?screen=1` … `?screen=5` en Chromium para reproducir cada vista. Controles ilustrativos; no procesan reservas.

Viewport 390 × 640 CSS px; PNG 780 × 1280 (DPR 2). Fuente Montserrat 400/700 con OFL incrustada. Verde #174C40, tinta #152C27, crema #F7F6F0. La marca gráfica fue creada para este caso, sin representar una organización real.

Datos coherentes: Corte clásico, 30 min, S/ 35; viernes 20 de noviembre de 2026 a las 16:00; Alex Rivera, alex@example.com (ficticios). En las cinco vistas se declara DEMO y simulación. La confirmación aclara que no hay cita real.

`screen-01.png`: elegir servicio; `screen-02.png`: fecha/horario; `screen-03.png`: datos; `screen-04.png`: revisar/confirmar; `screen-05.png`: reserva realizada dentro de la simulación. La primera vista también introduce Tanda en slide 7 y acompaña slide 10, sin desarrollar otro caso.
''')
print('Tanda mockup and licensed font copies generated')
