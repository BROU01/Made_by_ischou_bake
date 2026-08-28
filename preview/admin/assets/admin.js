/*
 * Preview admin "Made by Ischou" — /adminrootonly
 * Aucune donnée réelle de client, aucune authentification, aucun appel réseau.
 * Tout est stocké localement (localStorage) sous une clé distincte du panier public,
 * uniquement pour que les allers-retours de démonstration restent cohérents pendant la visite.
 * Rien ici ne doit être considéré comme sécurisé ou comme une source de vérité de production —
 * voir docs/ADMIN-VERCEL-MIGRATION.md pour la trajectoire réelle (backend, base, authentification).
 */
(function () {
  "use strict";

  var STORE_KEY = "made-by-ischou-admin-preview-v1";

  var CATALOGUE_INITIAL = [
    { id: "pas-poisson", famille: "Pastel", nom: "Poisson fumé", prix: 250, regle: "à la pièce", dispo: true },
    { id: "pas-classique", famille: "Pastel", nom: "Classique", prix: 300, regle: "Sardines.", dispo: true },
    { id: "pas-gourmand", famille: "Pastel", nom: "Gourmand", prix: 350, regle: "à partir de 350 F, prix confirmé à la commande", dispo: true },
    { id: "cre-chocolat", famille: "Crêpe", nom: "Chocolat", prix: 500, regle: "à la pièce", dispo: true },
    { id: "cre-vanille", famille: "Crêpe", nom: "Vanille", prix: 300, regle: "à la pièce", dispo: true },
    { id: "box-p-vanille", famille: "Box", nom: "Petite Box Vanille", prix: 1500, regle: "7 crêpes", dispo: true },
    { id: "box-p-chocolat", famille: "Box", nom: "Petite Box Chocolat", prix: 2500, regle: "6 crêpes", dispo: true },
    { id: "box-p-choco-banane", famille: "Box", nom: "Petite Box Chocolat-Banane", prix: 3500, regle: "6 crêpes", dispo: true },
    { id: "box-c-vanille", famille: "Box", nom: "Box Classique Vanille", prix: 2400, regle: "10 crêpes", dispo: true },
    { id: "box-c-chocolat", famille: "Box", nom: "Box Classique Chocolat", prix: 4000, regle: "9 crêpes", dispo: true },
    { id: "box-c-choco-banane", famille: "Box", nom: "Box Classique Chocolat-Banane", prix: 5600, regle: "9 crêpes", dispo: true },
    { id: "for-5-poisson", famille: "Formule", nom: "5 Pastels Poisson fumé", prix: 1000, regle: "formule fixe", dispo: true },
    { id: "for-5-classique", famille: "Formule", nom: "5 Pastels Classique", prix: 1200, regle: "formule fixe", dispo: true },
    { id: "for-5-gourmand", famille: "Formule", nom: "5 Pastels Gourmand", prix: 1500, regle: "formule fixe", dispo: true },
    { id: "for-11-poisson", famille: "Formule", nom: "11 Pastels Poisson fumé", prix: 2000, regle: "formule fixe", dispo: true },
    { id: "for-11-classique", famille: "Formule", nom: "11 Pastels Classique", prix: 2400, regle: "formule fixe", dispo: true },
    { id: "for-11-gourmand", famille: "Formule", nom: "11 Pastels Gourmand", prix: 3000, regle: "formule fixe", dispo: true }
  ];

  var COMMANDES_EXEMPLE = [
    { ref: "EX-0001", date: "2026-08-21", quartier: "Adidigomé (exemple)", items: "2× Box Classique Chocolat, 1× Formule 11 Pastels Classique", total: 6400, statut: "Livrée" },
    { ref: "EX-0002", date: "2026-08-27", quartier: "Ave Maria (exemple)", items: "1× Petite Box Vanille, 5× Pastel Poisson fumé (à la pièce)", total: 2750, statut: "En préparation" },
    { ref: "EX-0003", date: "2026-08-27", quartier: "Rue Mélonku (exemple)", items: "1× Formule 5 Pastels Gourmand", total: 1500, statut: "Reçue" }
  ];

  var MEDIAS_REELS = [
    { groupe: "Hero", nom: "made_by_ischou_hero_tabletop.jpg", src: "../../assets/hero section photo/made_by_ischou_hero_tabletop.jpg" }
  ];

  var REGLAGES_INITIAL = {
    nom: "Made by Ischou",
    adresse: "Adidigomé, Ave Maria, Rue Mélonku, Lomé",
    whatsappCommandes: "22871303911",
    telAffiche1: "71 30 39 11",
    telAffiche2: "97 11 56 38",
    cycle: "Commandes possibles entre deux jeudis, livraison le jeudi suivant."
  };

  var JOURNAL_EXEMPLE = [
    { date: "2026-08-27 09:12", action: "Exemple — disponibilité modifiée", detail: "Pastel Gourmand marqué disponible" },
    { date: "2026-08-21 18:40", action: "Exemple — statut de commande", detail: "EX-0001 passée à « Livrée »" }
  ];

  function load() {
    try {
      var raw = JSON.parse(localStorage.getItem(STORE_KEY));
      if (raw && typeof raw === "object") return raw;
    } catch (e) {}
    return null;
  }

  function seedState() {
    return {
      catalogue: CATALOGUE_INITIAL.map(function (p) { return Object.assign({}, p); }),
      commandes: COMMANDES_EXEMPLE.map(function (c) { return Object.assign({}, c); }),
      reglages: Object.assign({}, REGLAGES_INITIAL),
      journal: JOURNAL_EXEMPLE.slice()
    };
  }

  var state = load() || seedState();

  function persist() {
    try { localStorage.setItem(STORE_KEY, JSON.stringify(state)); } catch (e) {}
  }

  function fmt(n) {
    return new Intl.NumberFormat("fr-FR").format(n) + " F";
  }

  function log(action, detail) {
    var now = new Date();
    var pad = function (x) { return String(x).padStart(2, "0"); };
    var date = now.getFullYear() + "-" + pad(now.getMonth() + 1) + "-" + pad(now.getDate()) + " " + pad(now.getHours()) + ":" + pad(now.getMinutes());
    state.journal.unshift({ date: date, action: action, detail: detail });
    persist();
  }

  var toastTimer = null;
  function toast(msg) {
    var el = document.querySelector(".toast");
    if (!el) {
      el = document.createElement("div");
      el.className = "toast";
      document.body.appendChild(el);
    }
    el.textContent = msg;
    el.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { el.classList.remove("show"); }, 2600);
  }

  function resetAll() {
    state = seedState();
    persist();
  }

  window.IschouAdminPreview = {
    state: state,
    fmt: fmt,
    toast: toast,
    log: log,
    persist: persist,
    resetAll: resetAll
  };

  document.addEventListener("DOMContentLoaded", function () {
    var toggle = document.querySelector("[data-menu-toggle]");
    var side = document.querySelector(".side");
    if (toggle && side) {
      toggle.addEventListener("click", function () { side.classList.toggle("open"); });
    }
    var path = location.pathname.split("/").pop() || "index.html";
    document.querySelectorAll(".side__link").forEach(function (a) {
      if (a.getAttribute("href") === path) a.classList.add("active");
    });
  });
})();
