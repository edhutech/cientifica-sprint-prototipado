import {openBrowser} from './chromium.mjs';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
import {execFileSync} from 'node:child_process';

const root=resolve(import.meta.dirname,'..');
const out=resolve(root,'output/qa');await mkdir(out,{recursive:true});
const source=await readFile(resolve(root,'output/deck.html'),'utf8');
const browser=await openBrowser('sprint-final-qa');
const frames=[];const functional=[];
const assert=(condition,label,details)=>{functional.push({label,pass:!!condition,details});if(!condition)console.error('FAIL',label,details);};
const state=()=>browser.evaluate('({slide:Number(document.body.dataset.slide),state:Number(document.body.dataset.state)})');
const settle=()=>browser.evaluate('(async()=>{await Promise.all(document.getAnimations().map(a=>a.finished.catch(()=>{})));await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));return true;})()');
async function go(slide){await browser.key('Home');for(let guard=0;guard<40&&(await state()).slide<slide;guard++)await browser.key('ArrowRight');}
async function click(selector){const box=await browser.evaluate(`(()=>{const r=document.querySelector(${JSON.stringify(selector)}).getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2};})()`);await browser.call('Input.dispatchMouseEvent',{type:'mousePressed',button:'left',clickCount:1,...box});await browser.call('Input.dispatchMouseEvent',{type:'mouseReleased',button:'left',clickCount:1,...box});}
async function inspect(){return browser.evaluate(`(()=>{
  const slide=document.querySelector('.slide.active');
  const canvas=slide.querySelector('.canvas');
  const box=e=>{const {x,y,width,height,right,bottom}=e.getBoundingClientRect();return {x,y,width,height,right,bottom};};
  const visible=e=>e.getClientRects().length>0 && !e.closest('[hidden]') && getComputedStyle(e).visibility!=='hidden';
  const stage=box(canvas);
  const text=[...slide.querySelectorAll('[data-text]')].filter(visible).map(e=>({text:e.innerText,tag:e.tagName,box:box(e),fontSize:parseFloat(getComputedStyle(e).fontSize),overflow:e.scrollWidth>e.clientWidth+1||e.scrollHeight>e.clientHeight+2}));
  const overlap=(a,b)=>a.x<b.right-.8&&a.right>b.x+.8&&a.y<b.bottom-.8&&a.bottom>b.y+.8;
  const collisions=[];
  for(let i=0;i<text.length;i++)for(let j=i+1;j<text.length;j++)if(overlap(text[i].box,text[j].box))collisions.push([text[i].text,text[j].text]);
  const outside=text.filter(t=>t.box.x<stage.x-1||t.box.y<stage.y-1||t.box.right>stage.right+1||t.box.bottom>stage.bottom+1);
  const header=slide.querySelector('.institutional-header');
  const headerCollisions=header?text.filter(t=>overlap(t.box,box(header))).map(t=>t.text):[];
  const images=[...slide.querySelectorAll('img')].filter(visible).map(im=>({alt:im.alt,box:box(im),natural:[im.naturalWidth,im.naturalHeight],loaded:im.complete&&im.naturalWidth>0,embedded:im.currentSrc.startsWith('data:')}));
  const phone=slide.querySelector('.tanda-screen:not([hidden])');
  const discovery=slide.querySelector('.screen-stack');
  const answers=[...slide.querySelectorAll('.answer')].filter(visible).map(e=>e.innerText);
  const imageTextCollisions=[];
  for(const im of images.filter(im=>!im.alt.startsWith('Fondo institucional')&&!im.alt.startsWith('Universidad')&&im.alt!=='Científica Sprint'&&im.alt!==''))for(const t of text)if(overlap(im.box,t.box))imageTextCollisions.push([im.alt,t.text]);
  return {slide:Number(document.body.dataset.slide),state:Number(document.body.dataset.state),viewport:[innerWidth,innerHeight],canvas:stage,text,collisions,headerCollisions,outside,images,imageTextCollisions,
    pageOverflow:document.documentElement.scrollWidth>innerWidth||document.documentElement.scrollHeight>innerHeight,
    fontLoaded:document.fonts.check('400 36px Montserrat')&&document.fonts.check('700 36px Montserrat'),
    phone:phone?box(phone):null,screenIndex:phone?phone.alt:null,answers,
    summaryVisible:!!slide.querySelector('.discovery-summary:not([hidden])'),
    controls:box(document.querySelector('#controls')),
    stageCount:document.querySelectorAll('.slide').length,
    visibleSlides:document.querySelectorAll('.slide:not([hidden])').length};
})()`);}

