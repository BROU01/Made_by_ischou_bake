# CLAUDE.md — Made by Ischou

> Contexte de travail du projet. Lire les briefs normatifs avant toute modification.

## 1. Statut et ordre de préséance

La version 1 est archivée dans `index-v1.html`. Elle est rejetée sur le plan visuel et ne sert plus que de référence pour le format exact du message WhatsApp et le flux géolocalisation / adresse.

L'ordre de préséance est strict :

1. `PROMPT-CODEX-MAJ-CATALOGUE.md` — catalogue, prix et section H ;
2. `PROMPT-CODEX-TIMER.md` — timer et section I ;
3. `PROMPT-CODEX-REFONTE.md` — direction artistique et sections A à G ;
4. ce fichier et `AGENTS.md` — contraintes techniques uniquement ;
5. `index-v1.html` — référence d'implémentation limitée, jamais autorité.

`PROMPT-CODEX-MAJ-CATALOGUE.md` est la source unique du catalogue et des prix. Ne jamais les déduire d'un document antérieur.

## 2. Identité et produit

**Made by Ischou** est un commerce artisanal de pastels et crêpes faits maison, à Adidigomé (Ave Maria, Rue Mélonku), Lomé, Togo.

Le site compose une commande puis ouvre un lien WhatsApp pré-rempli. Il ne traite ni paiement, ni compte, ni backend. L'interface et les échanges sont en français. Orthographe obligatoire : **Ischou**.

Public : particuliers à Lomé, majoritairement sur mobile Android, connexion souvent lente.

## 3. Contraintes techniques non négociables

1. Le seul livrable applicatif est `index.html`, avec HTML, CSS et JavaScript inline.
2. Aucun build, framework, dépendance JavaScript, backend, base de données ou variable d'environnement. Google Fonts est la seule ressource externe admise.
3. Aucun `localStorage` ni `sessionStorage` : le panier vit en mémoire.
4. Le canal de commande est `wa.me?text=` avec contenu encodé par `encodeURIComponent` ; aucune WhatsApp Cloud API.
5. Ne jamais inventer un prix, produit, horaire ou numéro.

## 4. Direction en vigueur

La thèse est le rythme hebdomadaire : le héros est le temps, pas une photo.

- Champ dominant : framboise `#BC1B57` ; encre crème `#FBF3E9`.
- Jetons autorisés uniquement : `#BC1B57`, `#9A1447`, `#7A1230`, `#2A1810`, `#FBF3E9`, `#F3E6D5`, `#C2963B`, `#3E7B3A`.
- L'ambre `#C2963B` est réservé aux montants et aux chiffres du compte à rebours.
- Typographies : Bricolage Grotesque (display), Inter Tight (corps/interface), Martian Mono (temps, prix et chiffres tabulaires). Yellowtail est réservé au wordmark, une occurrence maximum.
- Les séparateurs sont des festons SVG répétés.
- Interdits : émojis-icônes, dégradés décoratifs, blobs, particules, ombres colorées, glassmorphisme, `backdrop-filter` ornemental, texte de remplissage, preuve sociale inventée et urgence fabriquée.

## 5. Timer hebdomadaire

La section I de `PROMPT-CODEX-TIMER.md` remplace B1 à B8 de la refonte ; B9 reste en vigueur. La référence fonctionnelle est `timer-reference.html`.

- Le rythme est défini dans un unique objet de configuration : ouverture, début des livraisons, clôture.
- La logique lit l'heure de Lomé avec les accesseurs UTC exclusivement.
- Les phases sont exactement `ouvert`, `livraison`, `ferme` ; elles changent le champ en framboise, bordeaux, puis chocolat.
- Le héros et un unique écho collant affichent le timer ; aucune troisième occurrence.
- La machine est testable avec une horloge injectable et un simulateur clairement séparé, retiré avant production.
- Règle métier validée : le client peut composer sa commande après le jeudi d'une semaine et jusqu'au jeudi suivant, pour la prochaine livraison du jeudi.
- Le début des livraisons est fixé au jeudi 12h00 et la clôture au jeudi 20h00 (heure de Lomé, UTC+0) : le compte à rebours vise le début des livraisons.
- L'ouverture technique est vendredi 00h00, déduite de la règle « après le jeudi » afin de permettre les trois phases de la section I. Les horaires correspondants de `timer-reference.html` restent périmés.
- Le message de fermeture tardive est dérivé de `RYTHME.cloture`, jamais figé dans le texte.

