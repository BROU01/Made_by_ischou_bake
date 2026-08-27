const accessCard = document.querySelector("#accessCard");
const adminApp = document.querySelector("#adminApp");
const accessStatus = document.querySelector("#accessStatus");
const appNotice = document.querySelector("#appNotice");
const loginForm = document.querySelector("#loginForm");
const loginButton = document.querySelector("#loginButton");
const emailField = document.querySelector("#email");
const emailStorageKey = "made_by_ischou_admin_login_email";
let auth;

function setStatus(target, message = "", type = "") { target.textContent = message; target.className = `status${type ? ` ${type}` : ""}`; }
function setNotice(message = "", type = "") { appNotice.textContent = message; appNotice.className = `notice${type ? ` ${type}` : ""}`; }
function money(value) { return `${Number(value).toLocaleString("fr-FR")} F`; }
function humanDate(value) { if (!value) return "À l’instant"; const date = value._seconds ? new Date(value._seconds * 1000) : new Date(value); return Number.isNaN(date.valueOf()) ? "À l’instant" : date.toLocaleString("fr-FR", { dateStyle: "medium", timeStyle: "short" }); }

async function request(path, options = {}) {
  const response = await fetch(path, { credentials: "same-origin", headers: { "Content-Type": "application/json", ...(options.headers || {}) }, ...options });
  if (response.status === 204) return null;
  const data = await response.json().catch(() => ({}));
  if (!response.ok) throw new Error(data.message || "La requête n’a pas abouti.");
  return data;
}

async function setupFirebase() {
  const config = await request("/api/admin/config");
  const { initializeApp } = await import("https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js");
  const authModule = await import("https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js");
  auth = authModule.getAuth(initializeApp(config));
  return authModule;
}

function showApp() { accessCard.hidden = true; adminApp.hidden = false; }
function showAccess() { adminApp.hidden = true; accessCard.hidden = false; }

function renderActivity(entries, target) {
  if (!entries?.length) { target.innerHTML = '<p class="empty">Aucune modification n’a encore été enregistrée.</p>'; return; }
  target.innerHTML = entries.map((entry) => `<div class="activity-item"><div><strong>${entry.action.replaceAll("_", " ")}</strong><span>${entry.targetType || "activité"}${entry.targetId ? ` · ${entry.targetId}` : ""}</span></div><span>${humanDate(entry.createdAt)}</span></div>`).join("");
}

function renderKpis(data) {
  const entries = [["Références catalogue",data.products,"Produits et formules."],["Commandes consenties",data.orders,"Aucune conversation WhatsApp."],["Médias administrés",data.media,"Bibliothèque future."],["Réglages enregistrés",data.settings,"Informations boutique."]];
  document.querySelector("#kpis").innerHTML = entries.map(([label,value,detail]) => `<article class="kpi"><span>${label}</span><strong>${value}</strong><small>${detail}</small></article>`).join("");
}

function renderCatalogue(products) {
  const target = document.querySelector("#catalogue");
  if (!products?.length) { target.innerHTML = '<p class="empty">Le catalogue de préproduction est vide. Utilisez « Initialiser le catalogue » pour enregistrer les 17 références validées.</p>'; return; }
  target.innerHTML = products.map((product) => `<article class="product-row"><span>${product.family === "pastel-offer" ? "Formule" : product.family}</span><strong>${product.name}</strong><b>${product.isEstimatedPrice ? "À partir de " : ""}${money(product.price)}</b><small>${product.isActive ? "Visible" : "Masqué"}</small></article>`).join("");
}

async function loadDashboard() {
  const data = await request("/api/admin/dashboard");
  renderKpis(data); renderActivity(data.recentActivity, document.querySelector("#recentActivity"));
}
async function loadCatalogue() { renderCatalogue(await request("/api/admin/catalog")); }
async function loadActivity() { renderActivity(await request("/api/admin/activity"), document.querySelector("#activity")); }
async function loadAll() { await Promise.all([loadDashboard(), loadCatalogue(), loadActivity()]); }

function activateTab(name) {
  document.querySelectorAll(".tab").forEach((tab) => tab.classList.toggle("active", tab.dataset.tab === name));
  document.querySelectorAll(".panel-view").forEach((panel) => { panel.hidden = panel.id !== `${name}Panel`; });
}

async function completeMagicLink(authModule) {
  if (!authModule.isSignInWithEmailLink(auth, window.location.href)) return false;
  const email = localStorage.getItem(emailStorageKey) || window.prompt("Confirmez l’adresse e-mail utilisée pour recevoir ce lien :");
  if (!email) throw new Error("L’adresse e-mail est nécessaire pour finaliser la connexion.");
  setStatus(accessStatus, "Vérification sécurisée du lien…");
  const credential = await authModule.signInWithEmailLink(auth, email, window.location.href);
  const idToken = await credential.user.getIdToken(true);
  await request("/api/admin/session", { method: "POST", headers: { Authorization: `Bearer ${idToken}` } });
  localStorage.removeItem(emailStorageKey);
  await authModule.signOut(auth);
  history.replaceState({}, document.title, "/adminrootonly/");
  return true;
}

async function boot() {
  try {
    const authModule = await setupFirebase();
    const linkCompleted = await completeMagicLink(authModule);
    const session = await request("/api/admin/session").catch(() => null);
    if (!session) { showAccess(); if (linkCompleted) setStatus(accessStatus, "Connexion validée. Le tableau de bord est prêt.", "success"); return; }
    showApp(); await loadAll();
  } catch (error) { showAccess(); setStatus(accessStatus, error.message || "La connexion n’a pas abouti.", "error"); }
}

loginForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  const email = emailField.value.trim();
  if (!emailField.checkValidity()) { setStatus(accessStatus, "Saisissez une adresse e-mail valide.", "error"); emailField.focus(); return; }
  try {
    loginButton.disabled = true; setStatus(accessStatus, "Préparation du lien sécurisé…");
    const { sendSignInLinkToEmail } = await import("https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js");
    await sendSignInLinkToEmail(auth, email, { url: `${window.location.origin}/adminrootonly/`, handleCodeInApp: true });
    localStorage.setItem(emailStorageKey, email);
    setStatus(accessStatus, "Lien envoyé. Ouvrez-le depuis votre boîte e-mail pour terminer la connexion.", "success");
  } catch (error) { setStatus(accessStatus, "Le lien n’a pas pu être envoyé. Vérifiez l’adresse ou réessayez plus tard.", "error"); }
  finally { loginButton.disabled = false; }
});

document.querySelector("#logoutButton").addEventListener("click", async () => { try { await request("/api/admin/session", { method: "DELETE" }); } finally { showAccess(); setStatus(accessStatus, "Vous êtes déconnecté."); } });
document.querySelector("#seedButton").addEventListener("click", async (event) => { try { event.currentTarget.disabled = true; const result = await request("/api/admin/catalog/seed", { method: "POST" }); setNotice(result.message, "success"); await loadAll(); } catch (error) { setNotice(error.message, "error"); } finally { event.currentTarget.disabled = false; } });
document.querySelectorAll(".tab").forEach((tab) => tab.addEventListener("click", () => activateTab(tab.dataset.tab)));
boot();
