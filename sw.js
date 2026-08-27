const CACHE_NAME = "made-by-ischou-shell-v2";
const SHELL_PATHS = [
  "/",
  "/index.html",
  "/app.webmanifest",
  "/favicon.svg",
  "/logo.svg",
  "/icons/made-by-ischou-192.png",
  "/icons/made-by-ischou-512.png",
];

self.addEventListener("install", (event) => {
  event.waitUntil(caches.open(CACHE_NAME).then((cache) => cache.addAll(SHELL_PATHS)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (event) => {
  event.waitUntil(caches.keys().then((keys) => Promise.all(keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key)))).then(() => self.clients.claim()));
});

self.addEventListener("fetch", (event) => {
  if (event.request.method !== "GET") return;
  const url = new URL(event.request.url);
  if (url.origin !== self.location.origin) return;
  const isNavigation = event.request.mode === "navigate";
  const isShell = isNavigation || SHELL_PATHS.includes(url.pathname);
  if (!isShell) return;
  event.respondWith(fetch(event.request).then((response) => {
    if (response && response.ok) caches.open(CACHE_NAME).then((cache) => cache.put(event.request, response.clone()));
    return response;
  }).catch(() => caches.match(event.request).then((cached) => cached || caches.match(isNavigation ? "/index.html" : "/"))));
});
