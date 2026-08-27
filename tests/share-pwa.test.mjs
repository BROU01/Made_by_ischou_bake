import assert from "node:assert/strict";
import { access, readFile } from "node:fs/promises";
import test from "node:test";

const root = new URL("../", import.meta.url);
const read = (name) => readFile(new URL(name, root), "utf8");

test("le manifeste PWA décrit une application installable avec les icônes requises", async () => {
  const manifest = JSON.parse(await read("app.webmanifest"));
  assert.equal(manifest.start_url, "/");
  assert.equal(manifest.display, "standalone");
  assert.equal(manifest.prefer_related_applications, false);
  assert.deepEqual(manifest.icons.map((icon) => icon.sizes), ["192x192", "512x512"]);
  await access(new URL("icons/made-by-ischou-192.png", root));
  await access(new URL("icons/made-by-ischou-512.png", root));
});

test("le partage et la PWA préservent les garde-fous de confidentialité et de compatibilité", async () => {
  const [html, worker] = await Promise.all([read("index.html"), read("sw.js")]);

  assert.match(html, /<link rel="manifest" href="app\.webmanifest">/);
  assert.match(html, /id="siteShare"/);
  assert.match(html, /<button class="site-share" id="siteShare"/);
  assert.match(html, /<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/);
  assert.match(html, /\.site-share svg\{width:16px;height:16px;flex:0 0 16px\}/);
  assert.doesNotMatch(html, /id="siteShare"[^>]*><span aria-hidden="true">↗<\/span>/);
  assert.match(html, /id="cartShare" disabled/);
  assert.match(html, /function validateDelivery\(\)/);
  assert.match(html, /Ajoutez une adresse, un point de repère ou votre position/);
  assert.match(html, /function encodeCartForShare\(\)\{return btoa\(JSON\.stringify\(\{v:1,items:productItems\(\)\.map/);
  assert.match(html, /function decodeSharedCart\(\)/);
  assert.match(html, /history\.replaceState\(\{\},document\.title,`\$\{window\.location\.pathname\}\$\{window\.location\.hash\}`\)/);
  assert.match(html, /beforeinstallprompt/);
  assert.match(html, /Sur iPhone ou iPad/);
  assert.match(html, /navigator\.serviceWorker\.register\("\/sw\.js"\)/);
  assert.match(html, /navigator\.serviceWorker\.getRegistration\("\/sw\.js"\)/);
  assert.match(html, /registration\?\.update\(\)/);
  const encoder = html.slice(html.indexOf("function encodeCartForShare"), html.indexOf("function decodeSharedCart"));
  assert.doesNotMatch(encoder, /customerName|deliveryAddress|orderNote|Position GPS|geo\.url/);
  assert.match(worker, /const SHELL_PATHS/);
  assert.match(worker, /const CACHE_NAME = "made-by-ischou-shell-v2"/);
  assert.match(worker, /event\.request\.method !== "GET"/);
  assert.doesNotMatch(worker, /localStorage|Position GPS|WhatsApp|cart/i);
});
