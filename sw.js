/* Urban Sentinel PWA: offline static shell only. Private portal and customer data are NEVER cached. */
const CACHE='us-static-no-feedback-20261120';
const PRECACHE=['./','./index.html','./3d-simulation.html','./manifest.webmanifest',
 './assets/css/style.css','./assets/css/3d-simulation.css','./assets/js/main.js',
 './assets/js/3d-simulation.js','./assets/js/simulation-design.js',
 './assets/icons/urban-sentinel-192.png','./assets/icons/urban-sentinel-512.png'];
self.addEventListener('install',event=>{event.waitUntil(caches.open(CACHE).then(async cache=>{
 await Promise.allSettled(PRECACHE.map(p=>cache.add(p)));
 self.skipWaiting();
}))});
self.addEventListener('activate',event=>{event.waitUntil(Promise.all([
 caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith('us-static-')&&k!==CACHE).map(k=>caches.delete(k)))),
 self.clients.claim()
]))});
self.addEventListener('fetch',event=>{
 const req=event.request;
 if(req.method!=='GET'||new URL(req.url).origin!==location.origin)return;
 const url=new URL(req.url);const path=url.pathname;
 // No caching of any backend call, contractor sessions, owner pages or contact/referral forms.
 if(path.includes('/backend/')||/(?:access|account|business-workspace|marketplace|privacy)\.html$/i.test(path)||path.endsWith('.php'))return;
 const isStatic=/\/(?:assets\/.*\.(?:js|css|png|webp|svg)|manifest\.webmanifest)$/i.test(path);
 if(isStatic){event.respondWith(caches.match(req).then(hit=>hit||fetch(req).then(resp=>{
 if(resp.ok){const copy=resp.clone();caches.open(CACHE).then(cache=>cache.put(req,copy))}return resp;
 })));return;}
 if(/\/(?:|index\.html|3d-simulation\.html)$/i.test(path)){
 event.respondWith(fetch(req).catch(()=>caches.match(req).then(hit=>hit||caches.match('./index.html'))));
 }
});
