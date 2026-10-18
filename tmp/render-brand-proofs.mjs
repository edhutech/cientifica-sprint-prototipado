// Native Chromium DevTools Protocol: exact CSS viewports, loaded fonts, no dependencies.
import { spawn, execFileSync } from 'node:child_process';
import { mkdir, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { once } from 'node:events';

const root = resolve(import.meta.dirname, '..');
const out = resolve(root, 'output/brand-proof');
await mkdir(out, { recursive: true });
const browser = spawn('chromium-browser', [
  '--headless', '--no-sandbox', '--disable-gpu', '--no-first-run',
  '--remote-debugging-port=0', '--user-data-dir=/tmp/opencode/proto-brand-proof-cdp', 'about:blank',
], { stdio: ['ignore', 'ignore', 'pipe'] });
let log = '';
const endpoint = await new Promise((res, rej) => {
  const timeout = setTimeout(() => rej(new Error('Chromium startup timed out')), 30000);
  browser.stderr.on('data', chunk => {
    log += chunk;
    const match = log.match(/DevTools listening on (ws:\/\/[^\s]+)/);
    if (match) { clearTimeout(timeout); res(match[1]); }
  });
  browser.on('exit', code => { clearTimeout(timeout); rej(new Error(`Chromium exited ${code}: ${log}`)); });
});
const ws = new WebSocket(endpoint);
await once(ws, 'open');
let sequence = 0;
const pending = new Map();
const errors = [];
ws.addEventListener('message', event => {
  const message = JSON.parse(event.data);
  if (message.method === 'Runtime.exceptionThrown') errors.push(message.params);
  if (!message.id) return;
  const item = pending.get(message.id);
  if (!item) return;
  pending.delete(message.id);
  clearTimeout(item.timer);
  if (message.error) item.reject(new Error(JSON.stringify(message.error)));
  else item.resolve(message.result);
});
function cdp(method, params = {}, sessionId) {
  return new Promise((resolve, reject) => {
    const id = ++sequence;
    const timer = setTimeout(() => { pending.delete(id); reject(new Error(`CDP timeout: ${method}`)); }, 45000);
    pending.set(id, { resolve, reject, timer });
    ws.send(JSON.stringify({ id, method, params, ...(sessionId ? { sessionId } : {}) }));
  });
}
const results = [];
try {
  const { targetId } = await cdp('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await cdp('Target.attachToTarget', { targetId, flatten: true });
  const call = (method, params = {}) => cdp(method, params, sessionId);
  await call('Page.enable');
  await call('Runtime.enable');
  await call('Network.enable');
  await call('Network.emulateNetworkConditions', { offline: true, latency: 0, downloadThroughput: 0, uploadThroughput: 0 });
  for (const layout of ['a', 'c']) {
    for (const [width, height] of [[1920, 1080], [1366, 768]]) {
      await call('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile: false });
      await call('Page.navigate', { url: pathToFileURL(resolve(root, `tmp/brand-proof-${layout}.html`)).href });
      // Page readiness is polled through CDP, not assumed from a fixed screenshot delay.
      let ready = false;
      for (let i = 0; i < 100; i++) {
        const check = await call('Runtime.evaluate', { expression: 'document.readyState === "complete" && !!document.querySelector(".canvas")', returnByValue: true });
        if (check.result.value) { ready = true; break; }
        await new Promise(resolve => setTimeout(resolve, 50));
      }
      if (!ready) throw new Error('Page did not load');
      const evaluation = await call('Runtime.evaluate', { awaitPromise: true, returnByValue: true, expression: `(async () => {
        await document.fonts.ready;
        await Promise.all([...document.images].map(image => image.decode()));
        await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
        const box = element => {
          const {x,y,width,height,right,bottom} = element.getBoundingClientRect();
          return {x,y,width,height,right,bottom};
        };
        const overlaps = (a,b) => a.x < b.right - 0.5 && a.right > b.x + 0.5 && a.y < b.bottom - 0.5 && a.bottom > b.y + 0.5;
        const canvas = document.querySelector('.canvas');
        const stage = box(canvas);
        const text = [...document.querySelectorAll('[data-text]')].map(element => ({
          id: element.id, text: element.textContent, box: box(element),
          fontSize: getComputedStyle(element).fontSize,
          fontFamily: getComputedStyle(element).fontFamily,
          overflow: element.scrollWidth > element.clientWidth + 1 || element.scrollHeight > element.clientHeight + 1,
        }));
        const collisions = [];
        text.forEach((a,i) => text.slice(i+1).forEach(b => { if (overlaps(a.box,b.box)) collisions.push([a.id,b.id]); }));
        const outOfCanvas = text.filter(t => t.box.x < stage.x - 1 || t.box.right > stage.right + 1 || t.box.y < stage.y - 1 || t.box.bottom > stage.bottom + 1).map(t => t.id);
        const reserved = canvas.dataset.layout === 'A'
          ? [{id:'photo-and-integrated-logos', x:stage.x+stage.width/2,y:stage.y,right:stage.right,bottom:stage.bottom}]
          : [{id:'institutional-header', ...box(document.querySelector('header'))}];
        const reservedCollisions = text.flatMap(t => reserved.filter(zone => overlaps(t.box,zone)).map(zone => [t.id,zone.id]));
        const elements = Object.fromEntries([...document.querySelectorAll('[id]')].map(el => [el.id,box(el)]));
        return {
          viewport: {width:innerWidth,height:innerHeight}, canvas:stage, text, elements,
          fontsLoaded: document.fonts.check('400 36px "Proof Montserrat"') && document.fonts.check('700 36px "Proof Montserrat"'),
          images: [...document.images].map(im => ({loaded:im.complete&&im.naturalWidth>0,width:im.naturalWidth,height:im.naturalHeight, embedded:im.currentSrc.startsWith('data:')})),
          collisions, reservedCollisions, outOfCanvas,
          pageOverflow: document.documentElement.scrollWidth>innerWidth || document.documentElement.scrollHeight>innerHeight,
        };
      })()` });
      if (evaluation.exceptionDetails) throw new Error(JSON.stringify(evaluation.exceptionDetails));
      const metrics = evaluation.result.value;
      const { data } = await call('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
      const filename = `layout-${layout}-${width}x${height}.png`;
      await writeFile(resolve(out, filename), Buffer.from(data, 'base64'));
      const pass = metrics.fontsLoaded && metrics.images.every(i => i.loaded && i.embedded) && !metrics.pageOverflow
        && !metrics.collisions.length && !metrics.reservedCollisions.length && !metrics.outOfCanvas.length && metrics.text.every(t => !t.overflow);
      results.push({layout:layout.toUpperCase(), screenshot:filename, pass, ...metrics});
      console.log(filename, pass ? 'PASS' : 'FAIL');
    }
  }
  await writeFile(resolve(out, 'composition-checks.json'), JSON.stringify({
    browser:execFileSync('chromium-browser', ['--version'], {encoding:'utf8'}).trim(),
    method:'CDP, deviceScaleFactor=1, offline network, fonts.ready and image.decode before capture',
    errors, results,
  }, null, 2) + '\n');
  if (errors.length || results.some(r => !r.pass)) process.exitCode = 1;
} finally {
  await writeFile(resolve(root, 'tmp/brand-proof-browser.log'), log);
  await cdp('Browser.close').catch(() => {});
  ws.close();
  browser.kill();
}
