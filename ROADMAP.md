# Roadmap de reprise — Made by Ischou

> Ce document est le point de reprise du projet. Il est mis à jour après chaque lot validé : décisions, état d'avancement, fichiers concernés et prochaine action.

## État actuel

- [x] Briefs lus et ordre de préséance documenté.
- [x] Version rejetée archivée sous `index-v1.html`.
- [x] `CLAUDE.md`, `AGENTS.md` et `LISEZ-MOI.md` réconciliés avec les briefs disponibles.
- [x] Catalogue mis à jour dans la documentation selon `PROMPT-CODEX-MAJ-CATALOGUE.md`.
- [x] Six photos produit vérifiées dans `assets/pastels_et_crepes_jpeg/`.
- [x] Décisions catalogue reçues : Pastel Poisson Fumé maintenu ; tous les pastels dans les offres ; offre 2 pastels supprimée ; supplément « Autre garniture — 600 F » maintenu ; Pastel Gourmand sans paliers détaillés ; box crêpes livrées le jeudi.
- [x] Début des livraisons confirmé : jeudi 12h00 (heure de Lomé, UTC+0) ; cible du compte à rebours.
- [x] Phase 1 : direction artistique sélectionnée — « La fournée en bande ».
- [x] Timer confirmé : livraisons jeudi 12h00 ; clôture jeudi 20h00 ; ouverture technique vendredi 00h00.
- [x] Lot 1 : structure, jetons, machine à états hebdomadaire et héros construits dans `index.html`.
- [x] Lot 2 : catalogue complet — pastels, crêpes, box, offres, extras, suppléments — panier dans l'en-tête, carnet de commande, gestion prix variable.

## Source de vérité

1. `PROMPT-CODEX-MAJ-CATALOGUE.md` — catalogue, prix, section H.
2. `PROMPT-CODEX-TIMER.md` — timer, section I.
3. `PROMPT-CODEX-REFONTE.md` — direction, sections A à G.
4. `CLAUDE.md` et `AGENTS.md` — contraintes techniques.
5. `index-v1.html` — uniquement le format WhatsApp et le flux GPS / adresse.

## Décisions fonctionnelles validées

- Commandes possibles entre deux jeudis ; livraison le jeudi suivant.
- Le compte à rebours vise le début des livraisons, jeudi 12h00 (heure de Lomé, UTC+0).
- Les commandes ferment jeudi à 20h00 ; l'ouverture technique du cycle suivant est vendredi 00h00.
- Le numéro WhatsApp de commande est `22871303911`.
- Catalogue :
  - Pastel Poisson Fumé — 250 F ; maintenu.
  - Pastel Classique — 300 F ; composition exacte : « Sardines. »
  - Pastel Gourmand — « À partir de 350 F » ; pas de paliers à afficher.
  - Offres : 5 pastels — 1 000 F ; 10 pastels — 2 000 F ; tous les pastels sont éligibles.
  - Offre 2 pastels — supprimée.
  - Crêpes à l'unité — 500 F.
  - Box crêpes — même rythme de livraison du jeudi.
  - Suppléments : Banane +200 F, Chocolat +500 F, Autre garniture +600 F.
  - Extras offerts : Éclats de biscuits, Noix de coco râpée, Amandes effilées.

## États d'avancement par lot

### Lot 1 — ✅ Terminé
Structure, jetons, machine à états hebdomadaire, héros timer, écho collant, simulateur.

### Lot 2 — ✅ Terminé
Catalogue complet dans `index.html` :
- **Pastels** (3 produits) : blocs typographiques, prix variable pour le Gourmand.
- **Offres pastels** (2) : 5 pastels — 1 000 F ; 10 pastels — 2 000 F.
- **Crêpes** (3) : blocs typographiques à 500 F.
- **Box crêpes** (2) : Petite Box — 3 000 F ; Box Classique — 4 000 F.
- **Suppléments crêpes** (3) : Banane +200 F, Chocolat +500 F, Autre garniture +600 F. Bloc visuellement distinct des extras.
- **Extras gourmands** (3) : Éclats de biscuits, Noix de coco râpée, Amandes effilées — gratuits, badges « offert ».
- **Panier** : déclencheur dans l'en-tête collant, tiroir latéral avec carnet de commande, stepper par article, suppression de ligne, confirmation de vidage.
- **Prix variable** : Pastel Gourmand affiché « À partir de 350 F », total libellé « Total estimé », mention de confirmation dans le carnet et le message WhatsApp.
- **Festons** entre sections.
- **Pied de page** avec contact, adresse, horaires.
- **Simulateur** de test toujours présent, délimité et supprimable.

### Lot 3 — ⏳ À venir
- Piège focus dans le carnet de commande (accessibilité clavier).
- Annulation 5 secondes après suppression de ligne.
- Vidage confirmé et réversible (déjà en place, à valider).
- Mobile : carnet en plein écran sous 640 px.
- Restitution du focus au déclencheur à la fermeture.

### Lot 4 — ⏳ À venir
- Message WhatsApp au format exact de `index-v1.html` (ordonnancement, libellés, unité F).
- Choix livraison Oui/Non dans le carnet.
- Géolocalisation `getCurrentPosition` + fallback adresse.
- Messages d'erreur explicites.
- Affichage de l'état de phase dans le carnet (« Cette commande partira sur la fournée de… »).

### Lot 5 — ⏳ À venir
- Responsive 360–1920 px — vérification minutieuse.
- Contraste ≥ 4.5:1 sur tous les jetons.
- `prefers-reduced-motion` — vérifier timer, transitions, pulse.
- Zéro erreur console.
- Passe de retrait : retirer un élément décoratif et documenter.
