# CLAUDE.md — Made by Ischou

> Référence technique et métier consolidée le 27 août 2026. Les décisions explicites de la cliente dans la conversation active priment sur tout brief antérieur.

## 1. Projet public et ordre de préséance

Le site public est une landing page **mono-page** dans `index.html`, déployée depuis `BROU01/Made_by_ischou_bake` vers `https://ischou.vercel.app`.

L’ordre de décision est le suivant :

1. Les décisions récentes de la cliente ;
2. `docs/REFONTE-PEAR-PERFORMANCE.md` et `docs/PROMPTS-VISUELS-OFFRES.md` ;
3. `PROMPT-CODEX-TIMER.md` pour le rythme de commande ;
4. Ce fichier et `AGENTS.md` pour les contraintes techniques ;
5. `index-v1.html` seulement comme référence de secours du format WhatsApp et de la géolocalisation.

## 2. Contraintes techniques

- Le livrable public est un unique `index.html` avec HTML, CSS et JavaScript inline.
- Aucun framework, backend, base de données, variable d’environnement ou clé secrète dans la landing page publique.
- Le panier peut utiliser `localStorage` pour restaurer les quantités après rechargement. Il ne doit jamais y stocker de nom, adresse ou géolocalisation.
- Toute commande ouvre uniquement un lien `wa.me?text=` créé avec `encodeURIComponent`. Aucune API WhatsApp ni paiement n’est intégré.
- Une future administration sécurisée exige un backend, une base de données et une authentification réelle ; une URL cachée ne constitue jamais une sécurité.

## 3. Marque et localisation

**Made by Ischou** propose des pastels et crêpes faits maison à **Adidigomé, Ave Maria, Rue Mélonku, Lomé**. La communication est en français et le public principal utilise un smartphone Android avec une connexion parfois lente.

Les commandes sont possibles entre deux jeudis et la livraison a lieu le jeudi suivant. Le numéro WhatsApp des commandes est `22871303911`. Les deux numéros téléphoniques restent affichés en contact : `71 30 39 11` et `97 11 56 38`.

## 4. Catalogue validé

| Famille | Produit | Prix | Quantité / règle |
|---|---|---:|---|
| Pastel | Poisson fumé | 250 F | à la pièce |
| Pastel | Classique | 300 F | composition exacte : `Sardines.` |
| Pastel | Gourmand | À partir de 350 F | prix variable à confirmer à la commande |
| Crêpe | Chocolat | 500 F | à la pièce |
| Crêpe | Vanille | 300 F | à la pièce |
| Box | Petite Box Vanille | 1 500 F | 7 crêpes |
| Box | Petite Box Chocolat | 2 500 F | 6 crêpes |
| Box | Petite Box Chocolat-Banane | 3 500 F | 6 crêpes |
| Box | Box Classique Vanille | 2 400 F | 10 crêpes |
| Box | Box Classique Chocolat | 4 000 F | 9 crêpes |
| Box | Box Classique Chocolat-Banane | 5 600 F | 9 crêpes |
| Formule | 5 Pastels Poisson fumé | 1 000 F | formule fixe |
| Formule | 5 Pastels Classique | 1 200 F | formule fixe |
| Formule | 5 Pastels Gourmand | 1 500 F | formule fixe |
| Formule | 11 Pastels Poisson fumé | 2 000 F | formule fixe |
| Formule | 11 Pastels Classique | 2 400 F | formule fixe |
| Formule | 11 Pastels Gourmand | 3 000 F | formule fixe |

Le seul supplément actif est **Banane +200 F**, applicable par crêpe individuelle ou par box. Il ne doit jamais s’afficher sur les pastels ni les formules de pastels. Aucun supplément chocolat et aucune « autre garniture » ne sont actifs.

## 5. Direction de landing page

La navigation relie les ancres Accueil, Pastels, Crêpes, Offres spéciales et Infos. La direction s’inspire uniquement des principes de Pear : phrase manifeste, composition asymétrique, rythme éditorial et repères graphiques fins. Elle ne reproduit pas la marque, les couleurs, le code, les textes ni les visuels de Pear.

La palette conserve chocolat, crème, framboise et or. Le hero peut utiliser une photo alimentaire optimisée. Les animations ne portent que sur `transform` et `opacity`, sont désactivées par `prefers-reduced-motion`, et ne doivent pas imposer un calcul sur toutes les images à chaque scroll.

## 6. Vérité visuelle et performances

- Chaque pastel doit apparaître large, généreux, en demi-lune avec bord pincé épais ; jamais comme une bouchée miniature.
- Chaque crêpe doit apparaître longue, roulée souplement et épaisse ; jamais comme un mini-rouleau.
- Les box et formules affichent le contenant take-away réel comme référence et montrent exactement le nombre annoncé de pièces.
- Les ingrédients, fruits, sauces et garnitures non vendus sont exclus des photos, même s’ils figurent sur une image de référence de taille.
- Le hero est la seule image de priorité haute. Toutes les images hors écran utilisent `loading="lazy"`, des dimensions définies et un format optimisé.

## 7. Panier, accessibilité et WhatsApp

- Le bouton `−` reste visible et désactivé à quantité zéro ; les steppers ne doivent jamais ouvrir la card produit.
- Le total est marqué « estimé » lorsqu’un Pastel Gourmand est présent.
- Le supplément Banane reste distinct et ne peut être commandé sans produit éligible.
- La livraison affiche clairement que les frais exacts sont confirmés par WhatsApp lorsqu’aucun barème n’est validé.
- La géolocalisation utilise `getCurrentPosition` avec un délai de 10 secondes, une alternative adresse visible et un message d’erreur contrasté.
- Le popup de remerciement dure 7 secondes avant WhatsApp, peut être fermé ou accéléré, et doit rester accessible au clavier.

## 8. Plancher qualité

Le site est utilisable de 360 px à 1920 px, avec contraste suffisant, focus visible, cibles tactiles confortables, aucune erreur console et une réponse visuelle immédiate. Aucune preuve sociale, urgence, avis ou information commerciale ne doit être inventée.
