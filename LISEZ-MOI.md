# Made by Ischou — site de commande WhatsApp

Le seul livrable applicatif est `index.html` : HTML, CSS et JavaScript inline, sans build ni serveur. La commande ouvre un message WhatsApp pré-rempli ; aucun paiement n'est traité sur le site.

## Catalogue et commandes

Le catalogue, les prix et les règles d'affichage sont définis exclusivement dans `PROMPT-CODEX-MAJ-CATALOGUE.md`. Ne pas reprendre les anciens flyers ni modifier un prix directement dans le code.

Les clients peuvent composer leur commande du vendredi 00h00 au jeudi 12h00 (heure de Lomé, UTC+0), pour une livraison le jeudi à partir de 12h00. Les commandes ferment le jeudi à 20h00 ; le site les rouvrira techniquement vendredi à 00h00 pour le cycle suivant.

Le numéro qui reçoit les commandes est **71 30 39 11** (`22871303911`). Le **97 11 56 38** reste un contact téléphonique affiché sur le site.

## Photos

Les six photos source sont déposées dans `assets/pastels_et_crepes_jpeg/` :

- `pastel-classique.jpg`
- `pastel-gourmand.jpg`
- `pastel-poisson-fume.jpg`
- `crepe-chocolat.jpg`
- `crepe-vanille.jpg`

Lors de l'intégration, les copies retenues devront être placées dans `assets/` sous le nom exact `assets/{id}.jpg`. Il n'y a pas de photo héros : le héros est le rythme hebdomadaire. La page doit rester convaincante même si une photo est indisponible.

## Maintenance — semaines d'exception

Le timer fonctionne automatiquement, sans aucune intervention. Si la commerçante doit suspendre ou déplacer une fournée, elle édite le fichier `assets/exceptions.json` :

```json
{
  "exceptions": [
    {
      "semaine": "2026-09-02",
      "type": "suspendue",
      "message": "Pas de fournée cette semaine — reprise le 9 septembre."
    }
  ]
}
```

La date `semaine` désigne le mercredi de la semaine concernée (format `YYYY-MM-DD`). Les types sont `suspendue` (pas de livraison) ou `deplacee` (horaires décalés). Voir `PROMPT-CODEX-TIMER-AUTO.md` pour le format complet. Sans ce fichier, le rythme standard s'applique.

## Mise en ligne

Un hébergement HTTPS est requis pour la géolocalisation. Netlify Drop ou Vercel conviennent. L'adresse reste toujours disponible : elle est un chemin de commande à part entière, pas un simple repli GPS.

## Décisions catalogue confirmées

Le Pastel Poisson Fumé est maintenu. Tous les pastels peuvent entrer dans les offres. L'offre 2 pastels est supprimée. Le supplément « Autre garniture — 600 F » est maintenu. Le Pastel Gourmand n'a pas de paliers à afficher : son total reste estimé et sera confirmé à la commande. Les box crêpes suivent aussi la livraison du jeudi.
