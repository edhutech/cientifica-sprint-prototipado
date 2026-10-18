import { spawn } from 'node:child_process';
import { once } from 'node:events';

export async function openBrowser(profile = 'sprint-deck') {
  const process = spawn('chromium-browser', ['--headless', '--no-sandbox', '--disable-gpu', '--no-first-run',
    '--remote-debugging-port=0', `--user-data-dir=/tmp/opencode/${profile}`, 'about:blank'], {stdio:['ignore','ignore','pipe']});
  let log = '';
  const endpoint = await new Promise((resolve,reject) => {
    const timer=setTimeout(()=>{process.kill();reject(new Error('Chromium startup timeout'));},30000);
    process.stderr.on('data',chunk=>{log+=chunk;const found=log.match(/DevTools listening on (ws:\/\/\S+)/);if(found){clearTimeout(timer);resolve(found[1]);}});
    process.on('exit',code=>{clearTimeout(timer);reject(new Error(`Browser exited ${code}: ${log}`));});
  });
  const socket=new WebSocket(endpoint); await once(socket,'open');
  let id=0; const pending=new Map(); const events=[];
  socket.addEventListener('message',event=>{
    const message=JSON.parse(event.data);
    if(!message.id){events.push(message);return;}
    const item=pending.get(message.id);if(!item)return;
    clearTimeout(item.timer);pending.delete(message.id);
    message.error?item.reject(new Error(JSON.stringify(message.error))):item.resolve(message.result);
  });
  function send(method,params={},sessionId){return new Promise((resolve,reject)=>{
    const key=++id;const timer=setTimeout(()=>{pending.delete(key);reject(new Error(`CDP timeout ${method}`));},60000);
    pending.set(key,{resolve,reject,timer});socket.send(JSON.stringify({id:key,method,params,...(sessionId?{sessionId}:{})}));
  });}
  const {targetId}=await send('Target.createTarget',{url:'about:blank'});
  const {sessionId}=await send('Target.attachToTarget',{targetId,flatten:true});
  const call=(method,params={})=>send(method,params,sessionId);
  await call('Page.enable');await call('Runtime.enable');await call('Network.enable');
  const evaluate=async(expression)=>{
    const result=await call('Runtime.evaluate',{expression,awaitPromise:true,returnByValue:true});
    if(result.exceptionDetails)throw new Error(JSON.stringify(result.exceptionDetails));
    return result.result.value;
  };
  return {call,evaluate,events,
    async viewport(width,height,dpr=1){await call('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:dpr,mobile:false});},
    async load(url,selector='body'){
      await call('Page.navigate',{url});
      for(let n=0;n<200;n++){
        if(await evaluate(`document.readyState==='complete' && !!document.querySelector(${JSON.stringify(selector)})`))break;
        if(n===199)throw new Error('Page readiness timeout');
        await new Promise(r=>setTimeout(r,40));
      }
      await evaluate(`(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(im=>im.decode()));await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));return true;})()`);
    },
    async screenshot(){const {data}=await call('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});return Buffer.from(data,'base64');},
    async key(key,code=key){await call('Input.dispatchKeyEvent',{type:'keyDown',key,code});await call('Input.dispatchKeyEvent',{type:'keyUp',key,code});},
    async close(){await send('Browser.close').catch(()=>{});socket.close();process.kill();}
  };
}
