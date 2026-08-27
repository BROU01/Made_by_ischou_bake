# Comparaison — Bases de données freemium hors Supabase

Date : 27 août 2026  
Contexte : panneau administrateur Made by Ischou hébergé sur Vercel, avec catalogue, commandes consenties, médias, journal d’activité et premier administrateur par e-mail.

## Candidats vérifiés

| Solution | Modèle | Ce qu’elle couvre | Compatibilité Vercel | Limite à connaître |
| --- | --- | --- | --- | --- |
| **Firebase** | Cloud Firestore (documents) + Firebase Authentication | Base, connexion, stockage et règles d’accès dans le même écosystème. | Compatible avec Next.js/Vercel, via SDK serveur et variables d’environnement. | Les requêtes ne sont pas SQL et la séparation lecture/écriture doit être pensée avec attention. |
| **Neon** | PostgreSQL serverless | Base SQL relationnelle, très adaptée aux commandes et lignes de commande. | Intégration Vercel documentée ; Drizzle reste compatible. | L’authentification e-mail et le stockage média doivent être ajoutés séparément. |
| **Turso** | SQLite distribué / libSQL | Base légère et rapide pour un petit catalogue et des commandes. | Intégration Vercel disponible. | L’authentification e-mail et le stockage média restent des services distincts. |

## Solution recommandée : Firebase

Pour le premier admin et une activité locale, **Firebase** est la solution freemium la plus simple à administrer : Firestore fournit une base de documents, Firebase Authentication prend en charge la connexion e-mail, et Firebase Storage peut héberger les médias. Le panneau admin Next.js s’exécute sur Vercel mais parle à Firebase uniquement via des accès serveur contrôlés pour les opérations sensibles.

La documentation Firebase indique que l’authentification permet d’identifier les utilisateurs et de contrôler l’accès aux données, avec prise en charge des comptes e-mail et des fournisseurs fédérés.[1] Firestore propose, pour un seul projet sans facturation, un quota gratuit de 1 Gio stocké, 50 000 lectures par jour, 20 000 écritures par jour, 20 000 suppressions par jour et 10 Gio de transfert sortant mensuel.[2] Ces plafonds doivent être surveillés dans la console Firebase ; ils sont suffisants pour démarrer mais ne constituent pas une promesse de gratuité illimitée.

| Couche | Choix Firebase recommandé | Garde-fou |
| --- | --- | --- |
| Connexion admin | Lien de connexion e-mail ou connexion Google limitée au compte administrateur. | Restreindre la liste des e-mails autorisés côté serveur. |
| Autorisation | Collection `users` avec `role: "admin"`, vérifiée sur le serveur Next.js. | Ne jamais se fier seulement aux règles visibles dans l’interface. |
| Commandes | Collections `orders` et `orderItems`, créées après consentement. | Pas de données de livraison sans finalité, consentement et durée de conservation définie. |
| Catalogue | Collection `products`, lue publiquement seulement si le produit est actif. | Écriture réservée à l’administrateur. |
| Médias | Firebase Storage ou stockage objet séparé. | Filtrer taille, type et origine du fichier avant l’envoi. |
| Journal | Collection `activityLogs` écrite depuis le serveur. | Le navigateur ne peut pas modifier le journal. |

## Quand choisir Neon à la place

Neon est préférable si l’on souhaite garder un modèle strictement relationnel dès le départ : une commande, ses lignes, ses produits et les rôles admin se représentent naturellement dans PostgreSQL. Neon indique que son offre gratuite via Vercel fournit jusqu’à 512 Mo de stockage et 190 heures de calcul ; Drizzle est compatible.[3] Cette voie implique toutefois de sélectionner et configurer séparément la connexion e-mail ainsi que le stockage des médias.

## Décision à confirmer

La prochaine étape est de choisir entre :

1. **Firebase** : le plus simple pour démarrer sans Supabase avec une connexion e-mail et une base dans le même projet ;
2. **Neon + un fournisseur d’authentification** : meilleure structure SQL, mais deux services à configurer ;
3. **Turso + un fournisseur d’authentification** : option légère, mais également composée de plusieurs services.

La recommandation par défaut est **Firebase**, sous réserve que la cliente accepte de créer ou connecter un projet Firebase et que les règles soient validées en Preview avant la mise en production.

## Références

[1]: https://firebase.google.com/docs/auth "Firebase Authentication — documentation officielle"
[2]: https://firebase.google.com/docs/firestore/quotas "Cloud Firestore — quotas et limites"
[3]: https://neon.com/docs/guides/vercel-postgres-transition-guide "Neon — guide Vercel Postgres"
