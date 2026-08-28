# Panneau `/adminrootonly` — trajectoire de migration Vercel

Date : 27 août 2026  
Statut : **plan validable — non déployé**

## État actuel

Le site public `ischou.vercel.app` est une landing statique. Il prépare une commande WhatsApp dans le navigateur et ne conserve localement que les quantités du panier et les suppléments Banane. Il ne contient donc pas, aujourd’hui, de base de données ni d’authentification administrateur déployées.

Le prototype local `made_by_ischou_fullstack` est une **référence fonctionnelle** : son code contient déjà un contrôle de rôle côté serveur, les structures Catalogue, Commande, Médias, Réglages et Journal d’activité. Il ne doit toutefois pas être envoyé tel quel sur Vercel ; son runtime et son authentification devront être adaptés au projet de production.

> Le chemin `/adminrootonly` est une adresse de confort, pas un mécanisme de sécurité. Le JavaScript livré au navigateur reste toujours inspectable. La protection réelle consiste à ne jamais livrer de données privées au navigateur sans session vérifiée et rôle `admin` validé côté serveur.

## Architecture recommandée

La solution la plus solide consiste à convertir le dépôt actuel en application **Next.js App Router** dans le même projet Vercel, en reproduisant à l’identique l’apparence et le comportement de la landing publique. Next.js permet de maintenir le contenu public rapide sur CDN et de réserver les opérations sensibles à des routes serveur. Vercel exécute ce code serveur sous forme de fonctions qui s’adaptent à la charge sans serveur à administrer.[1]

L’admin sera servi sous `https://ischou.vercel.app/adminrootonly`. Un proxy de route redirigera rapidement un visiteur sans session vers `/connexion`. Chaque écran admin et chaque accès aux données répéteront ensuite la vérification de session et du rôle dans le code serveur. Cette redondance est précisément le modèle conseillé par Vercel : contrôle rapide à l’entrée, puis contrôle faisant autorité au plus près des données.[2]

| Couche | Choix de mise en œuvre | Ce qu’elle protège |
| --- | --- | --- |
| Page publique | Landing conservée, optimisée et rendue statiquement. | Rapidité et référencement ; aucune donnée client persistée sans consentement. |
| Connexion | Authentification par lien à usage unique envoyé à l’adresse e-mail de l’administratrice, via un fournisseur d’identité dédié. | Pas de mot de passe écrit dans GitHub, le code ou le navigateur. |
| Session | Cookie chiffré, `httpOnly`, `secure`, `sameSite` adapté, de contenu minimal. | Réduit l’exposition d’un jeton au JavaScript de la page. |
| Route admin | `/adminrootonly` protégée par proxy ; toute lecture et mutation est aussi contrôlée dans les fonctions serveur. | Un accès direct à une URL ou une requête API ne suffit pas. |
| Autorisation | Table utilisateur avec rôle `admin` ; toutes les actions admin exigent ce rôle côté serveur. | Sépare une personne connectée d’une personne réellement autorisée. |
| Données | Base PostgreSQL managée ; fichiers média dans un stockage objet, référencés par URL et métadonnées. | Données persistantes, requêtes contrôlées, pas de fichier binaire en base. |
| Journalisation | Journal d’activité pour les changements de prix, produits, images et statuts de commande. | Traçabilité des changements sensibles. |

## Fonctionnalités du premier panneau

La première version ne cherchera pas à créer une usine à gaz. Elle reprendra seulement les modules déjà prototypes et réellement utiles : tableau d’ensemble, gestion du catalogue, commandes enregistrées avec consentement, médias, réglages et historique d’actions.

