# Architecture de mesure et de trafic

## Objectif

Mesurer des indicateurs utiles à la boutique — visites, pages vues, sources, ajouts au panier et intentions d’ouverture WhatsApp — sans suivre une personne ni présenter une intention comme une commande effectivement confirmée.

## Options gratuites étudiées

| Approche | Atouts | Limites | Coût et mise en place |
| --- | --- | --- | --- |
| Vercel Web Analytics | Mesure anonyme sans cookie, pages, référents et appareils dans Vercel | Les événements personnalisés ne sont pas inclus au palier Hobby ; pas de tableau intégré à l’admin à prévoir par défaut | Gratuit jusqu’à 50 000 événements mensuels, avec historique garanti d’un mois. [1] [2] |
| Google Analytics 4 seul | Standard pour suivre trafic, canaux et événements de conversion de la boutique | Les chiffres restent dans Google Analytics, pas dans `/adminrootonly` | Gratuit ; nécessite une propriété, un flux Web et un identifiant `G-…`. [3] [4] |
| Google Analytics 4 + lecture serveur | Les indicateurs sélectionnés peuvent être affichés dans l’admin sécurisé, sans secret dans le navigateur | Requiert un compte de service Google Analytics Data API, l’activation de l’API et un accès lecteur à la propriété | L’API a des quotas élevés pour des lectures quotidiennes légères. [5] [6] |

## Choix de conception

La trajectoire retenue est **Google Analytics 4 + lecture exclusivement côté serveur dans la Preview admin**, avec Vercel Web Analytics comme mesure complémentaire disponible dans Vercel. La landing envoie seulement des événements utiles et non identifiants : consultation, ajout/retrait de panier, ouverture du panier, partage, démarrage de commande et intention WhatsApp. Une intention WhatsApp n’est jamais comptée comme une commande livrée.

Le tableau de bord reprend la densité de la référence fournie : indicateurs réels sur une période explicite, comparaison éventuelle uniquement lorsque des données historiques existent, puis tableau des événements et origine du trafic. Il ne montre pas de chiffre d’affaires, d’avis, de clients, de localisation précise ou de commande inventés.

Le navigateur recevra uniquement l’identifiant public de mesure Google Analytics. L’identifiant de propriété, l’identité de lecture Analytics et sa clé resteront dans les variables Vercel et ne seront utilisés que par les routes protégées par la session Firebase.

## Références

[1]: https://vercel.com/docs/analytics/limits-and-pricing "Pricing for Web Analytics — Vercel"
[2]: https://vercel.com/docs/analytics "Vercel Web Analytics"
[3]: https://support.google.com/analytics/answer/9304153?hl=fr "Configurer Analytics pour un site Web et/ou une application — Google"
[4]: https://support.google.com/analytics/answer/12270356?hl=fr "ID de mesure GA4 — Google"
[5]: https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart "Google Analytics Data API quickstart"
[6]: https://developers.google.com/analytics/devguides/reporting/data/v1/quotas "Data API limits and quotas"
