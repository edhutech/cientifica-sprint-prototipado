"""Assemble the 18-slide standalone deck from approved layouts and explicit content."""
from pathlib import Path
import base64
import html
import json
import re

ROOT=Path(__file__).resolve().parents[1]
slides=json.loads((ROOT/'deck/content.json').read_text())
revision=json.loads((ROOT/'deck/revisions.json').read_text())
expanded=[]
for original in slides:
    key=str(original['number'])
    if key in revision['before']:
        expanded.append({**revision['before'][key], 'reveals':0, 'intro':True})
    expanded.append({**original, **revision['updates'].get(key,{})})
slides=expanded

def uri(path):
    p=ROOT/path
    mime={'.png':'image/png','.svg':'image/svg+xml','.webp':'image/webp','.jpeg':'image/jpeg','.ttf':'font/ttf'}[p.suffix]
    return f'data:{mime};base64,'+base64.b64encode(p.read_bytes()).decode()

def img(path,alt,cls=''):
    return f'<img class="{cls}" src="{uri(path)}" alt="{html.escape(alt)}">'

def p(text,cls=''):
    return f'<p class="{cls}" data-text>{html.escape(text)}</p>'

def h2(text,cls=''):
    return f'<h2 class="{cls}" data-text>{html.escape(text)}</h2>'

def items(texts,cls='plain-list',ordered=False):
    tag='ol' if ordered else 'ul'
    return f'<{tag} class="{cls}">'+''.join(f'<li data-text>{html.escape(t)}</li>' for t in texts)+f'</{tag}>'

def screen(n):
    return img(f'assets/content/tanda/screen-{n:02}.png',f'Tanda, pantalla {n} de 5. Caso ficticio de reserva de cita.','tanda-screen')

# Reuse the approved header structure and original image data; embed the large
# campus bitmap only once through CSS, with exactly the approved crop geometry.
proof_c=(ROOT/'tmp/brand-proof-c.html').read_text()
header=re.search(r'<header id="institutional-header".*?</header>',proof_c,re.S)[0]
header=header.replace('id="institutional-header"','class="institutional-header"')
header=re.sub(r' id="(?:sprint-logo|institutional-signature)"','',header)
header=re.sub(r'<div class="header-photo"><img.*?</div>','<div class="header-photo" aria-hidden="true"></div>',header,flags=re.S)
proof_a=(ROOT/'tmp/brand-proof-a.html').read_text()
cover=re.search(r'<div class="canvas cover".*?</div></section>',proof_a,re.S)[0].removesuffix('</section>')
cover=cover.replace('<h1 id="cover-title"','<p class="ribbon-label" data-text>Taller</p><h1 id="cover-title"')
fontcss='\n'.join(f'@font-face{{font-family:Montserrat;font-style:normal;font-weight:{w};font-display:block;src:url("{uri("assets/content/fonts/"+n)}") format("truetype");}}' for w,n in [(400,'Montserrat-Regular.ttf'),(700,'Montserrat-Bold.ttf')])
base=(ROOT/'.agents/skills/html-slides/assets/viewport-base.css').read_text()
approved=(ROOT/'tmp/brand-proof.css').read_text().split('.specimen-columns')[0].replace('"Proof Montserrat"','Montserrat').replace('#institutional-header','.institutional-header').replace('#education-title','.title')
shared=f'.header-photo{{background-image:url("{uri("assets/institutional/originals/image3.png")}");background-size:100% 502.325%;background-position:left top;background-repeat:no-repeat;}}'

