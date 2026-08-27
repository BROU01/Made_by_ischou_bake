# Diagnostic — Rechargement et position de scroll

Date : 27 août 2026

## Reproduction

La page publique a été vérifiée à l’URL racine cache-bustée, sans ancre dans l’URL. La page a une hauteur de 7 020 px pour une fenêtre de 1 100 px. Après une navigation déjà descendue, le navigateur était en position basse (`scrollY` observé : 5 338 px) et l’historique était réglé sur la restauration automatique (`history.scrollRestoration = "auto"`).

Cette restauration native peut reprendre la dernière position de lecture sur un rechargement et explique le symptôme signalé. Aucun élément n’avait le focus ; la cause n’est donc pas un focus forcé du panier ou d’un formulaire.

## Correction prévue

La page désactivera la restauration automatique dès le `<head>`, puis forcera l’URL racine sans fragment à revenir à `scrollY = 0` au chargement et après l’événement `pageshow`. Une URL volontairement ancrée, telle que `#offres`, continuera de respecter son ancre.

Le premier essai automatisé de rechargement n’a pas permis de confirmer le retour au hero : la position basse était toujours observée après l’action de rechargement du navigateur. La correction est donc renforcée avec plusieurs reprises légères après `load` et `pageshow`, afin de couvrir une restauration tardive du navigateur. Cette répétition ne s’exécute qu’au chargement et ne crée aucune boucle pendant le scroll.

Une nouvelle navigation sans fragment vers l’instance locale corrigée ouvre bien le hero (`Pixels above viewport : 0`). Les actions de test ont également montré qu’un navigateur pouvait tenter de restituer une position tardivement ; la correction finale associe donc `history.scrollRestoration = "manual"`, une remise à zéro immédiate, une reprise à la frame suivante et trois reprises courtes jusqu’à 900 ms après le chargement.

## Motion à renforcer

Les reveals existants fonctionnent mais leur profondeur est trop discrète pour être immédiatement ressentie. La correction renforcera les décalages d’entrée des chapitres, la cadence des éléments narratifs et les deux plans de profondeur desktop. Les animations resteront limitées à `transform` et `opacity`, sans canvas ni boucle active hors viewport.

Les amplitudes ont été portées à 26 px pour le visuel Crêpes et 18 px pour l’orbite décorative des Offres, avec des arrivées de titre, texte et repère de chapitre visiblement séquencées. Ces éléments restent désactivés sous 960 px et lorsque les mouvements réduits sont demandés.

## Contrôle des ancres

Une navigation explicite vers `#offres` conserve sa destination (`Pixels above viewport : 3 344`) et affiche bien le chapitre Offres. Le retour automatique au hero ne s’applique donc pas lorsqu’un visiteur demande volontairement une section avec un lien interne.
