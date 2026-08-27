# Marque Made by Ischou — fichiers vectoriels

## 1. Les trois fichiers et leur usage

| Fichier | Usage | Seuil |
|---|---|---|
| `icon.svg` | Marque seule, base festonnée. Profil WhatsApp Business, avatar réseaux, tampon dans la page. | **≥ 40 px** |
| `favicon.svg` | Marque simplifiée, base droite, trait épais. Favicon, onglet, icône d'app. | **≤ 32 px** |
| `logo.svg` | Lockup complet : toque + « MADE BY » + « Ischou ». En-tête du site, pied de page, documents. | ≥ 120 px de large |

**Pourquoi deux coupes.** Le feston — le bord crénelé du pastel — est repris comme
motif graphique dans tout le site. Il est l'idée du logo : la toque du cuisinier
qui se termine par le bord d'un pastel. Mais il disparaît sous 40 px, où le tracé
fin se referme en bouillie. `favicon.svg` sacrifie le feston et épaissit le trait
de 4 à 6,5 pour rester lisible dans un onglet. C'est la même marque, taillée
différemment — pas deux logos.

## 2. Le lockup demande une étape de plus

`icon.svg` et `favicon.svg` sont **des tracés purs**. Utilisables partout, tout de
suite, sans condition.

`logo.svg` contient deux éléments `<text>`. Conséquence :

- **Inséré en ligne dans `index.html`** — fonctionne, les polices sont chargées.
- **Utilisé comme fichier `.svg` autonome** — le script « Ischou » sera remplacé
  par une police système. Inutilisable en l'état pour un favicon, un profil
  WhatsApp ou une impression.

Je n'ai pas pu vectoriser le script moi-même : cela demande le fichier de police
Yellowtail, que je n'ai pas pu récupérer. Conversion en une commande :

```bash
inkscape logo.svg --export-text-to-path --export-plain-svg -o logo-outlined.svg
```

Fais-la avant tout usage hors de la page. Une fois convertie, la version
`logo-outlined.svg` n'a plus aucune dépendance de police.

## 3. Couleur

Les trois fichiers utilisent `currentColor` — **aucune couleur codée en dur**. Le
logo hérite de la couleur du contexte : framboise sur crème, crème sur framboise,
crème sur chocolat quand la page passe en phase fermée. Un seul fichier couvre
tous les fonds.

Pour un usage hors du web, remplacer `currentColor` par la valeur voulue :

```bash
sed 's/currentColor/#BC1B57/g' icon.svg > icon-framboise.svg
sed 's/currentColor/#FBF3E9/g' icon.svg > icon-creme.svg
```

## 4. Interdits

- Ne pas ajouter d'ombre, de contour, de dégradé, de cœur décoratif.
- Ne pas déformer les proportions — l'échelle est uniforme ou rien.
- Ne pas recolorer le feston séparément de la toque.
- Ne pas poser `icon.svg` sous 40 px : utiliser `favicon.svg`.
- Ne pas régénérer la marque par un modèle d'image. Les modèles écrivent mal et
  le résultat ne serait ni redimensionnable ni fidèle.

## 5. Liste des assets — CORRIGÉE

`assets/hero.jpg` est **supprimé de la liste**. La direction en vigueur pose le
timer comme héros de la page, sans photographie (exigences B9 et F1). C'était un
résidu de la version 1 du site.

Assets à produire :

```
assets/logo.svg                     ✅ livré
assets/icon.svg                     ✅ livré
assets/favicon.svg                  ✅ livré
assets/pastel-classique.jpg         ⏳ à générer
assets/pastel-gourmand.jpg          ⏳ à générer
assets/pastel-poisson-fume.jpg      ⏳ à générer   (sous réserve — voir Partie 4 §1 du catalogue)
assets/crepe-chocolat.jpg           ⏳ à générer
assets/crepe-vanille.jpg            ⏳ à générer
assets/exceptions.json              ⏳ optionnel — voir PROMPT-CODEX-TIMER-AUTO.md
```

Six photos, pas sept. Les prompts correspondants sont dans `PROMPT-ASSETS.md`
§4 et §5 — **ignorer le §3, qui concerne le héros supprimé**.
