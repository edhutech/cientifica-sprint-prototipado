from pathlib import Path
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[1]

def sheet(paths,target,columns,width):
    height=round(width*9/16)
    canvas=Image.new('RGB',(columns*width,((len(paths)+columns-1)//columns)*(height+32)), '#e5e7eb')
    draw=ImageDraw.Draw(canvas)
    for i,p in enumerate(paths):
        im=Image.open(p).convert('RGB');im=im.resize((width,height),Image.Resampling.LANCZOS)
        x=(i%columns)*width;y=(i//columns)*(height+32)
        draw.text((x+10,y+8),p.name,fill='#000000')
        canvas.paste(im,(x,y+32))
    canvas.save(target)

for resolution in ['1920x1080','1366x768']:
    folder=ROOT/'output/qa'/resolution
    paths=[folder/f'slide-{i:02}.png' for i in range(1,19)]
    if resolution=='1920x1080':sheet(paths,ROOT/'output/deck-contact-sheet.png',3,640)
    for batch in range(3):sheet(paths[batch*6:(batch+1)*6],ROOT/f'output/qa/contact-{resolution}-{batch+1}.png',2,800)
for n in [12,13]:
    paths=sorted((ROOT/'output/qa/1920x1080').glob(f'slide-{n}-state-*.png'))
    sheet(paths,ROOT/f'output/qa/reveals-{n}.png',2,800)
print('General contact sheet, six review sheets, and two reveal sheets generated.')
