import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const htmlPath = new URL("../index.html", import.meta.url);

test("le parcours de géolocalisation préserve consentement, secours et compatibilité iPhone", async () => {
  const html = await readFile(htmlPath, "utf8");

  assert.match(html, /id="geoButton">Partager ma position pour la livraison/);
  assert.match(html, /id="geoIosHelp" class="geo-ios-help" hidden/);
  assert.match(html, /Autoriser la localisation sur iPhone/);
  assert.match(html, /Réglages iPhone → Confidentialité et sécurité → Service de localisation/);
  assert.match(html, /Sites web Safari/);
  assert.match(html, /function setIOSPermissionHelp\(show\)\{const visible=Boolean\(show&&isIOS\)/);
  assert.match(html, /setIOSPermissionHelp\(error\.code===1\)/);
  assert.match(html, /setIOSPermissionHelp\(false\);const coordinates=/);
  assert.match(html, /id="geoMapLink" class="geo-map-link"[^>]*target="_blank" rel="noopener noreferrer" hidden/);
  assert.match(html, /const isIOS=\/iPad\|iPhone\|iPod\//);
  assert.match(html, /const isEmbeddedIOS=\//);
  assert.match(html, /https:\/\/maps\.apple\.com\/place\?coordinate=/);
  assert.match(html, /retryable=\(error\.code===2\|\|error\.code===3\)&&!retried/);
  assert.match(html, /maximumAge:60000/);
  assert.match(html, /La localisation n’a pas été autorisée/);
  assert.match(html, /Ouvrez le site dans Safari/i);
  assert.match(html, /geo=null;hideGeoMapLink\(\)/);
  assert.doesNotMatch(html, /localStorage\.(?:setItem|getItem)\([^)]*geo/i);
});
