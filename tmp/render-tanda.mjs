import {openBrowser} from './chromium.mjs';
import {writeFile,mkdir} from 'node:fs/promises';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
const root=resolve(import.meta.dirname,'..');
const browser=await openBrowser('sprint-tanda');
const report=[];
try{
  await browser.viewport(390,640,2);
  await browser.call('Network.emulateNetworkConditions',{offline:true,latency:0,downloadThroughput:0,uploadThroughput:0});
  for(let screen=1;screen<=5;screen++){
    await browser.load(pathToFileURL(resolve(root,'assets/content/tanda/mockup.html')).href+'?screen='+screen,'section:not([hidden])');
    const check=await browser.evaluate(`(()=>{const els=[...document.querySelectorAll('section:not([hidden]) *')];return {screen:${screen},text:document.querySelector('section:not([hidden])').innerText,overflow:document.documentElement.scrollHeight>640||document.documentElement.scrollWidth>390,outside:els.filter(e=>{const r=e.getBoundingClientRect();return r.width&&r.height&&(r.bottom>640.5||r.right>390.5||r.x<0||r.y<0)}).map(e=>e.tagName),font:document.fonts.check('400 22px Montserrat')&&document.fonts.check('700 22px Montserrat')};})()`);
    if(check.overflow||check.outside.length||!check.font)throw new Error(JSON.stringify(check));
    await writeFile(resolve(root,`assets/content/tanda/screen-${String(screen).padStart(2,'0')}.png`),await browser.screenshot());
    report.push(check);console.log('Tanda screen',screen,'PASS');
  }
  await mkdir(resolve(root,'output/qa'),{recursive:true});
  await writeFile(resolve(root,'output/qa/tanda-checks.json'),JSON.stringify(report,null,2));
}finally{await browser.close();}
