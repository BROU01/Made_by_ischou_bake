# PROMPT CODEX — Mise à jour catalogue & réponses aux questions ouvertes

> À envoyer à Codex **avant** de lancer le Lot 1.
> Remplace intégralement la section « Données produits » du brief initial.

---

## PARTIE 1 — Réponses à tes trois questions

### Q1 — Numéro WhatsApp

Confirmé : **`22871303911`** (71 30 39 11).

`CONFIG.whatsapp = "22871303911"`. Le second numéro (97 11 56 38) reste affiché
en pied de page comme contact téléphonique, mais ne reçoit pas les commandes du
site.

### Q2 — Sections EARS A à G

Elles existent. C'est un défaut de transmission de ma part : le brief que tu as
reçu contenait le marqueur `[Reporte ici les sections A à G]` sans le contenu.

Le fichier **`PROMPT-CODEX-REFONTE.md`** est joint au projet. Les sections A à G
s'y trouvent sous le titre « Transformation EARS » :

- **A** — Direction artistique imposée (7 exigences)
- **B** — Héros et machine à états hebdomadaire (9 exigences)
- **C** — Panier, correction du défaut de barre flottante (9 exigences)
- **D** — Carnet de commande (4 exigences)
- **E** — Livraison et géolocalisation (5 exigences)
- **F** — Absence d'assets (4 exigences)
- **G** — Plancher qualité (7 exigences)

Lis ce fichier intégralement. Ces 45 exigences sont normatives : elles priment
sur toute interprétation. La section **H** ci-dessous les complète.

### Q3 — Écarts entre flyers

Tranchés par la cliente. Les valeurs ci-dessous font foi et **remplacent** tout
ce qui figurait dans le brief initial. Les anciens flyers sont périmés.

---

## PARTIE 2 — Catalogue, source de vérité unique

### Pastels — vendus à l'unité

| id | nom | prix | composition |
|---|---|---|---|
| `pastel-poisson-fume` | Pastel Poisson Fumé | 250 F | Poisson fumé, légumes. |
| `pastel-classique` | Pastel Classique | 300 F | Sardines. |
| `pastel-gourmand` | Pastel Gourmand | **à partir de 350 F** | Sardine, saucisse ou œuf. |

Changements par rapport au brief initial :
- Les prix ont changé. Le tarif unique de 250 F n'existe plus.
- La mention « et épices » est **retirée de toutes** les compositions.
- Le Pastel Classique ne contient plus ni œuf, ni carotte, ni oignon, ni poivron,
  ni persil. Sa composition est désormais : **Sardines.** Un seul mot.
- Le Pastel Gourmand n'a plus de prix fixe.

### Offres pastels

| id | nom | prix |
|---|---|---|
| `offre-5` | 5 Pastels | 1 000 F |
| `offre-10` | 10 Pastels | 2 000 F |

L'offre « 4 pastels » et l'offre « 10 pastels à 2 200 F » sont **supprimées**.

### Crêpes

| id | nom | composition |
|---|---|---|
| `crepe-chocolat` | Crêpe Chocolat | Crêpe moelleuse garnie de chocolat fondant. |
| `crepe-vanille` | Crêpe Vanille `[NOUVEAU]` | Crêpe nappée d'une crème vanillée maison. |

### Box crêpes — NOUVEAU, absent du brief initial

| id | nom | prix | contenu |
|---|---|---|---|
| `box-petite` | Petite Box | 3 000 F | 5 à 6 crêpes roulées + chocolat |
| `box-classique` | Box Classique | 4 000 F | 8 à 10 crêpes roulées + chocolat |

### Supplément crêpe — payant

| id | nom | prix |
|---|---|---|
| `supp-banane` | Supplément Banane | +200 F |

Le supplément Fraise est **supprimé**. Ne le fais pas apparaître.

### Extras gourmandise — offerts, inchangés

Éclats de biscuits · Noix de coco râpée · Amandes effilées

**Ces trois extras sont gratuits.** Ils ne doivent jamais être confondus avec les
suppléments crêpes, qui sont payants.

### Configuration

```
whatsapp     : "22871303911"
devise       : "F"
livraisonMin : 1000
```

Adresse : Adidigomé, Ave Maria, Rue Mélonku, Lomé
Téléphones affichés : 71 30 39 11 · 97 11 56 38
Orthographe de marque : **Ischou** — jamais « Ishou », jamais « Made by by ».

---

## PARTIE 3 — Exigences EARS additionnelles (section H)

Ces exigences s'ajoutent aux sections A à G de `PROMPT-CODEX-REFONTE.md`.

### H — Catalogue, prix variables et suppléments