def content(s):
    if s.get('intro'):
        return img(s['image'],s['alt'],'section-art') if s.get('image') else ''
    t=s['text'];n=s['number']
    if n==2:
        logos=[('assets/content/presenter/logos/logo-startup-peru 2.svg','Startup Perú',''),('assets/content/presenter/logos/proinnovate-logo-removebg-preview 2.svg','ProInnóvate',''),('assets/content/presenter/logos/MS_Startups_Celebration_Badge_Dark.webp','Microsoft for Startups, insignia proporcionada',''),('assets/content/presenter/logos/fundacion romero.webp','Fundación Romero',''),('assets/content/presenter/derived/senati-dark.png','SENATI',''),('assets/content/presenter/logos/logo-nutrih-azul 1.svg','Nutri H','logo-nutri'),('assets/content/presenter/derived/basf-trimmed.png','BASF','logo-basf'),('assets/content/presenter/derived/nexum-dark.svg','NEXUM PUCP',''),('assets/content/presenter/derived/hub-udep-dark.svg','HUB UDEP','')]
        rolelogos=['guayerd ico.webp','ai_playground_per_logo.jpeg','LetyMind ico.svg']
        roles='<ul class="experience">'+''.join('<li>'+img('assets/content/presenter/logos/'+logo,'','role-logo')+'<span data-text>'+html.escape(text)+'</span></li>' for logo,text in zip(rolelogos,t[2:]))+'</ul>'
        return p(t[1],'positioning')+roles+img('assets/content/presenter/photo/perfil.png','Edhú Nuñez Alvarado','portrait')+'<div class="logo-cloud" aria-label="Organizaciones">'+''.join('<figure>'+img(path,alt,cls)+'</figure>' for path,alt,cls in logos)+'</div>'
    if n==3:
        return '<div class="three">'+''.join(f'<article><span class="number" aria-hidden="true">{i:02}</span>'+p(text)+'</article>' for i,text in enumerate(t[:3],1))+'</div>'+p(t[3],'takeaway')
    if n==4:
        return p(t[0],'lead')+'<div class="modes">'+''.join('<figure>'+img(f'assets/content/illustrations/{asset}.svg','', '')+f'<figcaption data-text>{label}</figcaption></figure>' for asset,label in zip(['visual','interactive','simulated'],t[1:4]))+'</div>'+p(t[4],'takeaway')
    if n==5:
        return '<div class="three">'+''.join('<article>'+h2(t[i])+p(t[i+1])+'</article>' for i in [0,2,4])+'</div>'
    if n==6:
        return '<div class="three illustration-grid">'+''.join('<figure>'+img(f'assets/content/illustrations/{a}.svg',f'Ilustración original: {label}')+f'<figcaption data-text>{label}</figcaption></figure>' for a,label in zip(['paper','digital','physical'],t[:3]))+'</div>'+p(t[3],'takeaway')
    if n==7:
        return '<div class="split"><div class="copy">'+p(t[0],'case-tag')+h2(t[1])+p(t[2])+h2(t[3])+p(t[4])+'</div><div class="screen-holder">'+screen(1)+'</div></div>'
    if n==8:
        return p(t[0],'lead')+'<div class="priority">'+p(t[1],'blue')+p(t[2],'muted')+'</div>'+p(t[3],'takeaway')
    if n==9:return items(t,'questions',True)
    if n==10:
        return '<div class="split"><div class="copy">'+p(t[0],'lead')+'<div class="secondary-functions">'+h2(t[1])+p(t[2])+'</div></div><div class="screen-holder">'+screen(1)+'</div></div>'
    if n==11:
        return p(t[0],'lead')+'<div class="happy-bottom">'+items(t[1:5])+'<div class="mini-flow">'+''.join(('<b aria-hidden="true">→</b>' if i else '')+f'<span data-text>{x}</span>' for i,x in enumerate(t[5:]))+'</div></div>'
    if n in [12,13]:
        start=1 if n==12 else 4
        count=3 if n==12 else 2
        responses=''.join(f'<li class="answer-slot"><span class="step-number" aria-hidden="true">{start+i:02}</span><span class="answer" data-text data-from="{2*i+1}">{html.escape(t[i+1])}</span></li>' for i in range(count))
        left=f'<div class="discovery-answers"'+(' data-states="0,1,2,3"' if n==13 else '')+'>'+p(t[0],'question')+f'<ol class="answer-list">{responses}</ol></div>'
        if n==13:left+='<div class="discovery-summary" data-states="4">'+h2(t[3])+items(t[4:],'full-path',True)+'</div>'
        screens=''
        for i in range(count):
            states=f'{2*i},{2*i+1}'+(',4' if n==13 and i==1 else '')
            screens+=screen(start+i).replace('<img ',f'<img data-states="{states}" ')
        return '<div class="discovery-grid"><div class="discovery-left">'+left+'</div><div class="screen-stack">'+screens+'</div></div>'
    if n==14:
        return '<div class="task-layout"><div>'+p('Actividad grupal','task-label')+p(t[1])+items(t[2:5],'plain-list',True)+p(t[5],'takeaway small')+'</div><div class="time-block"><strong data-text>20</strong>'+p('minutos')+'</div></div>'
    if n==15:
        return p(t[0],'task-label')+p(t[1],'lead')+items(t[2:],'individual-steps',True)
    if n==16:return items(t[:4],'plain-list',True)+p(t[4],'takeaway')
    if n==17:return '<div class="validation-grid">'+items(t[:4],'plain-list',True)+f'<blockquote data-text>{html.escape(t[4])}</blockquote></div>'+p(t[5],'takeaway')
    if n==18:
        mail='<svg class="contact-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m3 6 9 7 9-7"/></svg>'
        web='<svg class="contact-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="12" cy="12" r="10"/><ellipse cx="12" cy="12" rx="4" ry="10"/><path d="M2 12h20M4 6.5h16M4 17.5h16"/></svg>'
        return '<div class="contact-links"><a href="https://www.linkedin.com/in/edhutech" target="_blank" rel="noopener noreferrer"><span class="linkedin-icon" aria-hidden="true">in</span><span data-text>linkedin.com/in/edhutech</span></a><a href="mailto:hola@edhutech.com">'+mail+'<span data-text>hola@edhutech.com</span></a><a href="https://edhutech.com" target="_blank" rel="noopener noreferrer">'+web+'<span data-text>edhutech.com</span></a></div>'+img('assets/content/presenter/photo/perfil.png','Edhú Nuñez Alvarado','closing-portrait')
    raise ValueError(n)

