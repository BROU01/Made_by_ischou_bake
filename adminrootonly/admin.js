const $ = (selector) => document.querySelector(selector);
const $$ = (selector) => [...document.querySelectorAll(selector)];
const accessCard = $("#accessCard");
const adminApp = $("#adminApp");
const accessStatus = $("#accessStatus");
const appNotice = $("#appNotice");
const loginForm = $("#loginForm");
const loginButton = $("#loginButton");
const emailField = $("#email");
const productDialog = $("#productDialog");
const productForm = $("#productForm");
const emailStorageKey = "made_by_ischou_admin_login_email";
const labels = { dashboard:["Vue d’ensemble","Bonjour, l’atelier est prêt."], catalogue:["Produits","La carte de Made by Ischou."], analytics:["Audience","Comprendre les visites, sans les surveiller."], journal:["Journal","Chaque modification reste traçable."] };
const familyLabels = { pastel:"Pastel", crepe:"Crêpe", box:"Box de crêpes", "pastel-offer":"Formule pastel" };
let auth;
let products = [];
let editingProduct = null;

function setStatus(target, message = "", type = "") { target.textContent = message; target.className = `status${type ? ` ${type}` : ""}`; }
function setNotice(message = "", type = "") { appNotice.textContent = message; appNotice.className = `notice${type ? ` ${type}` : ""}`; }
function money(value) { return `${Number(value).toLocaleString("fr-FR")} F`; }
function humanDate(value) { if (!value) return "À l’instant"; const date = value._seconds ? new Date(value._seconds * 1000) : new Date(value); return Number.isNaN(date.valueOf()) ? "À l’instant" : date.toLocaleString("fr-FR", { dateStyle:"medium", timeStyle:"short" }); }
function escapeHtml(value = "") { return String(value).replace(/[&<>'"]/g, (char) => ({ "&":"&amp;", "<":"&lt;", ">":"&gt;", "'":"&#39;", "\"":"&quot;" }[char])); }
function quantityLabel(product) { if (!product.announcedQuantity) return "Quantité non précisée"; return `${product.announcedQuantity} ${product.announcedQuantity === 1 ? "pièce" : "pièces"}`; }

async function request(path, options = {}) {
  const response = await fetch(path, { credentials:"same-origin", headers:{ "Content-Type":"application/json", ...(options.headers || {}) }, ...options });
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
function showAccess() { adminApp.hidden = true; accessCard.hidden = false; closeSidebar(); }
function actionLabel(action = "activité") { return action.replaceAll("_", " ").replace(/^./, (letter) => letter.toUpperCase()); }

function renderActivity(entries, target) {
  if (!entries?.length) { target.innerHTML = '<p class="empty-state">Aucune action n’a encore été enregistrée.</p>'; return; }
  target.innerHTML = entries.map((entry) => `<article class="activity-item"><div><strong>${escapeHtml(actionLabel(entry.action))}</strong><span class="activity-target">${escapeHtml(entry.targetType || "activité")}${entry.targetId ? ` · ${escapeHtml(entry.targetId)}` : ""}</span></div><time>${escapeHtml(humanDate(entry.createdAt))}</time></article>`).join("");
}

function renderKpis(data) {
  const active = products.filter((product) => product.isActive).length;
  const entries = [["Références visibles", active, `${products.length || data.products} références dans la carte.`], ["Commandes consenties", data.orders, "Aucune conversation WhatsApp."], ["Médias administrés", data.media, "Bibliothèque de visuels future."], ["Audience", "—", "La liaison Analytics est à activer."]];
  $("#kpis").innerHTML = entries.map(([label, value, detail]) => `<article class="metric-card${value === "—" ? " metric-card--pending" : ""}"><span>${escapeHtml(label)}</span><strong>${escapeHtml(value)}</strong><small>${escapeHtml(detail)}</small></article>`).join("");
}

function filteredProducts() {
  const term = $("#catalogueSearch").value.trim().toLocaleLowerCase("fr");
  const family = $("#familyFilter").value;
  return products.filter((product) => (family === "all" || product.family === family) && (!term || `${product.name} ${product.description}`.toLocaleLowerCase("fr").includes(term)));
}

function renderCatalogue() {
  const list = filteredProducts();
  $("#catalogueCount").textContent = `${list.length} / ${products.length} référence${products.length > 1 ? "s" : ""}`;
  $("#catalogueEmpty").hidden = Boolean(list.length || !products.length);
  if (!products.length) { $("#catalogueBody").innerHTML = ""; $("#catalogueEmpty").hidden = false; $("#catalogueEmpty").textContent = "Le catalogue est vide. Initialisez les 17 références validées pour démarrer."; return; }
  $("#catalogueEmpty").textContent = "Aucune référence ne correspond à cette recherche.";
  $("#catalogueBody").innerHTML = list.map((product) => `<tr><td><div class="product-cell"><strong>${escapeHtml(product.name)}</strong><small>${escapeHtml(product.description)}</small></div></td><td><span class="family-label">${escapeHtml(familyLabels[product.family] || product.family)}</span></td><td><span class="product-price">${product.isEstimatedPrice ? "À partir de " : ""}${escapeHtml(money(product.price))}</span><br><small>${escapeHtml(product.unitLabel)} · ${escapeHtml(quantityLabel(product))}</small></td><td><span class="status-pill ${product.isActive ? "status-pill--active" : "status-pill--hidden"}">${product.isActive ? "Visible" : "Masqué"}</span></td><td class="product-actions"><button class="row-button" type="button" data-edit-product="${escapeHtml(product.id)}">Modifier</button></td></tr>`).join("");
}

async function loadDashboard() { const data = await request("/api/admin/dashboard"); renderKpis(data); renderActivity(data.recentActivity, $("#recentActivity")); }
async function loadCatalogue() { products = await request("/api/admin/catalog"); renderCatalogue(); }
async function loadActivity() { renderActivity(await request("/api/admin/activity"), $("#activity")); }
async function loadAll() { await loadCatalogue(); await Promise.all([loadDashboard(), loadActivity()]); }

function closeSidebar() { $("#adminSidebar").classList.remove("open"); $("#sidebarBackdrop").classList.remove("show"); $("#sidebarBackdrop").hidden = true; $("#sidebarToggle").setAttribute("aria-expanded", "false"); }
function openSidebar() { $("#adminSidebar").classList.add("open"); $("#sidebarBackdrop").hidden = false; $("#sidebarBackdrop").classList.add("show"); $("#sidebarToggle").setAttribute("aria-expanded", "true"); }
function activateTab(name) {
  const [eyebrow, title] = labels[name];
  $("#pageEyebrow").textContent = eyebrow; $("#pageTitle").textContent = title;
  $$(".nav-item").forEach((tab) => { const active = tab.dataset.tab === name; tab.classList.toggle("active", active); if (active) tab.setAttribute("aria-current", "page"); else tab.removeAttribute("aria-current"); });
  $$(".panel-view").forEach((panel) => { panel.hidden = panel.id !== `${name}Panel`; });
  closeSidebar();
}

function openProductDialog(id) {
  editingProduct = products.find((product) => product.id === id);
  if (!editingProduct) return;
  $("#editName").value = editingProduct.name;
  $("#editDescription").value = editingProduct.description;
  $("#editPrice").value = editingProduct.price;
  $("#editUnitLabel").value = editingProduct.unitLabel;
  $("#editQuantity").value = editingProduct.announcedQuantity ?? "";
  $("#editActive").checked = editingProduct.isActive;
  $("#editEstimated").checked = editingProduct.isEstimatedPrice;
  setStatus($("#dialogStatus"));
  productDialog.showModal();
  $("#editName").focus();
}

function closeProductDialog() { productDialog.close(); editingProduct = null; }
async function saveProduct(event) {
  event.preventDefault();
  if (!editingProduct || !productForm.reportValidity()) return;
  const saveButton = $("#saveProduct");
  const rawQuantity = $("#editQuantity").value.trim();
  const input = { id:editingProduct.id, name:$("#editName").value.trim(), description:$("#editDescription").value.trim(), price:Number($("#editPrice").value), unitLabel:$("#editUnitLabel").value.trim(), announcedQuantity:rawQuantity ? Number(rawQuantity) : null, isActive:$("#editActive").checked, isEstimatedPrice:$("#editEstimated").checked };
  try { saveButton.disabled = true; setStatus($("#dialogStatus"), "Enregistrement sécurisé…"); await request("/api/admin/catalog", { method:"PATCH", body:JSON.stringify(input) }); setNotice("Produit mis à jour et journalisé.", "success"); closeProductDialog(); await loadAll(); } catch (error) { setStatus($("#dialogStatus"), error.message || "La modification n’a pas été enregistrée.", "error"); } finally { saveButton.disabled = false; }
}

async function completeMagicLink(authModule) {
  if (!authModule.isSignInWithEmailLink(auth, window.location.href)) return false;
  const email = localStorage.getItem(emailStorageKey) || window.prompt("Confirmez l’adresse e-mail utilisée pour recevoir ce lien :");
  if (!email) throw new Error("L’adresse e-mail est nécessaire pour finaliser la connexion.");
  setStatus(accessStatus, "Vérification sécurisée du lien…");
  const credential = await authModule.signInWithEmailLink(auth, email, window.location.href);
  const idToken = await credential.user.getIdToken(true);
  await request("/api/admin/session", { method:"POST", headers:{ Authorization:`Bearer ${idToken}` } });
  localStorage.removeItem(emailStorageKey); await authModule.signOut(auth); history.replaceState({}, document.title, "/adminrootonly/"); return true;
}

async function boot() {
  try { const authModule = await setupFirebase(); const linkCompleted = await completeMagicLink(authModule); const session = await request("/api/admin/session").catch(() => null); if (!session) { showAccess(); if (linkCompleted) setStatus(accessStatus, "Connexion validée. Le tableau de bord est prêt.", "success"); return; } showApp(); await loadAll(); } catch (error) { showAccess(); setStatus(accessStatus, error.message || "La connexion n’a pas abouti.", "error"); }
}

loginForm.addEventListener("submit", async (event) => { event.preventDefault(); const email = emailField.value.trim(); if (!emailField.checkValidity()) { setStatus(accessStatus, "Saisissez une adresse e-mail valide.", "error"); emailField.focus(); return; } try { loginButton.disabled = true; setStatus(accessStatus, "Préparation du lien sécurisé…"); const { sendSignInLinkToEmail } = await import("https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js"); await sendSignInLinkToEmail(auth, email, { url:`${window.location.origin}/adminrootonly/`, handleCodeInApp:true }); localStorage.setItem(emailStorageKey, email); setStatus(accessStatus, "Lien envoyé. Ouvrez-le depuis votre boîte e-mail pour terminer la connexion.", "success"); } catch (error) { setStatus(accessStatus, "Le lien n’a pas pu être envoyé. Vérifiez l’adresse ou réessayez plus tard.", "error"); } finally { loginButton.disabled = false; } });
$("#logoutButton").addEventListener("click", async () => { try { await request("/api/admin/session", { method:"DELETE" }); } finally { showAccess(); setStatus(accessStatus, "Vous êtes déconnecté."); } });
$("#seedButton").addEventListener("click", async (event) => { try { event.currentTarget.disabled = true; const result = await request("/api/admin/catalog/seed", { method:"POST" }); setNotice(result.message, "success"); await loadAll(); } catch (error) { setNotice(error.message, "error"); } finally { event.currentTarget.disabled = false; } });
$("#catalogueSearch").addEventListener("input", renderCatalogue); $("#familyFilter").addEventListener("change", renderCatalogue); $("#catalogueBody").addEventListener("click", (event) => { const button = event.target.closest("[data-edit-product]"); if (button) openProductDialog(button.dataset.editProduct); });
$$(".nav-item").forEach((tab) => tab.addEventListener("click", () => activateTab(tab.dataset.tab))); $$('[data-go-to="journal"]').forEach((button) => button.addEventListener("click", () => activateTab("journal")));
$("#sidebarToggle").addEventListener("click", () => $("#adminSidebar").classList.contains("open") ? closeSidebar() : openSidebar()); $("#sidebarBackdrop").addEventListener("click", closeSidebar);
$("#dialogClose").addEventListener("click", closeProductDialog); $("#dialogCancel").addEventListener("click", closeProductDialog); productForm.addEventListener("submit", saveProduct);
boot();
