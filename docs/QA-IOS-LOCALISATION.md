# QA — Géolocalisation et parcours iPhone

Date de vérification : 27 août 2026

## Cas contrôlés sans collecte réelle

| Cas simulé | Résultat attendu | Résultat observé |
| --- | --- | --- |
| Permission refusée (`code 1`) | Message clair, adresse manuelle disponible, aucun lien de carte affiché. | Validé. Le panier explique que l’autorisation peut être réactivée dans Réglages et garde le champ d’adresse. |
| Délai dépassé (`code 3`) | Une unique tentative simplifiée puis secours d’adresse. | Validé. Deux appels exactement ont été effectués, puis un message indique qu’un point de repère suffit. |
| Position autorisée | Confirmation, précision affichée, lien cartographique uniquement après consentement. | Validé. Le bouton devient « Actualiser ma position » et le lien de carte apparaît avec les coordonnées de test. |

Les coordonnées utilisées pour le test étaient simulées. Aucune position réelle n’a été demandée, enregistrée dans le navigateur ou envoyée à WhatsApp.

## Comportement iPhone prévu

Sur iPhone, le lien de vérification utilisera une URL Plans `maps.apple.com` seulement après que Safari a transmis une position autorisée. Le lien est activé par un clic explicite du client : le site ne force jamais l’ouverture de Plans, ne contourne pas l’accord iOS et ne stocke pas la position dans le panier local.

Dans les navigateurs intégrés à Instagram, Facebook ou TikTok, le panier indique qu’il peut être préférable d’ouvrir le site dans Safari. L’adresse ou le point de repère reste disponible dans tous les cas.
