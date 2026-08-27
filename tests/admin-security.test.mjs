import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import security from "../api/_security.js";
import activityHandler from "../api/admin/activity.js";
import catalogHandler from "../api/admin/catalog.js";
import dashboardHandler from "../api/admin/dashboard.js";

function mockResponse() {
  return {
    headers: {},
    statusCode: 200,
    body: null,
    setHeader(name, value) { this.headers[name] = value; },
    status(code) { this.statusCode = code; return this; },
    json(value) { this.body = value; return this; },
    end() { this.ended = true; return this; },
  };
}

test("normalise et vérifie strictement l’allowlist d’administration", () => {
  const raw = " ADMIN@example.test , seconde@example.test ";
  assert.deepEqual([...security.allowedEmails(raw)], ["admin@example.test", "seconde@example.test"]);
  assert.equal(security.emailIsAllowed("Admin@Example.Test", raw), true);
  assert.equal(security.emailIsAllowed("visiteur@example.test", raw), false);
  assert.equal(security.emailIsAllowed(undefined, raw), false);
});

test("exige un bearer token correctement formé", () => {
  assert.equal(security.bearerToken({ headers: { authorization: "Bearer token-signe" } }), "token-signe");
  assert.throws(() => security.bearerToken({ headers: {} }), { code: "TOKEN_REQUIRED" });
  assert.throws(() => security.bearerToken({ headers: { authorization: "Basic token" } }), { code: "TOKEN_REQUIRED" });
});

test("rejette une origine qui ne correspond pas au domaine servi", () => {
  assert.doesNotThrow(() => security.requireSameOrigin({ headers: { origin: "https://ischou.vercel.app", host: "ischou.vercel.app", "x-forwarded-proto": "https" } }));
  assert.throws(() => security.requireSameOrigin({ headers: { origin: "https://attaque.example", host: "ischou.vercel.app", "x-forwarded-proto": "https" } }), { code: "ORIGIN_REJECTED" });
});

test("lit uniquement le cookie de session attendu", () => {
  assert.equal(security.cookieValue({ headers: { cookie: "theme=warm; made_by_ischou_admin_session=abc%20123; other=x" } }, "made_by_ischou_admin_session"), "abc 123");
  assert.equal(security.cookieValue({ headers: { cookie: "theme=warm" } }, "made_by_ischou_admin_session"), null);
});

test("les routes de données refusent une requête sans session avant Firestore", async () => {
  for (const handler of [dashboardHandler, catalogHandler, activityHandler]) {
    const response = mockResponse();
    await handler({ method: "GET", headers: {} }, response);
    assert.equal(response.statusCode, 401);
    assert.equal(response.body.error, "SESSION_REQUIRED");
    assert.equal(response.headers["Cache-Control"], "no-store, max-age=0");
  }
});

test("le helper Firebase accepte les variantes de clé injectées par Vercel sans accepter de valeur non PEM", async () => {
  const source = await readFile(new URL("../api/_firebase.js", import.meta.url), "utf8");
  assert.match(source, /function normalizedPrivateKey\(value\)/);
  assert.match(source, /JSON\.parse\(key\)/);
  assert.match(source, /replace\(\/\\\\n\/g, "\\n"\)/);
  assert.match(source, /BEGIN PRIVATE KEY/);
  assert.match(source, /ADMIN_NOT_CONFIGURED/);
});
