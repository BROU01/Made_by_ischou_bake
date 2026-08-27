# Recherche — Géolocalisation, Plans et iPhone

Date de consultation : 27 août 2026

## Principes techniques confirmés

La géolocalisation web est disponible uniquement dans un contexte sécurisé HTTPS et nécessite toujours l’autorisation explicite de la personne. Le navigateur peut retourner trois causes standard : permission absente ou refusée (`1`), position indisponible (`2`) ou délai dépassé (`3`). Le texte brut renvoyé par le système est destiné au débogage et ne doit pas être affiché tel quel au client.[1] [2]

Sur iPhone, les services de localisation dépendent des réglages de confidentialité et de localisation de l’appareil. Apple précise que l’utilisateur peut accorder, modifier ou retirer l’accès à tout moment, et qu’une application ou un site ne peut pas utiliser une position avant l’autorisation de la personne.[3]

Les URL Plans d’Apple peuvent ouvrir un point déterminé à partir de ses coordonnées. Une URL `https://maps.apple.com/place?coordinate=latitude,longitude&name=...` est donc pertinente **après** qu’une position a été capturée avec consentement. Apple propose également une URL de localisation courante, mais celle-ci exige une permission accordée à Plans.[4]

## Décisions d’implémentation

| Situation | Réponse dans le panier |
| --- | --- |
| Première demande | Expliquer que la position sert uniquement à préparer le message WhatsApp et déclencher la demande système au clic. |
| Accord et position reçue | Afficher la confirmation, ne conserver la position qu’en mémoire, présenter un lien explicite « Ouvrir dans Plans pour vérifier ». |
| Refus ou permission déjà bloquée | Ne jamais essayer d’ouvrir Plans de force. Expliquer que l’adresse manuelle reste suffisante et indiquer comment réautoriser si souhaité. |
| Délai ou précision GPS indisponible | Essayer une seule fois un positionnement réseau moins exigeant, puis basculer proprement vers l’adresse manuelle. |
| Navigateur Instagram, Facebook ou TikTok | Signaler que le navigateur intégré peut limiter la demande ; inviter à ouvrir le site dans Safari et conserver l’adresse manuelle. |
| iPhone sans Plans ou autre appareil | Le lien « vérifier la position » reste un lien cartographique web universel au lieu d’être une dépendance à une application installée. |

La position ne sera pas enregistrée dans `localStorage`. Elle est seulement incluse dans le message WhatsApp si le client choisit de poursuivre la commande après consentement.

## Références

[1]: https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API "MDN — Geolocation API"
[2]: https://developer.mozilla.org/en-US/docs/Web/API/GeolocationPositionError "MDN — GeolocationPositionError"
[3]: https://support.apple.com/en-us/102515 "Apple Support — Privacy and Location Services"
[4]: https://developer.apple.com/documentation/mapkit/unified-map-urls "Apple Developer — Unified Maps URLs"
