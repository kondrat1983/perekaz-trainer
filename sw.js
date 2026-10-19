// Офлайн після першого завантаження: кешуємо оболонку застосунку і дані.
const CACHE = 'perekaz-v2';
const ASSETS = [
  './',
  'index.html',
  'css/app.css',
  'js/app.js',
  'js/normalize.js',
  'js/store.js',
  'js/speech.js',
  'data/scenes.json',
  'data/characters.json',
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
