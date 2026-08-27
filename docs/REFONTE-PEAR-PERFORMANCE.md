# Audit de refonte — Pear et Made by Ischou

Date : 27 août 2026

## Référence Pear : principes réutilisables, non éléments à copier

La référence Pear repose sur une narration éditoriale très concentrée : un hero à visuel flou en arrière-plan, une grande phrase manifeste, des traits de repère fins, une hiérarchie typographique marquée, des sections longues mais aérées, et une révélation progressive au défilement. La refonte Made by Ischou pourra reprendre ce **rythme visuel**, la composition asymétrique, les repères inspirés d’étiquettes artisanales et des transitions lentes mais discrètes.

La marque, le texte, les couleurs bleu pétrole, le canvas décoratif, les contenus, les interactions et les médias de Pear ne seront pas reproduits. Made by Ischou conservera son univers chocolat, crème, framboise et or, ses photos alimentaires et sa commande WhatsApp.

## État du site déployé

Le site en ligne est un unique fichier `index.html` d’environ 2 106 lignes. Il charge une landing page, les produits, les box et les offres dans le même document, avec plusieurs observateurs, animations, détails produits, tiroir panier, overlay de remerciement et typewriter. Le transfert initial mesuré depuis la production est rapide, mais l’expérience peut être ralentie sur certains ordinateurs par la combinaison de toutes les sections, des images, du rendu dynamique et des calculs d’animation au scroll.

Le dossier `assets` pèse environ 3,5 Mo. Les images individuelles des pastels et crêpes représentent entre environ 276 Ko et 551 Ko chacune ; le hero optimisé représente environ 391 Ko. Ces poids restent acceptables pour une page courte, mais une landing enrichie doit éviter de charger dès l’ouverture des images qui se trouvent loin sous la ligne de flottaison.

## Budget et règles de performance pour la refonte

| Décision | Application prévue |
|---|---|
| Architecture | Rester sur une seule page HTML pour le site public déployé, avec ancres internes et sections clairement séparées. |
| Hero | Une seule image hero optimisée, `fetchpriority="high"`, sans vidéo, canvas lourd ou slider automatique. |
| Images secondaires | `loading="lazy"`, dimensions explicites, WebP ou JPEG optimisé, et chargement au défilement uniquement. |
| Animations | Une seule logique `IntersectionObserver`, transformations/opacité seulement, aucun calcul sur chaque image à chaque évènement scroll. |
| Typewriter | Une courte phrase, arrêt lors de `prefers-reduced-motion`, aucune boucle de réécriture coûteuse. |
| Catalogue | Les 17 cartes chargées dans des groupes repliables ou révélés après interaction/scroll, plutôt qu’un rendu dense immédiat. |
| Panier | Conserver les fonctions validées, mais éviter les reconstructions inutiles de DOM pendant le défilement. |

## Direction proposée

La landing page devient une histoire de commande en cinq temps : un hero manifeste et éditorial ; une frise « du façonnage au partage » ; les pastels ; les crêpes ; les offres spéciales avec les box et formules. Le panier reste disponible mais léger. Les images prennent le rôle de preuve produit, tandis que les repères graphiques évoquent la bordure festonnée d’un pastel et l’étiquette d’une préparation maison.

## Garde-fous de représentation des portions

Les photos de référence fournies le 27 août 2026 servent à corriger la perception de volume, et non à importer des recettes, ingrédients ou décorations. Chaque pastel devra présenter une demi-lune large, à bords pincés épais, dont la taille est clairement lisible par rapport à une grande assiette ou à la box. Chaque crêpe devra apparaître longue, roulée de façon souple, avec une épaisseur généreuse et une présence visuelle comparable à une portion de dessert complète.

| Produit | Repère de représentation retenu | Éléments à exclure |
|---|---|---|
| Pastels individuels | Trois grandes demi-lunes peuvent remplir une assiette de repas ; un pastel ne doit jamais ressembler à une bouchée apéritive. | Portions miniatures, forme triangulaire, garnitures inventées, sauces et herbes décoratives. |
| Crêpes individuelles | Une crêpe roulée doit s’étendre visiblement sur une grande assiette, avec une largeur et un volume réalistes. | Fraises, crème fouettée, autres fruits, garnitures salées et recettes absentes de la carte. |
| Petite box | Les 6 ou 7 crêpes doivent être serrées mais distinctes, suffisamment longues pour occuper le contenant. | Une photo de box dont les pièces seraient des mini-rouleaux disproportionnés. |
| Box classique | Les 9 ou 10 crêpes doivent être visibles comme une quantité généreuse et crédible dans le contenant réel. | Empilement confus empêchant de percevoir les pièces annoncées. |
| Formules pastels | Les lots doivent montrer exactement 5 ou 11 pastels de taille généreuse dans un cadrage lisible. | Quantités ambiguës, doublons visuels ou petits chaussons donnant une impression de portion réduite. |
