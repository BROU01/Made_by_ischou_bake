# Recherche — Partage, panier partageable et installation PWA

Date de vérification : 27 août 2026

## Décisions d’implémentation

| Besoin | Décision retenue | Garde-fou |
| --- | --- | --- |
| Partager le site | Utiliser `navigator.share()` depuis un clic, avec copie du lien comme repli. | Aucun partage automatique ; le client choisit l’application destinataire. |
| Partager le panier | Encoder uniquement les identifiants de produits, quantités et suppléments Banane dans l’URL. | Ne jamais inclure nom, note, adresse, position GPS ou choix de livraison. |
| Validation livraison | Avant WhatsApp, demander un repère si la livraison est choisie sans adresse ni position autorisée. | Le retrait et la commande avec adresse ou GPS restent inchangés. |
| Installation Android | Manifest, icônes PNG 192/512, service worker réduit et bouton lié à `beforeinstallprompt`. | Le cache ne couvre que la coquille statique ; aucune commande ni position n’est mise en cache. |
| Installation iPhone | Afficher les étapes « Partager → Sur l’écran d’accueil » lorsque le navigateur ne propose pas d’invite d’installation. | Ne pas prétendre déclencher l’invite native iOS, car elle n’est pas programmable de la même manière. |

La fonctionnalité Web Share doit être déclenchée par une action du client et reste disponible uniquement dans les contextes sécurisés pris en charge. Une solution de copie permet de continuer sur les navigateurs qui ne la proposent pas.[1]

Un manifeste décrit l’identité et le comportement d’une application installée. Les navigateurs Chromium s’appuient notamment sur un nom, des icônes 192/512, une URL de lancement et un mode d’affichage ; l’installation demande HTTPS hors développement local.[2] Sur iPhone, l’installation passe par le menu de partage et le site doit proposer une instruction claire plutôt qu’un faux bouton d’installation automatique.[2]

## Références

[1]: https://developer.mozilla.org/en-US/docs/Web/API/Navigator/share "MDN — Navigator: share()"
[2]: https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable "MDN — Making PWAs installable"