classes={2:'about',3:'results',4:'definition',5:'comparison',6:'illustrations long-title',7:'tanda-intro',8:'core',9:'long-title',10:'tanda-core',11:'happy',12:'discovery long-title',13:'discovery long-title',14:'team',15:'live-demo',16:'selection',17:'validation',18:'closing'}
sections=[]
for s in slides:
    n=s['number'];title=html.escape(s['title']);cls=classes.get(n,'')+' '+s.get('theme','')+(' section-intro' if s.get('intro') else '')
    body=cover if n==1 else f'<div class="canvas {cls}">{header}<div class="body-content"><h1 class="title" id="title-{n}" data-text>{title}</h1>'+('<div class="content">' if n!=18 else '')+content(s)+('</div>' if n!=18 else '')+'</div></div>'
    sections.append(f'<section class="slide" id="slide-{n}" data-title="{title}" data-max-state="{s["reveals"]}" aria-labelledby="'+('cover-title' if n==1 else f'title-{n}')+'">'+body+'</section>')
navigation='''<nav class="controls" id="controls" aria-label="Navegación de la presentación" hidden><button id="previous" type="button" aria-label="Anterior" title="Anterior">←</button><output id="counter" aria-label="Diapositiva actual">1 / 18</output><button id="next" type="button" aria-label="Siguiente" title="Siguiente">→</button><button id="fullscreen" type="button" aria-label="Pantalla completa" aria-pressed="false" title="Pantalla completa (F)">⛶</button></nav><div id="live-status" class="sr-only" aria-live="polite" aria-atomic="true"></div>'''
license=(ROOT/'assets/content/fonts/OFL.txt').read_text()
doc=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Prototipado Digital — Científica Sprint</title><!-- Montserrat font license\n{license}\n--><style>{fontcss}\n{base}\n{approved}\n{shared}\n{(ROOT/'deck/deck.css').read_text()}</style></head><body>{''.join(sections)}{navigation}<script>{(ROOT/'deck/deck.js').read_text()}</script></body></html>'''
doc=doc.replace('</head>','<style>'+(ROOT/'deck/revision.css').read_text()+'</style></head>')
(ROOT/'output/deck.html').write_text(doc)
print(f'output/deck.html: {len(doc.encode())/1024/1024:.2f} MiB; {len(slides)} slides; 9 progressive advances; no external runtime dependencies')
