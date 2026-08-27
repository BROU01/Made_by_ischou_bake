# Feuille de route — Commandes, SEO, performance et administration

Date : 27 août 2026  
Statut : recommandations fondées sur l’audit de la landing Vercel actuelle et du prototype full-stack local.

## Décision sur l’historique de commandes

Le site public ne doit pas afficher une liste publique de « commandes récentes ». Cette liste révélerait des informations sur d’autres clients et serait particulièrement inadaptée aux commandes de quartier. Aujourd’hui, la commande est finalisée dans WhatsApp et la landing statique n’enregistre aucun événement côté serveur ; elle ne peut donc pas connaître de manière fiable l’état réel d’une commande.

L’option correcte est un **suivi individuel et privé**, à ajouter avec le futur backend. Après accord explicite, le site crée une référence de commande et la transmet dans le message WhatsApp. La cliente met ensuite le statut à jour dans son admin. Le client peut consulter uniquement sa propre commande grâce à un lien contenant un jeton opaque, imprévisible et limité dans le temps. Aucune recherche par prénom, numéro de téléphone ou simple numéro séquentiel ne doit être proposée.

| Élément | Landing statique actuelle | Avec backend sécurisé |
| --- | --- | --- |
| Historique général visible sur le site | À ne pas ajouter. | À ne pas ajouter. |
| Dernière commande du client | Non fiable, car WhatsApp confirme hors site. | Possible avec référence privée et accord du client. |
| Statuts « reçue », « en préparation », « livrée » | Non disponible. | L’administratrice les met à jour dans l’admin. |
| Coordonnées de livraison | Non conservées. | Conservées seulement avec consentement, accès admin et durée de conservation définie. |
| Message WhatsApp | Préparé dans le navigateur. | Préparé avec la référence de commande, sans automatisation trompeuse. |

> **Point essentiel :** WhatsApp ne remontera pas automatiquement l’état d’une commande sur le site. Au départ, la cliente devra passer le statut elle-même dans le panneau admin. Une automatisation ultérieure exigerait une intégration officielle WhatsApp Business et des webhooks signés.

## Panneau `/adminrootonly` : méthode recommandée

La bonne trajectoire consiste à effectuer une migration contrôlée du dépôt vers **Next.js App Router**, sans interrompre la landing publique. La page publique reste pré-rendue et servie rapidement par Vercel ; les données, rôles et mutations sensibles passent exclusivement par le serveur.

Le prototype local contient déjà les modèles Catalogue, Commandes, Médias, Réglages et Journal d’activité, ainsi qu’un contrôle de rôle `admin` côté serveur. Il fournit une base utile mais ne doit pas être déclaré déployé sur Vercel tant que les éléments ci-dessous ne sont pas construits et validés.

| Étape | Travaux | Résultat attendu |
| --- | --- | --- |
| 1. Préproduction | Créer une branche et un déploiement Preview, puis reproduire visuellement la landing actuelle. | Le site public reste disponible durant la migration. |
| 2. Données | Connecter une base PostgreSQL gérée, créer `users`, `catalog_products`, `orders`, `order_items`, `media_assets`, `store_settings` et `activity_logs`. | Une source de vérité pour le catalogue et les commandes consenties. |
| 3. Connexion | Ajouter un fournisseur d’authentification e-mail à lien à usage unique et configurer l’adresse du premier administrateur dans des variables serveur. | Aucun mot de passe ou jeton privé dans GitHub ou le navigateur. |
| 4. Rôles | Contrôler la session et le rôle `admin` dans chaque route, lecture et écriture sensible. | Le chemin `/adminrootonly` seul ne suffit jamais à obtenir un accès. |
| 5. Modules admin | Porter le tableau de bord, le catalogue, les commandes, les médias, les réglages et le journal d’activité. | La cliente peut gérer les produits et les statuts de manière centralisée. |
| 6. Suivi privé | Générer une référence et un lien de suivi limité ; ajouter consentement, politique de conservation et suppression. | Le client ne voit que sa commande, jamais celles d’autrui. |
| 7. Tests et bascule | Tester les droits refusés, les validations de formulaire, les rôles, le partage de lien et les Preview Deployments. | L’URL publique et l’admin coexistent dans le même projet Vercel. |

Le premier choix requis avant de démarrer les étapes 2 et 3 est l’**adresse e-mail de la personne qui doit être le premier administrateur**. Il faudra aussi choisir le fournisseur de lien de connexion. Cette adresse sera enregistrée comme variable d’environnement dans Vercel, jamais dans le JavaScript public ni dans Git.

## Optimisations prioritaires de performance

La réponse HTML publique mesurée le 27 août 2026 renvoyait un statut 200, avec un TTFB observé de 0,21 s sur cache Vercel et un document HTML d’environ 82 Ko. Les cartes produits utilisent déjà le chargement différé et le hero reçoit une priorité de chargement. Le travail utile consiste donc à réduire les octets les plus coûteux et à mesurer les résultats, plutôt qu’à ajouter des effets décoratifs.

