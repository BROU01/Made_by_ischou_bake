# État de configuration — Preview Vercel

Dernière vérification : 27 août 2026.

| Élément | État observé |
| --- | --- |
| Branche de préproduction | `admin-preview`, commit `63f4cd3` publié. |
| Déploiement Preview | Prêt, distinct de la production. |
| Variables Firebase publiques et allowlist | Sept variables ont été ajoutées à l’environnement **Preview** uniquement. |
| Clé Firebase Admin | Variable secrète limitée à **Preview**, restreinte à la branche `admin-preview`. Sa valeur n’a jamais été affichée ni inscrite dans ce dépôt. |
| Domaine Firebase Authentication | Le domaine Vercel stable de `admin-preview` a été ajouté aux domaines autorisés pour les retours de liens e-mail. |
| Connexion e-mail Firebase | Un lien de test a été reçu, ouvert avec confirmation, puis la session serveur a été créée avec succès. |
| Contrôles de routes | Les journaux Vercel confirment le refus `401` d’une requête sans session et des réponses `200` uniquement après session valide. |
| Catalogue Firestore | Les 17 références validées ont été initialisées via la session administrateur, sans commande, conversation WhatsApp ni donnée client. |
| Production | La landing publique et ses variables existantes ne doivent pas être modifiées pendant cette phase. |

Ce document ne contient ni clé, ni adresse d’administrateur, ni donnée client.