## 6. Catalogue en vigueur

La Partie 2 de `PROMPT-CODEX-MAJ-CATALOGUE.md` remplace intégralement les données antérieures.

- Pastels : Poisson Fumé — 250 F ; Classique — 300 F, composition exacte « Sardines. » ; Gourmand — « À partir de 350 F », prix variable.
- Offres : 5 Pastels — 1 000 F ; 10 Pastels — 2 000 F. Les offres 2 et 4 pastels, ainsi que 10 pastels à 2 200 F, sont périmées.
- Crêpes : Chocolat — 500 F la pièce ; Vanille — 300 F la pièce.
- Box crêpes : Petite Box — 3 000 F ; Box Classique — 4 000 F.
- Supplément crêpe payant : Banane +200 F. Aucun supplément chocolat actif. Les extras gourmands restent gratuits uniquement s’ils sont confirmés dans le catalogue actif.
- WhatsApp : `22871303911` reçoit les commandes. Les deux numéros restent affichés en contact téléphonique.

Le Pastel Gourmand impose les règles H1 à H3 : prix « À partir de 350 F », total libellé « Total estimé » et mention de confirmation dans le message WhatsApp. Les suppléments sont des lignes payantes, avec quantité propre, et restent distincts des extras offerts.

### Décisions catalogue validées

- Le Pastel Poisson Fumé est maintenu.
- Tous les pastels sont admissibles aux offres de 5 et 10 pièces.
- L'offre « 2 pastels — 500 F » est supprimée.
- Le supplément « Autre garniture — 600 F » est maintenu.
- Les variantes sardine, saucisse et œuf du Pastel Gourmand n'ont pas de paliers distincts : le prix reste présenté « À partir de 350 F » et confirmé à la commande.
- Les box crêpes suivent le même rythme de livraison du jeudi.

## 7. Panier, carnet et WhatsApp

- Aucune barre panier flottante ; le déclencheur, avec quantité et total, est dans l'en-tête collant et garde sa place même vide.
- Le carnet est un bon de commande manuscrit, avec perforation et lignes en tirets ; plein écran sous 640 px.
- Il se ferme par bouton, Échap ou clic sur le voile, piège le focus puis le restitue au déclencheur.
- Vider le panier nécessite une confirmation réversible ; retirer une ligne offre « Annuler » pendant cinq secondes.
- Conserver exactement le format WhatsApp de `index-v1.html` : ordre des blocs, libellés, sauts de ligne et unité `F`.
- La géolocalisation utilise `getCurrentPosition` avec `timeout: 10000`, génère un lien Google Maps à six décimales et propose toujours une adresse comme chemin de premier rang. Masquer le bouton GPS si l'API est absente.

## 8. Assets

La page doit rester complète sans photo. Chaque produit est d'abord un bloc typographique composé ; un point d'insertion `assets/{id}.jpg` pourra remplacer l'aplat sans modifier la hauteur ou la mise en page. Il n'y a pas de photo héros.

Six photos sont disponibles dans `assets/pastels_et_crepes_jpeg/` : les trois pastels et les trois crêpes unitaires. Elles devront être reprises sous les noms canoniques `assets/{id}.jpg` uniquement au moment où l'implémentation des cartes photo est autorisée.

Les fichiers de marque sont fournis à la racine : `logo.svg`, `icon.svg` et `favicon.svg`. Consulter `LOGO.md` pour leur usage.

## 9. Plancher qualité

- Utilisable de 360 px à 1920 px ; cibles tactiles et envoi adaptés au mobile.
- Focus visible d'au moins 3 px ; interactions clavier complètes.
- Contraste texte d'au moins 4.5:1.
- `prefers-reduced-motion: reduce` désactive les transitions, animations du timer et pulsation d'état.
- Aucune erreur console et réponse visuelle à chaque interaction sous 400 ms.

## 10. Skills

Avant toute tâche, vérifier `.claude/skills/` si le dossier existe puis lire les `SKILL.md` dont la description recoupe la demande. Pour cette refonte, seuls les skills autorisés par l'humain peuvent être chargés. En cas de conflit, les trois briefs normatifs ci-dessus priment.