**H1.** Le système **doit** afficher le prix du Pastel Gourmand sous la forme
« À partir de 350 F » et **ne doit pas** l'afficher comme un prix ferme.

**H2.** **Tant que** le panier contient au moins un article à prix variable, le
système **doit** libeller le total « Total estimé » plutôt que « Total produits ».

**H3.** **Tant que** le panier contient au moins un article à prix variable, le
système **doit** insérer dans le message WhatsApp, sous le total, la ligne :
`(Total à confirmer — Pastel Gourmand facturé selon la garniture choisie)`.

**H4.** Le système **doit** présenter les extras gourmandise et les suppléments
crêpes dans **deux blocs visuellement distincts**, le premier portant la mention
« offert », le second affichant le prix de chaque ligne.

**H5.** Le système **doit** permettre de sélectionner un supplément crêpe avec une
quantité propre, et **doit** l'intégrer au total comme une ligne de commande à
part entière.

**H6.** **Si** le panier contient un supplément crêpe sans contenir aucune crêpe
ni aucune box, alors le système **doit** afficher dans le carnet la mention
« Un supplément s'ajoute à une crêpe — ajoutez d'abord une crêpe ou une box » et
**ne doit pas** bloquer l'envoi.

**H7.** Le système **doit** traiter les box crêpes comme des articles autonomes du
catalogue, avec leur propre bloc de section, distinct des crêpes à l'unité.

**H8.** Le système **ne doit pas** afficher de prix barré, de mention « au lieu
de », ni de pourcentage de réduction sur les offres pastels et les box.

**H9.** Le système **doit** dériver le prix affiché exclusivement du tableau de la
Partie 2 et **ne doit pas** recalculer, arrondir ni interpoler un prix unitaire à
partir d'une offre groupée.

**H10.** Le système **doit** afficher la composition du Pastel Classique
exactement telle qu'écrite — « Sardines. » — sans l'enrichir, sans lui ajouter de
légume, d'épice ou d'adjectif.

---

## PARTIE 4 — Six points NON tranchés : pose la question, ne décide pas

La cliente a répondu partiellement. Ces six points restent ouverts. **N'en
tranche aucun.** Si un lot en dépend, signale-le et attends.

**1 · Le Pastel Poisson Fumé survit-il à la règle ?**
La consigne est « retirer épices et poisson des garnitures de tous les pastels ».
Or ce produit est défini par le poisson fumé. Deux lectures : soit la règle ne
visait que la mention générique « poisson » dans les autres compositions, soit ce
produit est retiré du catalogue. Le tableau ci-dessus le conserve, **par défaut,
en attente**.

**2 · Quels pastels entrent dans les offres groupées ?**
5 pastels à 1 000 F revient à 200 F l'unité, alors que le tarif unitaire va de
250 à 350 F. Un lot composé uniquement de Pastels Gourmands vaudrait 1 750 F à
l'unité. Il manque la règle : les offres portent-elles sur un pastel de base
uniquement, ou sur n'importe quelle combinaison ?

**3 · L'offre « 2 pastels — 500 F » existe-t-elle encore ?**
Absente du nouveau flyer. Supprimée ou simplement non reprise ?

**4 · Le supplément « Autre garniture — 600 F » est-il maintenu ?**
Il figure sur le flyer crêpes. La cliente a corrigé Banane et Chocolat, supprimé
Fraise, et n'a rien dit de celui-ci.

**5 · Que recouvre « à partir de 350 F » pour le Pastel Gourmand ?**
Sardine, saucisse et œuf sont-ils trois variantes au même prix, ou trois paliers
tarifaires distincts ? Cela détermine si le site propose un choix de garniture au
moment de l'ajout au panier ou se contente de la mention d'estimation.

**6 · Les box crêpes suivent-elles le rythme mercredi → jeudi ?**
Rien ne l'indique sur le flyer. Si les box demandent un délai différent, la
machine à états hebdomadaire doit en tenir compte.

---

## PARTIE 5 — Ce que tu fais maintenant

1. Lis `PROMPT-CODEX-REFONTE.md` en entier, sections A à G incluses.
2. Charge les skills du projet selon le protocole du brief initial.
3. Remplace le catalogue par la Partie 2. Les anciennes données sont périmées.
4. Intègre la section H aux exigences normatives.
5. Reprends au **Lot 1** du workflow — la structure change, puisque deux familles
   de produits s'ajoutent (box, suppléments payants).
6. Si un lot bute sur l'un des six points de la Partie 4, dis-le et attends.

Rends compte en indiquant ce qui a changé, où, et pourquoi. Pas de récit de
processus.
