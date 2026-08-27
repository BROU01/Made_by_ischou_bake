import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const root = new URL("../", import.meta.url);
const read = (name) => readFile(new URL(name, root), "utf8");

test("le panneau reprend les parcours utiles de la référence sans données de démonstration", async () => {
  const html = await read("adminrootonly/index.html");

  for (const section of ["dashboard", "catalogue", "analytics", "journal"]) {
    assert.match(html, new RegExp(`data-tab="${section}"`));
    assert.match(html, new RegExp(`id="${section}Panel"`));
  }
  assert.match(html, /id="catalogueSearch"/);
  assert.match(html, /id="familyFilter"/);
  assert.match(html, /id="productDialog"/);
  assert.match(html, /Les données clients ne sont jamais collectées sans accord explicite/);
  assert.match(html, /Une ouverture de WhatsApp indique une intention, jamais une commande/);
  assert.doesNotMatch(html, /1\s*284\s*500|Chiffre d'affaires|données de démonstration|Paiement refusé/);
});

test("l’éditeur de produit appelle uniquement la route admin protégée et échappe les données affichées", async () => {
  const script = await read("adminrootonly/admin.js");

  assert.match(script, /function escapeHtml/);
  assert.match(script, /request\("\/api\/admin\/catalog", \{ method:"PATCH"/);
  assert.match(script, /credentials:"same-origin"/);
  assert.match(script, /await request\("\/api\/admin\/session", \{ method:"DELETE"/);
  assert.doesNotMatch(script, /localStorage\.setItem\([^\n]*token|firebase.*firestore/i);
});

test("la navigation latérale reste utilisable sur mobile sans dépendre d’icônes emoji", async () => {
  const [html, css] = await Promise.all([read("adminrootonly/index.html"), read("adminrootonly/admin.css")]);

  assert.match(html, /id="sidebarToggle"/);
  assert.match(html, /<svg viewBox="0 0 24 24" aria-hidden="true">/);
  assert.match(css, /\.sidebar\.open\{transform:none\}/);
  assert.match(css, /\.sidebar-backdrop\.show\{display:block\}/);
  assert.doesNotMatch(html, /[📈📊🛒💬✨🚀]/u);
});
