# Made by Ischou

Site de commande en ligne pour une marque artisanale de pastels et crepes faits maison a Lome, Togo.

Lien live : [madebyischou.com](https://madebyischou.com)

---

## Apercu

| Desktop | Mobile |
|---------|--------|
| ![Hero desktop](docs/preview-hero-desktop.png) | ![Hero mobile](docs/preview-hero-mobile.png) |

| Panier | Remerciement |
|--------|-------------|
| ![Drawer](docs/preview-drawer.png) | ![Thank you](docs/preview-thankyou.png) |

---

## Fonctionnalites

- Catalogue complet : pastels, crepes, box, offres groupées
- Panier interactif avec boutons + / −
- Supples payants (banane, chocolat) avec quantite propre
- Persistance du panier en localStorage (session uniquement)
- Livraison ou take-away avec geolocalisation
- Message WhatsApp pre-rempli avec total exact
- Overlay de remerciement avec barre de progression avant ouverture WhatsApp
- Typewriter hero avec rotation de trois etats editoriaux
- Menu responsive mobile avec burger
- Scroll reveal sur toutes les sections
- Accessibilite : ARIA, prefers-reduced-motion, navigation clavier

---

## Stack

- HTML, CSS, JavaScript inline — un seul fichier `index.html`
- Aucun framework, aucun build, aucun backend
- Google Fonts : Bricolage Grotesque, Inter Tight, Martian Mono, Yellowtail
- Commandes transmises via `wa.me` (WhatsApp)

---

## Structure du projet

```
.
├── index.html              # Application complete (HTML + CSS + JS)
├── favicon.svg
├── icon.svg
├── logo.svg
├── assets/
│   ├── shoppingbag.gif     # Animation remerciement
│   ├── hero section photo/
│   ├── pastels_et_crepes_jpeg/
│   └── images box crepes/
├── AGENTS.md               # Instructions agent
├── CLAUDE.md               # Contexte projet
├── PROMPT-CODEX-MAJ-CATALOGUE.md
├── PROMPT-CODEX-REFONTE.md
├── ROADMAP.md
└── LISEZ-MOI.md
```

---

## Donnees produits

Les prix et compositions sont definis dans `PROMPT-CODEX-MAJ-CATALOGUE.md`, seule source de verite.

| Produit | Prix |
|---------|------|
| Pastel Poisson Fume | 250 F |
| Pastel Classique | 300 F |
| Pastel Gourmand | a partir de 350 F |
| Crepe Chocolat | 500 F |
| Crepe Vanille | 500 F |
| Crepe Banane Chocolat | 500 F |
| Petite Box (5-6 crepes) | 3 000 F |
| Box Classique (8-10 crepes) | 4 000 F |
| 5 Pastels | 1 000 F |
| 10 Pastels | 2 000 F |

Supples : Banane +200 F, Chocolat +500 F.

---

## Commande

Les commandes se passent exclusivement par WhatsApp. Le site genere un message pre-rempli avec la selection du client, les supples, le total et les informations de livraison.

Aucune donnee n'est stockee cote serveur. Le panier est conservé en localStorage pendant la session.

---

## Developpement

Ouvrir `index.html` directement dans un navigateur. Aucune installation requise.

Pour les tests, des scripts Playwright sont disponibles temporairement dans le repertoire (a supprimer avant production).

---

## Licence

Projet prive. Made by Ischou.
