class AdminAccessError extends Error {
  constructor(status, code, message) {
    super(message);
    this.name = "AdminAccessError";
    this.status = status;
    this.code = code;
  }
}

function allowedEmails(raw = process.env.ADMIN_ALLOWED_EMAILS || "") {
  return new Set(raw.split(",").map((entry) => entry.trim().toLowerCase()).filter(Boolean));
}

function emailIsAllowed(email, raw) {
  return typeof email === "string" && allowedEmails(raw).has(email.trim().toLowerCase());
}

function parseJsonBody(req) {
  if (!req.body) return {};
  if (typeof req.body === "object") return req.body;
  try {
    return JSON.parse(req.body);
  } catch {
    throw new AdminAccessError(400, "INVALID_JSON", "Le format de la requête est invalide.");
  }
}

function requireSameOrigin(req) {
  const origin = req.headers.origin;
  if (!origin) return;
  const host = req.headers["x-forwarded-host"] || req.headers.host;
  const protocol = String(req.headers["x-forwarded-proto"] || "https").split(",")[0].trim();
  if (!host || origin !== `${protocol}://${host}`) {
    throw new AdminAccessError(403, "ORIGIN_REJECTED", "Cette origine n’est pas autorisée.");
  }
}

function bearerToken(req) {
  const authorization = req.headers.authorization || "";
  const match = /^Bearer\s+(.+)$/i.exec(authorization);
  if (!match) throw new AdminAccessError(401, "TOKEN_REQUIRED", "Une authentification est requise.");
  return match[1];
}

function cookieValue(req, key) {
  const source = req.headers.cookie || "";
  const pair = source.split(";").map((part) => part.trim()).find((part) => part.startsWith(`${key}=`));
  return pair ? decodeURIComponent(pair.slice(key.length + 1)) : null;
}

function noStore(res) {
  res.setHeader("Cache-Control", "no-store, max-age=0");
}

function sendError(res, error) {
  const status = error instanceof AdminAccessError ? error.status : 500;
  const code = error instanceof AdminAccessError ? error.code : "SERVER_ERROR";
  if (status >= 500) console.error("[admin]", error);
  noStore(res);
  return res.status(status).json({ error: code, message: status >= 500 ? "Le service est momentanément indisponible." : error.message });
}

module.exports = {
  AdminAccessError,
  allowedEmails,
  bearerToken,
  cookieValue,
  emailIsAllowed,
  noStore,
  parseJsonBody,
  requireSameOrigin,
  sendError,
};
