# Scénario QA — Made by Ischou

Cette procédure vérifie le parcours principal d’un visiteur avant la mise en ligne. Elle ne doit pas envoyer de commande réelle pendant les essais : l’étape WhatsApp est contrôlée par la présence du remerciement, la progression et l’URL préremplie, puis validée avec un numéro de test si nécessaire.

## Préparation

Depuis la racine du dépôt, démarrez un serveur HTTP local :

```bash
python3 -m http.server 4173
```

Ouvrez ensuite :

```text
http://localhost:4173/docs/test-flow-preview.html
```

La preview charge le vrai `index.html` dans un cadre de test. Le panneau de droite sert de checklist manuelle et le bouton **Simuler la progression** ne touche pas au site ni à WhatsApp.

## Parcours nominal

| Étape | Action | Résultat attendu |
| ---: | --- | --- |
| 1 | Charger la preview puis le site dans l’iframe | Le hero, la navbar, le timer et les sections apparaissent sans erreur visible. |
| 2 | Cliquer sur Pastels, Crêpes, Box, Offres et Infos | La page défile vers la bonne section sans redirection vers une autre page. |
| 3 | Ouvrir une carte produit | La fiche détaillée s’ouvre ; le panier et la navbar restent cohérents. |
| 4 | Cliquer sur `+` puis `−` | La quantité change uniquement ; la fiche produit ne s’ouvre pas au clic sur le stepper. |
| 5 | Ouvrir le panier | Le carnet affiche les bonnes lignes, quantités et totaux. |
| 6 | Ajouter le supplément Banane | Le supplément apparaît avec sa quantité et son prix de `+200 F`. |
| 7 | Ajouter le supplément Chocolat | Le supplément apparaît avec sa quantité et son prix de `+500 F`. |
| 8 | Tester livraison et take-away | L’adresse reste disponible ; le GPS n’est demandé qu’après action ; le coût de livraison est présenté comme confirmé sur WhatsApp. |
| 9 | Ajouter un Pastel Gourmand | Le produit affiche `À partir de 350 F` ; le total devient `Total estimé`. |
| 10 | Vérifier le message WhatsApp sans l’envoyer | Les articles, quantités, suppléments, total et informations de livraison sont dans le bon ordre. |
| 11 | Cliquer sur l’envoi uniquement avec un contexte de test | L’overlay de remerciement s’affiche avant l’ouverture de WhatsApp. |
| 12 | Observer trois secondes de progression | La barre va de 0 % à 100 % et le panier n’est pas vidé avant l’ouverture. |
| 13 | Ouvrir WhatsApp | Le message est prérempli ; l’utilisateur doit encore appuyer sur Envoyer. |

## Contrôles de données métier

Vérifier que le catalogue utilise les valeurs du brief officiel :

| Donnée | Valeur attendue |
| --- | --- |
| Pastel Poisson Fumé | `250 F` |
| Pastel Classique | `300 F` — composition exacte : `Sardines.` |
| Pastel Gourmand | `À partir de 350 F` |
| Crêpe Chocolat | `500 F` |
| Crêpe Vanille | `300 F` |
| Petite Box | `3 000 F` — 5 à 6 crêpes roulées + chocolat |
| Box Classique | `4 000 F` — 8 à 10 crêpes roulées + chocolat |
| Offre 5 Pastels | `1 000 F` |
| Offre 10 Pastels | `2 000 F` |
| Supplément Banane | `+200 F` |
| Supplément Fraise | Absent |

## Contrôles mobile

Tester au minimum à 360 px de largeur. Vérifier que le menu burger, le panier plein écran, les boutons de quantité, les contrôles de livraison, la page de remerciement et le CTA WhatsApp restent utilisables sans débordement horizontal.

Tester également au clavier : Tab, Shift+Tab, Entrée, Espace et Échap. Le focus doit rester visible et le panier doit pouvoir être fermé sans souris.

## Contrôles techniques

Ouvrir la console du navigateur et confirmer qu’aucune erreur JavaScript ne se produit au chargement ou pendant le parcours. Dans l’onglet réseau, vérifier qu’aucun asset prévu ne répond en 404. Vérifier que les liens internes utilisent des ancres locales et qu’ils ne rechargent pas `index.html`.

Tester l’option de réduction des mouvements du système. Les animations décoratives et le mouvement du timer doivent être désactivés ou réduits sans supprimer l’information textuelle ni le fonctionnement du panier.

## Critères de sortie

Le site peut être considéré comme prêt lorsque les huit étapes de la preview sont cochées, que les prix correspondent au brief, qu’aucune erreur console ou 404 critique n’est présente, que le parcours mobile fonctionne à 360 px et que l’ouverture de WhatsApp ne survient qu’après la préparation visuelle prévue.
