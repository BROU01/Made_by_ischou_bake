# QA — Validation de livraison, partage et PWA

Date de vérification : 27 août 2026

## Contrôles locaux réalisés

| Parcours | Résultat |
| --- | --- |
| Livraison sans position ni adresse | Validé. La préparation WhatsApp est bloquée, le champ d’adresse reçoit `aria-invalid`, le message est clair et aucun popup de redirection ne s’ouvre. |
| Partage du panier | Validé avec un partage natif simulé. L’URL contient un paramètre `panier` et ne contient ni nom, ni adresse, ni coordonnées GPS. |
| Partage du site | Bouton visible dans la navigation, déclenché par un clic client. Une copie de lien est prévue lorsque le partage natif n’est pas disponible. |
| Aide à l’installation | Carte « Gardez Made by Ischou à portée de main » disponible dans les informations. Android attend l’invite du navigateur ; iPhone affiche les étapes manuelles après un clic. |

Une livraison contenant une adresse de test a également été vérifiée : le popup de préparation s’ouvre normalement et le message d’erreur de destination disparaît. Le popup a été fermé immédiatement, sans redirection vers WhatsApp.

Le partage du site a été simulé avec l’API native : il transmet le titre, le message court et uniquement l’URL racine de la page. Aucun paramètre de panier n’est ajouté au partage public du site.

La carte « Gardez Made by Ischou à portée de main » a été contrôlée dans la section Informations sur la landing locale. Elle reste lisible, séparée du supplément Banane et positionne son bouton d’installation à droite sur grand écran, sans affecter le footer ou le panier.

Un lien de panier de contrôle a été préparé avec deux crêpes Chocolat, un supplément Banane et un Pastel Classique. Les seules données encodées sont les identifiants produits, quantités et supplément associé ; les informations de livraison ne font pas partie de ce lien.

Le lien a été ouvert dans une nouvelle session locale. Le panier a bien reconstruit deux Crêpes Chocolat, un supplément Banane et un Pastel Classique, a affiché le message « Panier partagé chargé », puis a retiré le paramètre de partage de l’URL. Le visiteur arrive au hero et peut contrôler sa commande avant WhatsApp.

Les tests exécutés ici n’ont déclenché ni partage réel, ni commande WhatsApp, ni localisation réelle.
