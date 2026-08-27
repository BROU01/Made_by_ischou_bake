# Préproduction Firebase — Made by Ischou Admin

Date de création : 27 août 2026  
Statut : projet Firebase créé, Firestore et Authentication configurés ; la branche `admin-preview` contient désormais l’intégration Vercel isolée à configurer puis tester.

| Élément | Valeur |
| --- | --- |
| Nom du projet | Made by Ischou Admin |
| Identifiant technique | `made-by-ischou-admin` |
| Forfait initial | Spark sans facturation activée |
| Google Analytics | Désactivé à la création |
| Gemini dans Firebase | Désactivé à la création |
| Finalité | Préproduction du panneau sécurisé `/adminrootonly` ; aucune bascule de la landing publique. |

## Services configurés

Cloud Firestore a été créé en édition Standard, en région `africa-south1` (Johannesburg), avec le mode production. Firebase Authentication est activé avec le fournisseur e-mail et la connexion sans mot de passe par lien e-mail. Une application web de préproduction est enregistrée ; Firebase Hosting est volontairement désactivé, car Vercel reste l’hébergeur du projet. Le domaine public Vercel actuellement utilisé est autorisé dans Firebase Authentication pour permettre le retour des liens de connexion e-mail.

La règle Firestore publiée est le refus par défaut (`allow read, write: if false`). Aucune collection, y compris les futures commandes, ne peut être lue ou modifiée directement par un navigateur. Le serveur Vercel utilise Firebase Admin SDK, qui est volontairement le seul chemin d’accès aux données administratives.

Firebase Storage sera activé seulement lorsqu’il sera nécessaire pour les photos pilotées depuis l’admin et après vérification du forfait et des règles associées. Les clés, jetons, identifiants de service et configurations de production ne doivent jamais être consignés dans ce fichier ou dans Git.

## Sécurité prévue

Le premier compte administrateur sera déclaré dans la variable Vercel `ADMIN_ALLOWED_EMAILS`, jamais dans le code, Git ou le navigateur. La route de connexion reçoit un jeton Firebase vérifié, le convertit en cookie HTTP-only à durée limitée et réévalue l’allowlist serveur à chaque requête administrative. Les collections de commandes ne contiendront des informations client qu’après un consentement explicite intégré au parcours futur.

## Variables Vercel à renseigner hors Git

| Variable | Rôle | Emplacement |
| --- | --- | --- |
| `FIREBASE_PROJECT_ID` | Identifie le projet Firebase pour les fonctions serveur. | Preview et Production (lors de la bascule seulement) |
| `FIREBASE_CLIENT_EMAIL` | Compte de service Firebase Admin. | Preview et Production |
| `FIREBASE_PRIVATE_KEY` | Clé privée du compte de service, avec les retours à la ligne encodés `\\n`. | Preview et Production |
| `FIREBASE_WEB_API_KEY` | Configuration du SDK Firebase dans la page de connexion. | Preview et Production |
| `FIREBASE_WEB_AUTH_DOMAIN` | Domaine Firebase Authentication de l’application web. | Preview et Production |
| `FIREBASE_WEB_APP_ID` | Identifiant de l’application web Firebase. | Preview et Production |
| `FIREBASE_WEB_MESSAGING_SENDER_ID` | Identifiant public de messagerie de l’application web. | Preview et Production |
| `ADMIN_ALLOWED_EMAILS` | Allowlist serveur, une ou plusieurs adresses séparées par des virgules. | Preview et Production |

Les variables de type `FIREBASE_WEB_*` sont une configuration web et non des secrets cryptographiques ; elles restent néanmoins hors Git afin de séparer les environnements et de limiter leur diffusion. Les deux valeurs réellement sensibles sont la clé privée et la liste des administrateurs.
