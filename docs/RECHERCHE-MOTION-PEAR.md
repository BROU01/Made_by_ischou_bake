# Recherche de direction — Motion au scroll inspirée de Pear

Date de consultation : 27 août 2026

Cette note relève des **principes de mise en scène** observés sur [Pear](https://pear.no/). Elle ne constitue ni une copie de son code, ni une réutilisation de ses visuels, de sa marque ou de sa composition.

## Observations

La page de référence est construite comme une longue scène éditoriale. Le scroll ne se limite pas à faire apparaître des cartes : il révèle progressivement des morceaux d’une composition et rend le changement d’échelle perceptible. Au début, l’illustration reste ancrée pendant que le contenu se déplace ; une composition unique est donc découverte par fragments, avec une cadence lente et intentionnelle.

La sensation de profondeur provient du décalage modéré entre des plans visuels, des repères de grille et les textes. Les grands titres s’installent sans oscillation excessive. Les transitions paraissent continues grâce à des transformations plutôt qu’à des changements brusques de position ou de taille.

## Principes retenus pour Made by Ischou

| Principe | Adaptation originale proposée | Limite de performance |
| --- | --- | --- |
| Composition à découvrir | Révéler chaque grand moment de la carte comme un plateau : repère, titre, visuel, puis produits. | Une seule animation d’entrée par élément. |
| Profondeur | Faire varier très légèrement l’offset des visuels de section sur desktop, sans parallaxe sur les cards. | Maximum 10 à 14 px ; aucun calcul continu sur mobile. |
| Rythme lent | Allonger les entrées éditoriales à 720–900 ms avec une courbe de décélération personnalisée. | Animations uniquement sur `opacity` et `transform`. |
| Changement de chapitre | Ajouter une ligne de progression discrète ou un numéro de chapitre au début des sections clés. | CSS statique, sans bibliothèque externe. |
| Mise en avant produit | Préserver une image principale lisible au lieu d’animer simultanément toutes les cartes. | Images déjà optimisées et lazy-loaded. |

## Exclusions volontaires

Le canvas immersif de Pear, les scènes illustrées lourdes et la fixation prolongée d’éléments complexes ne seront pas portés sur cette landing. Ils seraient inadaptés à l’objectif de commande rapide, moins favorables aux appareils modestes et non nécessaires pour obtenir une sensation premium.
