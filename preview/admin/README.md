# Preview `/adminrootonly` — aperçu statique, non sécurisé

Ce dossier est un **aperçu visuel** de ce à quoi ressemblera l'administration Made by Ischou une fois le backend construit. Il sert à valider l'interface avec la cliente avant tout développement du panneau réel.

## Ce que cet aperçu N'EST PAS

- Ce n'est pas un panneau sécurisé : il n'y a ni authentification, ni session, ni rôle vérifié côté serveur.
- Ce n'est pas connecté au site public : modifier un produit ou un statut de commande ici n'a aucun effet sur `index.html` ni sur WhatsApp.
- Ce n'est pas une source de données réelle pour les commandes ou le journal : ces écrans utilisent des exemples fictifs, clairement annotés.
- Cette URL n'est protégée par aucun mécanisme : un chemin non référencé n'est jamais une sécurité (voir `docs/ADMIN-VERCEL-MIGRATION.md`).

## Ce que cet aperçu contient

Six écrans correspondant aux modules déjà validés dans `docs/ADMIN-VERCEL-MIGRATION.md` :

1. Tableau de bord
2. Commandes (exemples fictifs)
3. Produits (catalogue réel et public, éditable en local uniquement)
4. Médias (référence des visuels déjà présents dans le dépôt)
5. Réglages (informations boutique réelles, édition locale seulement)
6. Journal d'activité (exemples + actions faites dans cet aperçu)

Chaque modification est stockée uniquement dans le `localStorage` du navigateur, sous la clé `made-by-ischou-admin-preview-v1`, distincte du panier public. Le bouton « Réinitialiser l'aperçu » dans Réglages efface ces données locales.

## Origine

L'interface reprend des patterns UX (barre latérale, recherche/filtre, pastilles de statut, modale d'édition) observés dans un ZIP de maquette générique fourni par la cliente — voir `docs/AUDIT-ZIP-ADMIN-ORIXA.md` pour le détail de ce qui a été gardé et de ce qui a été écarté. Aucun code, image, identifiant ou donnée de ce ZIP n'a été copié tel quel.

## Suite

Cet aperçu ne devient un panneau exploitable qu'après les étapes décrites dans `docs/ADMIN-VERCEL-MIGRATION.md` et `docs/FEUILLE-DE-ROUTE-COMMANDES-SEO-ADMIN.md` : choix d'un backend, d'une base de données, d'une authentification par lien e-mail à usage unique, et d'un contrôle de rôle `admin` côté serveur.