| Module | Première capacité | Règle de sécurité |
| --- | --- | --- |
| Tableau de bord | Compteurs de catalogue, commandes consenties et activité récente. | Agrégation servie uniquement après contrôle du rôle. |
| Catalogue | Modifier nom, prix, description, quantité annoncée, statut et visuel. | Validation stricte des champs et journalisation de chaque modification. |
| Commandes | Consulter le détail et passer les statuts : confirmée, préparation, livrée ou annulée. | Accès exclusivement administrateur ; ne stocker les coordonnées qu’après consentement explicite. |
| Médias | Sélectionner un visuel parmi des fichiers stockés côté serveur. | Type, taille et origine des fichiers contrôlés. |
| Réglages | Mettre à jour les informations éditoriales nécessaires. | Liste blanche de clés modifiables, sans secrets visibles. |
| Journal | Voir qui a changé quoi et quand. | Créé côté serveur et non modifiable depuis le navigateur. |

## Déroulé de migration sans casser le site public

| Étape | Action | Résultat attendu |
| --- | --- | --- |
| 1. Branche de migration | Créer une branche dédiée et répliquer visuellement la landing dans Next.js. | Le site public actuel reste disponible tant que la version n’est pas validée. |
| 2. Données | Créer les tables `users`, `catalog_products`, `orders`, `order_items`, `media_assets`, `store_settings` et `activity_logs`. | Catalogue et administration disposent d’une source de vérité. |
| 3. Identité | Connecter un fournisseur d’authentification e-mail et déclarer l’adresse du premier admin dans une variable serveur. | Première connexion sans mot de passe exposé. |
| 4. Rôles | À la première connexion autorisée, créer ou promouvoir l’utilisateur en rôle `admin` côté base. | Les utilisateurs ordinaires restent exclus des procédures admin. |
| 5. Interface | Porter le tableau de bord du prototype, puis connecter chaque action aux fonctions serveur avec validation. | Les données sensibles ne sont pas dans le bundle public. |
| 6. Vérifications | Tests automatisés d’accès refusé, validation de formulaires, contrôle des droits et essais manuels en déploiement Preview. | Aucune action admin ne dépend uniquement de l’interface. |
| 7. Bascule | Mettre la version validée en production dans le projet Vercel existant. | L’URL publique et `/adminrootonly` coexistent sous le même domaine. |

## Informations à choisir avant l’étape 3

Pour démarrer la migration, il faudra seulement confirmer l’**adresse e-mail qui recevra la connexion administrateur** et le fournisseur préféré pour l’authentification e-mail. La recommandation est une connexion par lien à usage unique, plutôt qu’un mot de passe administrateur géré artisanalement. Cette adresse ne sera jamais inscrite dans le JavaScript public ni dans Git ; elle sera configurée comme variable d’environnement sur Vercel.

La création d’un compte admin supplémentaire devra se faire depuis l’admin existant ou par mise à jour contrôlée de la base, jamais par une route publique qui permettrait de s’auto-promouvoir.

## Garanties et limites

Vercel protège l’infrastructure réseau et peut compléter la sécurité applicative, mais ne remplace pas la vérification des rôles, des sessions et des droits dans l’application elle-même.[2] Le code du frontend peut toujours être vu via les outils du navigateur ; aucun secret, mot de passe, clé d’API privée ni donnée de commande ne doit s’y trouver.

La landing actuelle continuera à ouvrir WhatsApp. L’enregistrement d’une commande en base ne sera ajouté qu’avec une case de consentement explicite, une information claire sur les données conservées et une finalité limitée à la gestion de la commande.

## Mise à jour — 28 août 2026

Une Preview statique de l'interface (« Interface » à l'étape 5 ci-dessus, uniquement la maquette visuelle) a été construite dans `preview/admin/`, à partir de l'audit d'un ZIP de maquette générique fourni par la cliente (`docs/AUDIT-ZIP-ADMIN-ORIXA.md`). Elle couvre les six modules validés ci-dessus avec l'identité Made by Ischou, des données de catalogue réelles et des exemples de commandes clairement fictifs. Elle reste isolée (`noindex`, non liée au site public, exclue de `robots.txt`) et sans authentification : les étapes 2 à 4 et 6 à 7 restent entièrement à faire avant toute bascule.

## Références

[1]: https://vercel.com/docs/functions "Vercel Functions — documentation officielle"
[2]: https://vercel.com/kb/guide/application-authentication-on-vercel "Application authentication on Vercel — guide officiel"
