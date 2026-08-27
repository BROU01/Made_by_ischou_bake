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
| Reprise de PWA | Un retour au premier plan déclenche le même contrôle tant que le client n’a pas commencé à naviguer. |
| Intention client | Le premier toucher, clic, geste de molette ou raccourci clavier arrête la remise automatique au hero. |
| Ancre volontaire | Les fragments d’URL ne sont jamais écrasés. |

Les quatre tests automatisés du site sont passés après l’ajout de cette protection : motion et scroll, géolocalisation iPhone, partage/PWA et confidentialité des liens de panier.
