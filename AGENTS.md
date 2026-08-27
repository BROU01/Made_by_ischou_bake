# AGENTS.md — Made by Ischou

Lire `CLAUDE.md` et les briefs normatifs avant toute modification.

## Préséance

1. Les décisions de catalogue et de présentation confirmées par la cliente dans la conversation active — elles remplacent les valeurs antérieures qui les contredisent.
2. `docs/REFONTE-PEAR-PERFORMANCE.md` et `docs/PROMPTS-VISUELS-OFFRES.md` — direction de refonte, performance et représentation honnête des portions.
3. `PROMPT-CODEX-TIMER.md` — timer, seulement dans les limites des décisions récentes de la cliente.
4. `CLAUDE.md` / ce fichier — technique uniquement.
5. `index-v1.html` — uniquement WhatsApp et géolocalisation / adresse.

## Décisions cliente en vigueur — 27 août 2026

- Le livrable public reste une landing page **mono-page** dans `index.html`, déployée depuis `BROU01/Made_by_ischou_bake` vers `https://ischou.vercel.app`.
- Les sections publiques sont Accueil, Pastels, Crêpes, Offres spéciales et Infos, reliées par ancres internes.
- Le catalogue en cours est : 3 pastels individuels, 2 crêpes individuelles, 6 box de crêpes et 6 formules de pastels. Les formules sont séparées par type de pastel et par quantité de 5 ou 11 pièces.
- Supplément unique : Banane +200 F, applicable par crêpe individuelle ou par box. Il ne doit jamais être proposé sur un pastel ni une formule de pastels.
- Le hero peut utiliser une photo alimentaire optimisée. Les visuels doivent représenter des pastels larges et généreux ainsi que des crêpes longues et épaisses ; ne jamais employer une image donnant l’impression de mini-portions.
- Les anciennes valeurs « 5 à 6 crêpes », « 8 à 10 crêpes », « 10 pastels », « tous pastels confondus », les deux box génériques et les deux offres génériques sont périmées.
- Les données privées et un panneau admin réellement sécurisé restent hors du site statique ; leur migration sera traitée séparément avec un backend réel.

## Règles essentielles

- Livrable applicatif unique : `index.html`, avec HTML, CSS et JS inline.
- Aucun framework, build, backend ni Cloud API dans la landing page publique ; commandes via `wa.me?text=` encodé. Le panier peut être conservé localement uniquement pour faciliter la reprise d’une commande, sans données personnelles.
- Direction : champ framboise, encre crème ; Bricolage Grotesque, Inter Tight, Martian Mono ; Yellowtail réservé au seul wordmark.
- Jetons autorisés : `#BC1B57`, `#9A1447`, `#7A1230`, `#2A1810`, `#FBF3E9`, `#F3E6D5`, `#C2963B`, `#3E7B3A`.
- Aucun emoji-icône, dégradé décoratif, blob, image manquante ou texte de remplissage.
- Le hero combine une phrase manifeste, une photo alimentaire optimisée et un rythme éditorial inspiré de Pear, sans copie visuelle ou technique.
- Les photos produit sont autorisées lorsqu’elles sont optimisées, lazy-loadées hors hero et cohérentes avec la portion réellement proposée.
- Ne jamais inventer prix, produits, horaires ou numéro ; le catalogue en vigueur vient exclusivement de `PROMPT-CODEX-MAJ-CATALOGUE.md`.
- Les commandes sont possibles entre deux jeudis, pour livraison le jeudi suivant. Aucune heure de cycle n'est validée : ne pas figer le timer.
- Interface et échanges : français.
