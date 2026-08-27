# QA — Retour au hero sur iPhone, Android et PWA

Date : 27 août 2026

## Diagnostic vérifié

L’analyse externe partagée utilisait l’URL `https://ischou.vercel.app/#infos`. Cette adresse demande explicitement l’ancre `#infos` : elle ouvre donc volontairement la section Informations, en bas de la landing. Ce comportement ne doit pas être confondu avec le bug de restauration de scroll à l’URL racine.

Le site conserve désormais ce comportement volontaire pour les ancres telles que `#infos` ou `#offres`, tout en renforçant le retour au hero lorsqu’aucune ancre n’est présente.

## Correctif mobile

| Élément | Protection appliquée |
| --- | --- |
| Historique navigateur | `history.scrollRestoration` est défini sur `manual`. |
| Retour au hero | Le site remet la position à zéro immédiatement, puis après six délais courts couvrant les restaurations tardives. |
| Verrou initial | Pendant 2,6 secondes au démarrage, une boucle `requestAnimationFrame` limitée maintient le hero à l’écran si Safari ou Chrome restaure tardivement une ancienne position. |
| Reprise de PWA | Un retour au premier plan déclenche le même contrôle tant que le client n’a pas commencé à naviguer. |
| Intention client | Le premier toucher, clic, geste de molette ou raccourci clavier arrête la remise automatique au hero. |
| Ancre volontaire | Les fragments d’URL ne sont jamais écrasés. |

Les quatre tests automatisés du site sont passés après l’ajout de cette protection : motion et scroll, géolocalisation iPhone, partage/PWA et confidentialité des liens de panier.

## Validation Vercel

La version publique du commit `5be1da0` a été ouverte sans fragment. Elle démarre au hero (`scrollY : 0`), utilise `history.scrollRestoration = "manual"` et contient le verrou initial de 2,6 secondes. Le service worker actif est bien `https://ischou.vercel.app/sw.js` ; sa stratégie est réseau d’abord et ne doit donc pas servir une ancienne page lorsque le client est connecté.
