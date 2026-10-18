import {openBrowser} from './chromium.mjs';
import {mkdir,writeFile} from 'node:fs/promises';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
const root=resolve(import.meta.dirname,'..');const b=await openBrowser('sprint-revision');const frames=[];
try{
 await b.call('Network.emulateNetworkConditions',{offline:true,latency:0,downloadThroughput:0,uploadThroughput:0});
 for(const [width,height] of [[1920,1080],[1366,768]]){
  const dir=resolve(root,`output/qa/revision/${width}x${height}`);await mkdir(dir,{recursive:true});await b.viewport(width,height);
  await b.load(pathToFileURL(resolve(root,'output/deck.html')).href,'.slide.active');
  for(let n=1;n<=22;n++){
   const max=await b.evaluate('Number(document.querySelector(".slide.active").dataset.maxState)');
   for(let state=0;state<=max;state++){
    await b.evaluate('(async()=>{await Promise.all(document.getAnimations().map(a=>a.finished));return true})()');
    const result=await b.evaluate(`(()=>{const s=document.querySelector('.slide.active');const visible=e=>e.getClientRects().length&&!e.closest('[hidden]');const els=[...s.querySelectorAll('[data-text]')].filter(visible);const rect=e=>e.getBoundingClientRect();const errors=[];for(const e of els){const r=rect(e);if(r.x<0||r.y<0||r.right>innerWidth+1||r.bottom>innerHeight+1||e.scrollWidth>e.clientWidth+2||e.scrollHeight>e.clientHeight+2)errors.push('overflow '+e.textContent)}for(let i=0;i<els.length;i++)for(let j=i+1;j<els.length;j++){const a=rect(els[i]),c=rect(els[j]);if(a.x<c.right-1&&a.right>c.x+1&&a.y<c.bottom-1&&a.bottom>c.y+1)errors.push('overlap '+els[i].textContent+' / '+els[j].textContent)}return {id:s.id,slide:Number(document.body.dataset.slide),state:Number(document.body.dataset.state),errors,images:[...s.querySelectorAll('img')].every(i=>i.complete&&i.naturalWidth),font:document.fonts.check('700 40px Montserrat')};})()`);
    if(result.slide!==n||result.state!==state||!result.images||!result.font)throw Error(JSON.stringify(result));
    const shot=await b.screenshot();await writeFile(resolve(dir,`slide-${String(n).padStart(2,'0')}${max?'-state-'+state:''}.png`),shot);
    if(state===max)await writeFile(resolve(dir,`slide-${String(n).padStart(2,'0')}.png`),shot);
    frames.push({width,height,...result});if(result.errors.length)console.log(result);
    if(state<max){await b.key('ArrowRight');await b.key('ArrowLeft');if(await b.evaluate('Number(document.body.dataset.state)')!==state)throw Error('Reverse failed');await b.key('ArrowRight');}
   }
   if(n<22)await b.key('ArrowRight');
  }
 }
 const links=await b.evaluate('[...document.querySelectorAll("a")].map(a=>a.href)');
 await b.key('Home');if(await b.evaluate('document.body.dataset.slide')!=='1')throw Error('Home');await b.key('End');if(await b.evaluate('document.body.dataset.slide')!=='22')throw Error('End');
 const errors=b.events.filter(e=>e.method==='Runtime.exceptionThrown');const requests=b.events.filter(e=>e.method==='Network.requestWillBeSent'&&/^https?:/.test(e.params.request.url));
 await writeFile(resolve(root,'output/qa/revision/checks.json'),JSON.stringify({frames,links,errors,requests},null,2));
 console.log(`${frames.length} states; ${frames.filter(f=>f.errors.length).length} layout failures; ${errors.length} JS errors; ${requests.length} network requests`);
}finally{await b.close()}
