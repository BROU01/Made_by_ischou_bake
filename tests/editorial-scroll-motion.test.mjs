import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const htmlPath = new URL("../index.html", import.meta.url);

test("la motion éditoriale conserve ses garde-fous de performance et d’accessibilité", async () => {
  const html = await readFile(htmlPath, "utf8");

  assert.match(html, /function initEditorialScroll\(\)/);
  assert.match(html, /IntersectionObserver\(entries=>\{entries\.forEach\(entry=>\{if\(entry\.isIntersecting\)active\.add/);
  assert.match(html, /window\.addEventListener\("scroll",schedule,\{passive:true\}\)/);
  assert.match(html, /requestAnimationFrame\(update\)/);
  assert.match(html, /prefers-reduced-motion: reduce\), \(max-width: 960px\)/);
  assert.match(html, /data-chapter="01"/);
  assert.match(html, /data-chapter="02"/);
  assert.match(html, /data-chapter="03"/);
  assert.match(html, /data-chapter="04"/);
  assert.match(html, /data-depth="14"/);
  assert.match(html, /data-depth="11"/);
  assert.doesNotMatch(html, /setInterval\(/);
});