try{
  await browser.call('Network.emulateNetworkConditions',{offline:true,latency:0,downloadThroughput:0,uploadThroughput:0});
  for(const [width,height] of [[1920,1080],[1366,768]]){
    const dir=resolve(out,`${width}x${height}`);await mkdir(dir,{recursive:true});
    await browser.viewport(width,height);
    await browser.load(pathToFileURL(resolve(root,'output/deck.html')).href,'.slide.active');
    assert((await state()).slide===1,`Initial slide ${width}`);
    let advances=0;
    for(let slide=1;slide<=18;slide++){
      const max=slide===12?5:slide===13?4:0;
      const phonePositions=[];
      for(let step=0;step<=max;step++){
        await settle();
        const metrics=await inspect();
        assert(metrics.slide===slide&&metrics.state===step,`Deterministic state ${width} ${slide}:${step}`);
        const suffix=max?`-state-${String(step).padStart(2,'0')}`:'';
        const filename=`slide-${String(slide).padStart(2,'0')}${suffix}.png`;
        const screenshot=await browser.screenshot();
        await writeFile(resolve(dir,filename),screenshot);
        if(max&&step===max)await writeFile(resolve(dir,`slide-${String(slide).padStart(2,'0')}.png`),screenshot);
        const pass=!metrics.pageOverflow&&!metrics.collisions.length&&!metrics.headerCollisions.length&&!metrics.outside.length&&!metrics.imageTextCollisions.length&&metrics.text.every(t=>!t.overflow)&&metrics.images.every(i=>i.loaded&&i.embedded)&&metrics.fontLoaded;
        frames.push({screenshot:`output/qa/${width}x${height}/${filename}`,pass,...metrics});
        if(!pass)console.error('VISUAL METRIC FAIL',slide,step,width,{collisions:metrics.collisions,overflow:metrics.text.filter(t=>t.overflow).map(t=>t.text),outside:metrics.outside,imageText:metrics.imageTextCollisions});
        if(max){
          phonePositions.push(metrics.phone);
          const expectedCount=slide===12?[0,1,1,2,2,3][step]:[0,1,1,2,0][step];
          const expectedScreen=slide===12?[1,1,2,2,3,3][step]:[4,4,5,5,5][step];
          assert(metrics.answers.length===expectedCount&&metrics.screenIndex.includes('pantalla '+expectedScreen),`Reveal content ${width} ${slide}:${step}`,{answers:metrics.answers,screen:metrics.screenIndex});
          if(slide===13)assert(metrics.summaryVisible===(step===4),`Full path visibility ${width} ${step}`);
        }
        if(step<max){await browser.key('ArrowRight');advances++;}
      }
      if(max)assert(phonePositions.every(p=>Math.abs(p.x-phonePositions[0].x)<.1&&Math.abs(p.y-phonePositions[0].y)<.1&&Math.abs(p.height-phonePositions[0].height)<.1),`No screen layout shifts ${width} slide ${slide}`);
      if(slide<18){await browser.key('ArrowRight');advances++;}
    }
    assert(advances===26,`Exactly 26 advances from first to final ${width}`,advances);
    await browser.key('ArrowRight');assert((await state()).slide===18,'End boundary');
  }
  await browser.viewport(1920,1080);
  await browser.load(pathToFileURL(resolve(root,'output/deck.html')).href,'.slide.active');
  await go(12);
  for(let n=0;n<5;n++)await browser.key('ArrowRight');
  for(let n=4;n>=0;n--){await browser.key('ArrowLeft');assert((await state()).state===n,'Reverse reveal '+n);}
  await browser.key('ArrowLeft');assert((await state()).slide===11,'Previous slide at first state');
  await browser.key('ArrowRight');assert((await state()).slide===12&&(await state()).state===0,'Reentry reset slide 12');
  await browser.key(' ','Space');assert((await state()).state===1,'Space advances one answer');
  await browser.key('r','KeyR');assert((await state()).state===0,'R resets activity');
  await browser.key('PageDown');assert((await state()).state===1,'PageDown advances one state');
  await browser.key('PageUp');assert((await state()).state===0,'PageUp reverses one state');
  await browser.call('Input.dispatchKeyEvent',{type:'keyDown',key:'ArrowRight',code:'ArrowRight',autoRepeat:true});
  await browser.call('Input.dispatchKeyEvent',{type:'keyUp',key:'ArrowRight',code:'ArrowRight'});
  assert((await state()).state===0,'Held key ignored');
  await click('#next');assert((await state()).state===1,'Next button advances once');
  await browser.key('ArrowLeft');assert((await state()).state===0,'Keyboard after control focus');
  await browser.evaluate('document.activeElement.blur()');
  await browser.call('Input.dispatchMouseEvent',{type:'mousePressed',x:1000,y:950,button:'left',clickCount:1});
  await browser.call('Input.dispatchMouseEvent',{type:'mouseReleased',x:1000,y:950,button:'left',clickCount:1});
  assert((await state()).state===1,'Body click advances once');
  await browser.call('Input.dispatchMouseEvent',{type:'mousePressed',x:1000,y:950,button:'left',clickCount:2});
  await browser.call('Input.dispatchMouseEvent',{type:'mouseReleased',x:1000,y:950,button:'left',clickCount:2});
  assert((await state()).state===1,'Double-click does not skip reveal');
  await go(14);await browser.key('ArrowLeft');assert((await state()).slide===13&&(await state()).state===0,'Reentry reset slide 13');
  await browser.key('End');assert((await state()).slide===18,'End key');
  await browser.key('Home');assert((await state()).slide===1,'Home key');
  await browser.key('ArrowLeft');assert((await state()).slide===1,'Start boundary');
  const before=await state();await click('#fullscreen');await settle();
  assert(await browser.evaluate('Boolean(document.fullscreenElement)'),'Fullscreen API via real click');
  assert((await state()).slide===before.slide,'Fullscreen click does not advance');
  await browser.evaluate('document.exitFullscreen()');await settle();
  assert(!await browser.evaluate('Boolean(document.fullscreenElement)'),'Exit fullscreen');
  await browser.call('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]});
  await go(12);await browser.key('ArrowRight');
  assert(await browser.evaluate('matchMedia("(prefers-reduced-motion: reduce)").matches && document.getAnimations().length===0'),'Reduced motion removes animation');
  assert((await state()).state===1,'Reduced motion preserves reveal ordering');
  await browser.key('Home');
  await browser.call('Emulation.setTouchEmulationEnabled',{enabled:true,maxTouchPoints:1});
  await browser.call('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:1000,y:700}]});
  await browser.call('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:800,y:700}]});
  await browser.call('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
  assert((await state()).slide===2,'Horizontal touch swipe advances once');
  await browser.call('Emulation.setTouchEmulationEnabled',{enabled:false});
  const links=await browser.evaluate('[...document.querySelectorAll("a[href]")].map(a=>a.getAttribute("href"))');
  assert(links.length===0,'No broken or invented presentation links',links);
  const ids=await browser.evaluate('(()=>{const ids=[...document.querySelectorAll("[id]")].map(e=>e.id);return ids.filter((id,i)=>ids.indexOf(id)!==i)})()');
  assert(ids.length===0,'Unique element IDs',ids);
  const external=browser.events.filter(e=>e.method==='Network.requestWillBeSent'&&/^https?:/.test(e.params.request.url)).map(e=>e.params.request.url);
  const errors=browser.events.filter(e=>e.method==='Runtime.exceptionThrown');
  assert(external.length===0,'Zero runtime network requests with offline emulation',external);
  assert(errors.length===0,'No JavaScript exceptions',errors);
  assert(!/<(?:script|link)[^>]+(?:src|href)=["']https?:/i.test(source),'No CDN script or style dependencies');
  assert(!/fntdata/.test(source),'No extracted Gotham fonts in HTML');
  await browser.call('Emulation.setScriptExecutionDisabled',{value:true});
  await browser.call('Page.reload',{ignoreCache:true});
  let staticCheck;
  for(let n=0;n<100;n++){
    staticCheck=await browser.evaluate('({loaded:document.readyState==="complete",js:document.documentElement?.classList.contains("js"),count:document.querySelectorAll(".slide:not([hidden])").length,controls:document.querySelector("#controls")?.hidden,summary:document.querySelector(".discovery-summary")?getComputedStyle(document.querySelector(".discovery-summary")).display:null})');
    if(staticCheck.loaded&&!staticCheck.js)break;
    await new Promise(r=>setTimeout(r,40));
  }
  assert(staticCheck.count===18&&staticCheck.controls&&staticCheck.summary==='none','No-JS document fallback without overlay',staticCheck);
  await browser.call('Emulation.setScriptExecutionDisabled',{value:false});
  await writeFile(resolve(out,'checks.json'),JSON.stringify({browser:execFileSync('chromium-browser',['--version'],{encoding:'utf8'}).trim(),method:'Chromium CDP; DPR 1; offline from before load; fonts.ready + image.decode; actual key/pointer input; all 27 visual states at both viewports',frames,functional,external,errors},null,2));
  console.log(`${frames.length} visual states; ${functional.length} functional assertions; metric failures ${frames.filter(x=>!x.pass).length}; functional failures ${functional.filter(x=>!x.pass).length}`);
  if(frames.some(x=>!x.pass)||functional.some(x=>!x.pass))process.exitCode=1;
}finally{await browser.close();}
