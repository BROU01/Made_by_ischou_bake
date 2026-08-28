# Audit du ZIP « admin » fourni — panneau générique ORIXA

Date : 28 août 2026
Statut : audit de cartographie — **rien de ce ZIP n'a été exécuté ni importé tel quel.**

## Contenu réel du ZIP

Le ZIP ne contient que 12 pages HTML (`admin/*.html`) : `index`, `commandes`, `clients`, `produits`, `collections`, `reductions`, `personnalisation`, `pages`, `menus`, `medias`, `utilisateurs`, `reglages`. Il ne contient **ni** `assets/css/admin.css`, **ni** `assets/js/{admin,catalog,content}.js`, **ni** images. Chaque page référence ce CSS/JS manquant : le ZIP n'est donc pas exécutable en l'état, seulement lisible comme plan d'écrans.

## De quoi s'agit-il

C'est la maquette d'un back-office **générique multi-boutique** nommé « ORIXA », pensé pour une épicerie en ligne avec paiement intégré (T-Money, Flooz, carte, virement), comptes clients, codes de réduction, thème personnalisable et pages CMS. Ce n'est ni une marque ni un code de Made by Ischou : il sert uniquement de référence de structure et d'interactions.

## Cartographie des écrans

| Écran | Rôle dans ORIXA | Compatible avec le scope validé Made by Ischou ? |
| --- | --- | --- |
| `index.html` | Tableau de bord : 4 KPI (CA, commandes, panier moyen, références), dernières commandes, stock faible | Oui, à adapter (pas de CA en ligne réel tant qu'il n'y a pas de paiement web) |
| `commandes.html` | Table commandes avec recherche, filtre statut, changement de statut inline, export CSV | Oui — correspond au suivi de statut décrit dans `FEUILLE-DE-ROUTE-COMMANDES-SEO-ADMIN.md` |
| `produits.html` | CRUD produit (nom, prix, stock, rayon, provenance, badge, image via sélecteur média), sélection multiple, actions groupées | Oui pour l'édition catalogue ; **non** pour « rayon/provenance/stock », concepts d'épicerie sans équivalent validé |
| `medias.html` | Galerie d'images groupées, upload en `data:` URL stocké navigateur | Utile comme UX, mais le stockage `data:` en `localStorage` ne tient pas à l'échelle — nécessite un vrai stockage objet serveur, déjà noté dans `ADMIN-VERCEL-MIGRATION.md` |
| `reglages.html` | Infos boutique, frais de livraison, **moyens de paiement en ligne**, export/import JSON, reset | Partiellement : livraison oui ; paiement en ligne **non**, Made by Ischou commande exclusivement via WhatsApp |
| `clients.html` | Fiches client avec total dépensé, historique | **Hors scope** : la landing ne doit jamais afficher d'historique public ni un profil client agrégé sans base réelle et consentement |
| `collections.html` | Rayons de la boutique en ligne | **Hors scope** : pas de multi-rayons, un catalogue à plat suffit |
| `reductions.html` | Codes promo | **Hors scope** : aucune réduction validée par la cliente |
| `personnalisation.html` | Thème/couleurs du site | **Hors scope** : la direction visuelle est déjà fixée dans `AGENTS.md` |
| `pages.html`, `menus.html` | CMS de pages et navigation | **Hors scope** : la landing reste mono-page, une seule navigation par ancres |
| `utilisateurs.html` | Comptes et rôles multiples | **Hors scope pour la V1** : un seul rôle admin (la cliente) est prévu |

## Patterns UX à réutiliser (indépendants du code, reproduits proprement)

- Barre latérale groupée par catégories, lien retour « Voir la boutique », bandeau utilisateur connecté.
- Bandeau d'avertissement en haut d'écran quand des données sont fictives/démo.
- Recherche + filtre select au-dessus d'un tableau, normalisation des accents pour la recherche.
- Pastilles de statut colorées (`pill--ok/warn/danger/neutral`).
- Modale de formulaire produit avec sélecteur média dédié plutôt qu'un champ URL nu.
- Export CSV/JSON et un bouton de réinitialisation explicite avec confirmation.
- Lien « squelette de navigation » = accessibilité de base (`skip-link`, `aria-label`, `visually-hidden`).

## Ce qui est explicitement rejeté

- Le nom, la marque et les couleurs « ORIXA » ne sont pas repris.
- Tout module de paiement en ligne, réduction, compte client, thème ou CMS hors scope validé.
- Le stockage `localStorage`/`data:` comme unique persistance : rappelé comme démonstratif uniquement, jamais une solution de production (cf. `ADMIN-VERCEL-MIGRATION.md`).
- Aucun identifiant, jeton ou donnée du ZIP n'a été copié : il n'y en avait aucun dans les fichiers fournis.

## Suite donnée

La Preview `/adminrootonly` a été reconstruite dans `preview/admin/` en reprenant uniquement les patterns ci-dessus, limitée aux six modules déjà validés dans `docs/ADMIN-VERCEL-MIGRATION.md` (Tableau de bord, Commandes, Produits, Médias, Réglages, Journal d'activité), avec l'identité graphique Made by Ischou et des données explicitement fictives. Voir `preview/admin/README.md`.
