const admin = require("firebase-admin");
const { AdminAccessError, cookieValue, emailIsAllowed } = require("./_security");

const SESSION_NAME = "made_by_ischou_admin_session";
const SESSION_DURATION_MS = 1000 * 60 * 60 * 24 * 5;

function requiredEnv(name) {
  const value = process.env[name];
  if (!value) throw new AdminAccessError(503, "ADMIN_NOT_CONFIGURED", "La Preview sécurisée n’est pas encore configurée.");
  return value;
}

function serviceAccount() {
  return {
    projectId: requiredEnv("FIREBASE_PROJECT_ID"),
    clientEmail: requiredEnv("FIREBASE_CLIENT_EMAIL"),
    privateKey: requiredEnv("FIREBASE_PRIVATE_KEY").replace(/\\n/g, "\n"),
  };
}

function firebaseApp() {
  if (!admin.apps.length) {
    admin.initializeApp({ credential: admin.credential.cert(serviceAccount()) });
  }
  return admin.app();
}

function assertAdminToken(decodedToken) {
  if (!decodedToken?.email || decodedToken.email_verified !== true || !emailIsAllowed(decodedToken.email)) {
    throw new AdminAccessError(403, "ADMIN_REQUIRED", "Ce compte ne possède pas l’accès administrateur requis.");
  }
  return decodedToken;
}

async function requireAdminSession(req) {
  const sessionCookie = cookieValue(req, SESSION_NAME);
  if (!sessionCookie) throw new AdminAccessError(401, "SESSION_REQUIRED", "La session administrateur a expiré. Reconnectez-vous.");
  const decoded = await admin.auth(firebaseApp()).verifySessionCookie(sessionCookie, true);
  return assertAdminToken(decoded);
}

async function createAdminSession(idToken) {
  const auth = admin.auth(firebaseApp());
  const decoded = await auth.verifyIdToken(idToken, true);
  assertAdminToken(decoded);
  const sessionCookie = await auth.createSessionCookie(idToken, { expiresIn: SESSION_DURATION_MS });
  return { sessionCookie, decoded };
}

function setSessionCookie(res, value) {
  res.setHeader("Set-Cookie", `${SESSION_NAME}=${encodeURIComponent(value)}; Path=/api/admin; HttpOnly; Secure; SameSite=Strict; Max-Age=${Math.floor(SESSION_DURATION_MS / 1000)}`);
}

function clearSessionCookie(res) {
  res.setHeader("Set-Cookie", `${SESSION_NAME}=; Path=/api/admin; HttpOnly; Secure; SameSite=Strict; Max-Age=0`);
}

function firestore() {
  firebaseApp();
  return admin.firestore();
}

module.exports = {
  clearSessionCookie,
  createAdminSession,
  firestore,
  requireAdminSession,
  setSessionCookie,
};
