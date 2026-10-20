// Офлайн після першого завантаження: кешуємо оболонку застосунку і дані.
const CACHE = 'perekaz-v8';
const ASSETS = [
  './',
  'index.html',
  'css/app.css',
  'js/app.js',
  'js/normalize.js',
  'js/store.js',
  'js/speech.js',
  'data/works.json',
  'data/works/happy-prince/scenes.json',
  'data/works/happy-prince/characters.json',
  'data/works/painted-fox/scenes.json',
  'data/works/painted-fox/characters.json',
  'manifest.webmanifest',
  'images/icon.svg',
  'images/map.svg',
  'images/backdrop.svg',
  'images/prince.svg',
  'images/mayor.svg',
  'images/swallow.svg',
  'images/reed.svg',
  'images/seamstress.svg',
  'images/matchgirl.svg',
  'images/angel.svg',
  'images/prince-cry.svg',
  'images/swallow-sad.svg',
  'images/swallow-cold.svg',
  'images/matchgirl-happy.svg',
  'images/seamstress-happy.svg',
  'images/mayor-angry.svg',
  'images/items/gold.svg',
  'images/items/sapphire.svg',
  'images/items/ruby.svg',
  'images/items/matches.svg',
  'images/items/oranges.svg',
  'images/items/heart.svg',
  'images/items/deadswallow.svg',
  'images/items/bread.svg',
  'images/items/stones.svg',
  'images/items/rain.svg',
  'images/items/fire.svg',
  'images/items/light.svg',
  'images/bg/river.svg',
  'images/bg/room.svg',
  'images/bg/winter.svg',
  'images/bg/sky.svg',
  'images/painted-fox/barrel.svg',
  'images/painted-fox/bear.svg',
  'images/painted-fox/crown.svg',
  'images/painted-fox/dog.svg',
  'images/painted-fox/forest.svg',
  'images/painted-fox/fox-blue.svg',
  'images/painted-fox/fox-howl.svg',
  'images/painted-fox/fox-king.svg',
  'images/painted-fox/fox.svg',
  'images/painted-fox/glade.svg',
  'images/painted-fox/hen.svg',
  'images/painted-fox/market.svg',
  'images/painted-fox/notes.svg',
  'images/painted-fox/stump.svg',
  'images/painted-fox/wolf.svg',
];

self.addEventListener('install', (event) => {
  event.waitUntil(caches.open(CACHE).then((cache) => cache.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((key) => key !== CACHE).map((key) => caches.delete(key))))
      .then(() => self.clients.claim()),
  );
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);
  // Шрифти Google не кешуємо тут: якщо їх немає, застосунок працює системними шрифтами.
  if (url.origin !== self.location.origin) return;
  event.respondWith(
    caches.match(event.request).then((cached) => cached || fetch(event.request).then((response) => {
      if (response.ok) {
        const copy = response.clone();
        caches.open(CACHE).then((cache) => cache.put(event.request, copy));
      }
      return response;
    })),
  );
});