| Priorité | Optimisation | Effet recherché | Précaution |
| --- | --- | --- | --- |
| 1 | Charger le GIF du popup uniquement à l’ouverture de la confirmation. | Réduit les données initiales pour les visiteurs qui ne commandent pas. | Le GIF doit rester visible dès l’ouverture du popup. |
| 2 | Produire une variante moderne et responsive du hero avec une image de repli JPEG. | Réduit le poids du plus grand visuel visible sans dégrader l’image sur les appareils non compatibles. | Préserver l’image authentique et ses dimensions réservées pour éviter les sauts de mise en page. |
| 3 | Ajouter un budget de performance mesuré dans Lighthouse et Search Console. | Surveille LCP, INP et CLS avec des données de terrain lorsque le trafic sera suffisant. | Ne pas optimiser uniquement un score de laboratoire. |
| 4 | Réduire la police et les graisses réellement utilisées après un audit de couverture. | Évite le téléchargement de variantes de police inutiles. | Conserver le logo et les contrastes actuels. |
| 5 | Conserver les motions seulement en `transform` et `opacity`, déjà limitées sur mobile. | Évite des calculs coûteux pendant le scroll. | Aucune parallaxe continue sur petits écrans. |

Google recommande de suivre les Core Web Vitals, qui couvrent chargement, interactivité et stabilité ; les cibles indicatives sont LCP sous 2,5 s, INP sous 200 ms et CLS sous 0,1.[1] Ces indicateurs n’assurent pas à eux seuls un classement élevé, mais ils sont de bons garde-fous pour l’expérience mobile.[2]

## Optimisations SEO local et partage social

| Priorité | Optimisation | État actuel | Conditions de qualité |
| --- | --- | --- | --- |
| 1 | Ajouter une balise canonique, les balises Open Graph et une carte X. | À ajouter. | Réutiliser une vraie photo et le vrai nom de la marque ; aucun avis ou promesse inventé. |
| 2 | Créer `robots.txt` et `sitemap.xml`, puis déclarer le site dans Google Search Console. | À ajouter. | Le compte Google du propriétaire devra confirmer le domaine et soumettre le sitemap. |
| 3 | Ajouter un JSON-LD `FoodEstablishment` ou `Restaurant` minimal. | À ajouter. | Inclure uniquement nom, adresse réellement affichée, téléphone, URL et menu ; ne pas créer d’horaires précis, notes ou avis non vérifiés. |
| 4 | Créer ou compléter le profil Google Business avec les mêmes coordonnées. | Action de la cliente. | Coordonnées, photos et horaires doivent être réels et cohérents avec le site. |
| 5 | Contrôler les aperçus WhatsApp, Facebook et Instagram après ajout des balises. | À tester. | L’image sociale doit charger vite et rester fidèle aux portions vendues. |

Les données structurées peuvent aider les moteurs à comprendre le contenu et parfois enrichir l’affichage, mais Google ne garantit pas qu’un résultat enrichi sera affiché. Il est préférable de fournir peu de données, mais des données complètes et exactes.[3] Pour le balisage d’un commerce local, Google exige notamment un nom et une adresse, et recommande d’indiquer le téléphone, l’URL, le menu et seulement les autres informations réellement publiées.[4]

## Optimisations de conversion sans manipulation

L’amélioration la plus utile est de réduire les incertitudes au moment de commander. Les fonctions récemment ajoutées — vérification de la livraison, panier partageable, partage natif et installation sur l’écran d’accueil — répondent déjà à ce principe.

| Action suivante | Raison | Dépendance |
| --- | --- | --- |
| Aperçu social fiable | Les liens partagés présentent clairement la marque et la photo hero dans WhatsApp et les réseaux. | Balises Open Graph. |
| FAQ courte dans Infos | Répond aux questions de retrait, livraison, Banane et préparation avant d’ouvrir WhatsApp. | Valider chaque réponse avec la cliente. |
| Mesure anonyme du tunnel | Compter les clics catalogue, panier, partage et préparation WhatsApp. | Politique de confidentialité courte et outil d’analytique configuré. |
| Disponibilités administrables | Afficher uniquement les produits momentanément disponibles ou indisponibles. | Panneau admin et base de données. |
| Suivi privé de commande | Réduit les demandes de suivi dans WhatsApp lorsque la cliente met les statuts à jour. | Backend, consentement et admin. |

## Ordre de mise en œuvre conseillé

1. **SEO et partage social** : balises canonique/Open Graph, `robots.txt`, `sitemap.xml` et JSON-LD minimal après validation des informations métier.
2. **Performance ciblée** : chargement différé du GIF, formats modernes et audit Lighthouse mobile.
3. **Préproduction admin** : branche Preview, conversion technique vers Next.js, puis base de données et connexion e-mail.
4. **Gestion catalogue et commandes consenties** : modules admin, journal d’activité et règles de conservation.
5. **Suivi individuel privé** : uniquement après l’étape précédente et après validation du texte de consentement.

## Références

[1]: https://developers.google.com/search/docs/appearance/core-web-vitals "Google Search Central — Core Web Vitals"
[2]: https://developers.google.com/search/docs/appearance/page-experience "Google Search Central — Page experience"
[3]: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data "Google Search Central — Introduction aux données structurées"
[4]: https://developers.google.com/search/docs/appearance/structured-data/local-business "Google Search Central — Données structurées LocalBusiness"
