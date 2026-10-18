from pathlib import Path
import base64, urllib.request
root=Path(__file__).resolve().parents[1]
out=root/'assets/content/sections';out.mkdir(exist_ok=True)
url='https://www.gstatic.com/images/branding/productlogos/ai_studio/v1/web-512dp/logo_ai_studio_color_1x_web_512dp.png'
urllib.request.urlretrieve(url,out/'google-ai-studio.png')
def pic(n,x,y,w,h):
 data=base64.b64encode((root/f'assets/content/tanda/screen-{n:02}.png').read_bytes()).decode()
 return f'<image href="data:image/png;base64,{data}" x="{x}" y="{y}" width="{w}" height="{h}"/>'
def save(name,art):
 (out/name).write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 680">'+art+'</svg>')
save('prototype.svg','''<ellipse cx="450" cy="620" rx="350" ry="24" fill="#002968"/>
<g transform="translate(45 110) rotate(-8 150 200)"><rect width="300" height="430" fill="#fff9ea"/><path d="M30 48h170M30 65h100" stroke="#667184" stroke-width="6"/><rect x="30" y="100" width="235" height="70" fill="none" stroke="#667184" stroke-width="3"/><rect x="30" y="195" width="235" height="70" fill="none" stroke="#667184" stroke-width="3"/><rect x="30" y="290" width="235" height="70" fill="none" stroke="#667184" stroke-width="3"/><path d="M48 120h130m-130 22h80m-80 74h140m-140 22h75m-75 75h140" stroke="#667184" stroke-width="4"/><path d="m238 134 10 10 22-24" fill="none" stroke="#f68d20" stroke-width="5"/></g>
<path d="M349 320q48-45 90-8m-22-24 22 24-30 13" fill="none" stroke="#f68d20" stroke-width="8"/>
<rect x="452" y="40" width="340" height="580" rx="28" fill="#112039"/><rect x="467" y="60" width="310" height="540" rx="10" fill="white"/>'''+pic(1,475,70,294,516)+'''<path d="m60 590 214-65 9 27-214 65-35-5z" fill="#f68d20"/><path d="m60 590 9 27-35-5z" fill="#ead7b1"/>''')
save('happy-path.svg','''<ellipse cx="425" cy="590" rx="385" ry="30" fill="#002968"/><path d="M120 535C240 650 310 410 420 535S650 640 740 535" stroke="#f68d20" stroke-width="10" fill="none" stroke-dasharray="16 12"/>'''+''.join(f'<rect x="{x-8}" y="{y-8}" width="236" height="377" rx="16" fill="#132544"/>'+pic(n,x,y,220,361) for n,x,y in [(1,35,100),(2,315,155),(5,595,100)])+'''<path d="m270 300 27 0-10-12m10 12-10 12m270-12h27l-10-12m10 12-10 12" fill="none" stroke="white" stroke-width="5"/>''')
(out/'README.md').write_text('# Recursos de aperturas\n\nIlustraciones originales reproducibles: boceto y prototipo digital; secuencia de pantallas conectadas. Reutilizan el caso ficticio Tanda, no fotografías reales.\n\nLogo Google AI Studio descargado desde el recurso enlazado en https://aistudio.google.com/welcome :\n'+url+'\nSin alteración del original. Incrustado en el HTML para funcionamiento offline.\n')
print('Section illustrations and official Google AI Studio asset ready')
