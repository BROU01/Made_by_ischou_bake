# QA — Identité et visuels restaurés

Date de vérification : 27 août 2026  
Version GitHub : `b122bd5`  
Adresse de production : `https://ischou.vercel.app/?v=b122bd5`

## Résultats vérifiés

| Élément | Résultat |
| --- | --- |
| Logo | `logo.svg` est chargé dans la navigation et dans le footer. |
| Hero | Le typewriter contient trois états : Pastels, Crêpes et Box. Les boutons d’état sont accessibles. |
| Photos d’offres | Douze balises image sont présentes : six box et six formules, chacune reliée à un fichier explicitement nommé. |
| Cards d’offres | La production affiche six cards de box et six cards de formules, avec prix, quantité et stepper. |
| Supplément Banane | La règle reste limitée aux crêpes et aux box. La formule pastel ne propose pas de contrôle Banane. |
| Popup | Le popup de remerciement s’ouvre, le GIF est chargé, la barre a le rôle `progressbar` et le délai de sept secondes est configuré. |
| Typewriter | Un clic sur un état change le message actif. Le test a confirmé l’état Crêpes et l’écriture progressive. |
| Sélection manuelle | Après un clic sur Box, la phrase complète « Box prêtes à partager. » est restée stable après plus d’une seconde ; l’autoplay n’écrase donc pas un choix volontaire. |
| Console | Aucune erreur JavaScript n’a été observée durant le chargement et les tests. |

## Vérification manuelle conseillée à la cliente

Les photos d’offres sont intégrées à partir des fichiers fournis et associés aux cards par leur nom explicite. Avant toute campagne publique, la cliente doit confirmer sur un téléphone que chaque photo correspond visuellement au nombre de crêpes ou pastels effectivement servis, en particulier les lots de 9, 10 et 11 pièces.

Le test de commande a été contrôlé sans envoyer de message réel. WhatsApp doit être testé avec le téléphone de la cliente afin de confirmer le comportement final de l’application installée.
