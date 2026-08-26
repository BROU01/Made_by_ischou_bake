# PROMPT CODEX — Refonte « Made by Ischou »

> Généré via `prompt-optimizer` (EARS). À coller tel quel dans Codex.
> Projet : site de commande WhatsApp, fichier HTML unique, sans assets photo.

---

## Exigence initiale

> « Refaire le site Made by Ischou avec un design plus pro, moins cliché,
> améliorer le héros, et corriger la barre panier flottante qu'on ne peut pas
> annuler. »

**Faiblesses identifiées :**

| # | Faiblesse | Nature |
|---|---|---|
| 1 | « plus pro », « moins cliché », « sort de l'ordinaire » | Non mesurable — aucun critère de rejet objectif |
| 2 | Aucune thèse visuelle imposée | L'agent retombera sur le gabarit food par défaut |
| 3 | Le bug panier est décrit, pas spécifié | Ni comportement cible, ni états d'annulation |
| 4 | « améliorer le héros » | Pas de contenu de substitution alors que les photos manquent |
| 5 | Contrainte assets absente | L'agent va générer des `<img>` vers des fichiers inexistants |
| 6 | Aucun budget de complexité | Risque de refonte qui casse le flux WhatsApp validé |

---

## Transformation EARS

### A. Direction artistique (imposée, non négociable)

**A1.** Le système **doit** utiliser le framboise `#BC1B57` comme **champ dominant**
(fond des zones principales) et la crème `#FBF3E9` comme encre, inversant la
convention fond-clair/accent-coloré.

**A2.** Le système **doit** limiter l'ambre `#C2963B` aux chiffres du compte à
rebours et aux montants, et à rien d'autre.

**A3.** Le système **doit** utiliser exactement trois familles typographiques :
`Bricolage Grotesque` (display, 700–800), `Inter Tight` (corps et interface),
`Martian Mono` (chiffres, prix, libellés temporels, en tabulaire).

**A4.** Le système **doit** réserver `Yellowtail` au seul wordmark de marque, à une
occurrence maximum par page.

**A5.** Le système **doit** dessiner les séparateurs de section comme un **feston**
SVG répété — le bord crénelé du pastel — et **ne doit pas** utiliser de filet
droit, de dégradé ni de forme organique flottante comme séparateur.

**A6.** Le système **ne doit pas** produire : émoji utilisé comme icône, dégradé
décoratif, blob, particule, ombre colorée, glassmorphisme, `backdrop-filter`
ornemental, image générée, texte de remplissage.

**A7.** Si une couleur n'appartient pas au jeton défini en §Formats, alors le
système **doit** s'abstenir de l'introduire.

---

### B. Héros — machine à états hebdomadaire

Le héros est le compte à rebours vers la prochaine fournée. **Aucune photographie.**

**B1.** Le système **doit** afficher, comme élément principal du héros, le temps
restant avant le prochain jeudi, en jours / heures / minutes, en `Martian Mono`,
à une taille d'au moins `clamp(3.5rem, 12vw, 8rem)`.

**B2.** Le système **doit** recalculer ce compte à rebours toutes les 60 secondes
sans rechargement de page.

**B3.** **Tant que** le jour courant est lundi, mardi ou mercredi, le système
**doit** afficher l'état `COMMANDES OUVERTES`, activer tous les contrôles d'ajout
au panier, et libeller le compte à rebours « Fermeture des commandes dans ».

**B4.** **Tant que** le jour courant est jeudi, le système **doit** afficher l'état
`FOURNÉE DU JOUR`, et libeller le compte à rebours « Livraisons en cours ».

**B5.** **Tant que** le jour courant est vendredi, samedi ou dimanche, le système
**doit** afficher l'état `COMMANDES FERMÉES`, conserver les contrôles d'ajout
actifs, et libeller le compte à rebours « Prochaine fournée dans ».

**B6.** **Si** l'utilisateur ajoute un article alors que l'état est
`COMMANDES FERMÉES`, alors le système **doit** afficher, dans le carnet de
commande, la mention « Cette commande partira sur la fournée de jeudi » et
**ne doit pas** bloquer l'ajout.

**B7.** Le système **doit** afficher sous le compte à rebours une **frise de
semaine** de sept marqueurs `LUN MAR MER JEU VEN SAM DIM`, où le jour courant est
marqué, `MER` porte le libellé « clôture » et `JEU` le libellé « livraison ».

**B8.** Le système **doit** dériver les sept marqueurs de la frise de la logique de
date réelle et **ne doit pas** les coder en dur comme décoration.

**B9.** Le système **ne doit pas** placer dans le héros : image de fond, badge
« 100 % fait maison », note étoilée, compteur de clients, ni aucun élément de
preuve sociale non vérifiable.

---

### C. Panier — correction du défaut signalé

**C1.** Le système **ne doit pas** afficher de barre flottante fixe en bas de
l'écran. Ce composant est supprimé.

**C2.** Le système **doit** placer l'indicateur de panier dans l'en-tête collant,
sous forme d'un unique bouton affichant le nombre d'articles et le total.

**C3.** **Tant que** le panier est vide, le système **doit** afficher ce bouton en
état désactivé visuellement distinct, sans le retirer du flux, afin que la position
de l'en-tête ne se décale jamais.

**C4.** Le système **ne doit jamais** recouvrir le contenu de la page par un
élément non fermable.

**C5.** **Quand** l'utilisateur ouvre le carnet de commande, le système **doit**
offrir trois sorties : bouton de fermeture explicite, touche `Échap`, et clic sur
le voile.

**C6.** Le système **doit** fournir une action « Vider le panier » assortie d'une
confirmation en une étape, réversible tant que la confirmation n'est pas validée.

**C7.** Le système **doit** permettre de retirer une ligne entière du carnet,
distinctement de la décrémentation de quantité.

**C8.** **Quand** une ligne est retirée, le système **doit** afficher pendant
5 secondes une action « Annuler » qui restaure la ligne à sa quantité antérieure.

**C9.** **Si** le panier passe de non-vide à vide, alors le système **doit** fermer
la confirmation de vidage et afficher l'état vide du carnet, sans fermer le carnet.

---

### D. Carnet de commande

**D1.** Le système **doit** présenter le tiroir de commande comme un **carnet de
commande manuscrit** : perforation, lignes en tirets, numérotation de ticket.

**D2.** **Tant que** la largeur de viewport est inférieure à 640 px, le système
**doit** afficher le carnet en plein écran plutôt qu'en tiroir latéral.

**D3.** Le système **doit** piéger le focus clavier dans le carnet tant qu'il est
ouvert, et le restituer au bouton déclencheur à la fermeture.

**D4.** Le système **doit** conserver le format de message WhatsApp existant à
l'identique — ordre des blocs, libellés, unité `F`. Ce format est validé côté
commerçante.

---

### E. Livraison et géolocalisation

**E1.** **Quand** l'utilisateur sélectionne « Oui » à la livraison, le système
**doit** révéler le bloc destination sans déplacer le bouton d'envoi hors de vue.

**E2.** **Quand** l'utilisateur demande le partage de position, le système **doit**
appeler `navigator.geolocation.getCurrentPosition` avec `timeout: 10000` et
joindre au message un lien `https://maps.google.com/?q={lat},{lng}` à six décimales.

**E3.** **Si** la permission est refusée (`err.code === 1`), alors le système
**doit** énoncer le motif et orienter vers la saisie d'adresse, sans s'excuser ni
rester vague.

**E4.** **Si** `navigator.geolocation` est absent, alors le système **doit**
masquer le bouton GPS et conserver le champ adresse.

**E5.** Le système **doit** traiter le champ adresse comme un chemin de premier
rang et non comme un repli dégradé : la géolocalisation exige HTTPS et sera
refusée par une part significative des utilisateurs.

---

### F. Absence d'assets

**F1.** Le système **doit** produire une page **complète et livrable sans aucun
fichier image**. Aucune photographie n'est disponible à ce jour.

**F2.** Le système **ne doit pas** référencer de fichier image inexistant sans
mécanisme de repli.

**F3.** Le système **doit** représenter chaque produit par un **bloc typographique
composé** : nom en display, composition en corps, prix en mono, sur aplat de
couleur — et non par un cadre gris, un pictogramme générique ou une icône d'image.

**F4.** Le système **doit** prévoir pour chaque produit un point d'insertion photo
`assets/{id}.jpg` qui, une fois le fichier présent, remplace l'aplat sans
modification de mise en page ni de hauteur de carte.

---

### G. Plancher qualité

**G1.** Le système **doit** rester utilisable de 360 px à 1920 px de large.

**G2.** Le système **doit** rendre visible le focus clavier sur tout élément
interactif, avec un contour d'au moins 3 px.

**G3.** Le système **doit** respecter `prefers-reduced-motion: reduce` en
supprimant transitions et animations, compte à rebours inclus.

**G4.** Le système **doit** maintenir un contraste texte ≥ 4.5:1 — vérifier
particulièrement crème sur framboise et ambre sur framboise.

**G5.** Le système **doit** répondre à toute interaction en moins de 400 ms
(seuil de Doherty), le panier étant en mémoire.

**G6.** Le système **doit** rester un fichier unique, sans dépendance JS, sans
build, sans `localStorage`, sans backend.

**G7.** Le système **doit** se charger sans aucune erreur console.

---

## Domaine et théories mobilisées

**Domaine principal :** commerce alimentaire artisanal à disponibilité périodique,
canal de conversion hors-site (messagerie).

| Théorie | Application |
|---|---|
| **Repères temporels** (Dai, Milkman & Riis) | Le jeudi est un repère hebdomadaire. Le compte à rebours l'exploite comme structure de page, non comme gadget marketing. |
| **Effet Von Restorff** (isolation) | Un seul élément isolé — le compte à rebours. Tout le reste est délibérément calme, ce qui rend cet élément mémorable. |
| **Loi de Jakob** | Conformité totale sur les mécaniques d'interaction (stepper, tiroir, `Échap`), déviation totale sur l'esthétique. La singularité se paie sur le registre visuel, jamais sur l'apprentissage. |
| **Loi de Fitts** | Sur mobile, les cibles panier et envoi ≥ 48 px et positionnées en zone du pouce, sans recouvrir le contenu. |
| **Loi de Hick** | Menu volontairement court (6 produits, 3 offres, 3 extras). Ne pas ajouter de filtres, tri ou catégories : le coût de décision augmenterait sans bénéfice. |
| **Gestalt — région commune** | Le carnet de commande regroupe articles, extras, note et livraison dans une région fermée unique, matérialisant « une commande ». |
| **Seuil de Doherty** | Retour visuel sous 400 ms sur chaque ajout, retrait et bascule. |

**Théorie écartée sciemment :** rareté persuasive / urgence artificielle. Le
compte à rebours reflète une contrainte de production **réelle**. Il ne doit
jamais être accéléré, coloré en rouge d'alerte, ni assorti d'un compteur de stock
fictif. Une urgence fabriquée dans un commerce de quartier détruit la confiance
qui est l'actif principal de la marque.

---

## PROMPT À COLLER DANS CODEX

```
# Rôle

Tu es directeur artistique et développeur front-end senior dans un studio réputé
pour donner à chaque client une identité visuelle qu'on ne peut confondre avec
aucune autre. Ce client a déjà rejeté une première proposition jugée « banale et
clichée ». Il travaille lui-même dans le design web : il reconnaîtra
immédiatement un gabarit générique. Tu es payé pour un point de vue, pas pour une
exécution neutre.

# Contexte projet

Made by Ischou — pastels et crêpes faits maison, Agidogomé (Ave Maria, Rue
Mélonku), Lomé, Togo. Commandes le mercredi, livraison le jeudi uniquement.
Cible : particuliers à Lomé, mobile Android majoritaire, réseau lent.
Langue de l'interface : français. Orthographe de marque : « Ischou ».

Le site ne traite aucun paiement. Il compose une commande et l'envoie sur
WhatsApp via un lien profond wa.me pré-rempli.

# Skills à charger AVANT toute écriture de code

Liste le dossier de skills du projet et lis intégralement le SKILL.md de chaque
skill dont la description recoupe cette tâche. Plusieurs s'appliquent
simultanément — lis-les tous, ne devine aucun contenu depuis son nom.
Pertinents ici : ui-ux-pro-max, ui-ux-design-pro, taste, impeccable,
color-expert, nothing-design, claude-design-skill, claudedesignskills,
pencilplaybook, huashu-design, Front-End-Checklist, frontend-dev-bookmarks,
superpowers.
Lis également CLAUDE.md et AGENTS.md à la racine.
En cas de conflit, l'ordre de préséance est : ce prompt > CLAUDE.md > skills.

# Thèse imposée

Le fait le plus intéressant de ce commerce n'est pas le produit, c'est le rythme.
Rien ne se passe six jours sur sept, puis il y a une fournée. Ce n'est pas un
restaurant, c'est un rendez-vous hebdomadaire.

Le héros de cette page est donc LE TEMPS, pas le menu.

Un site de restaurant met une photo de plat et une accroche. Tu ne feras pas ça.
Tu construiras une page qui change de personnalité selon le jour de la semaine,
articulée autour d'un compte à rebours vers la prochaine fournée.

# Compétences attendues

- Direction artistique fondée sur la matière du sujet, pas sur des tendances
- Typographie : échelle, graisses, chasses, interlettrage délibérés
- Machines à états en JavaScript vanilla, sans framework
- Accessibilité clavier et lecteur d'écran de niveau production
- CSS moderne maîtrisé : container queries, clamp(), color-mix(), :has()
- Discipline de spécificité CSS (éviter l'annulation mutuelle des marges)
- Rédaction d'interface : verbes actifs, phrase courte, zéro remplissage
- Autocritique : retirer un élément avant de livrer

# Contraintes techniques absolues

1. Livrable unique : index.html. HTML + CSS + JS inline.
2. Zéro dépendance JS. Pas de React, Vue, Tailwind, Bootstrap, jQuery, Alpine.
   Seule ressource externe autorisée : Google Fonts.
3. Zéro backend, zéro build, zéro variable d'environnement.
4. Pas de localStorage ni sessionStorage. Le panier vit en mémoire.
5. Pas de WhatsApp Cloud API. Canal = lien profond wa.me?text= encodé via
   encodeURIComponent.
6. AUCUN FICHIER IMAGE N'EXISTE. La page doit être complète et belle sans une
   seule photo.
7. N'invente aucun prix, produit, horaire ni numéro de téléphone.

Si une consigne entre en conflit avec ces sept points, arrête-toi et signale le
conflit au lieu de contourner.

# Jetons de design imposés

Couleurs — n'introduis AUCUNE valeur hors de cette liste :
  --framboise:       #BC1B57   CHAMP DOMINANT (fond des zones principales)
  --framboise-fonce: #9A1447   états pressés
  --bordeaux:        #7A1230   profondeurs, ombrages d'aplat
  --chocolat:        #2A1810   texte sur crème, zones sombres
  --creme:           #FBF3E9   ENCRE sur framboise / fond des zones claires
  --creme-fonce:     #F3E6D5   aplats secondaires
  --or:              #C2963B   UNIQUEMENT chiffres du compte à rebours et montants
  --vert:            #3E7B3A   état « commandes ouvertes »

Inversion imposée : le framboise est le SOL, la crème est l'ENCRE. Ne produis pas
un fond clair avec un accent coloré — c'est exactement la convention rejetée.

Typographie — trois rôles, pas un de plus :
  Bricolage Grotesque  700–800   display, titres, états
  Inter Tight          400–600   corps, interface, libellés
  Martian Mono         500–700   chiffres, prix, temps — TOUJOURS tabulaire
  Yellowtail                     wordmark UNIQUEMENT, une occurrence max

Séparateur de section : feston SVG répété (le bord crénelé du pastel). Jamais de
filet droit, jamais de dégradé, jamais de forme organique flottante.

# Interdits — rejet automatique du livrable

- Émoji employé comme icône. Toute icône est un SVG inline, stroke 2–2.4,
  stroke="currentColor". Les cœurs ♥ de la charte imprimée sont autorisés :
  ce sont des glyphes de marque, pas des émojis.
- Dégradé décoratif, blob, particule, forme flottante, glassmorphisme,
  backdrop-filter ornemental, ombre colorée.
- Placeholder gris, icône « image manquante », cadre vide.
- Preuve sociale non vérifiable : note étoilée, compteur de clients, témoignage
  inventé, badge « n°1 ».
- Urgence fabriquée : stock fictif, minuteur accéléré, rouge d'alerte sur le
  compte à rebours. La contrainte du jeudi est réelle — elle se suffit.
- Texte de remplissage, superlatif creux, « Bienvenue sur notre site ».
- Libellé système : on écrit « Commander », pas « Soumettre ». Le nom d'une
  action reste identique du bouton jusqu'à la confirmation.
- Les trois défauts IA courants : crème + serif contrastée + terracotta #D97757 ;
  noir profond + accent vert acide ; layout broadsheet à filets fins.

# Workflow

## Phase 1 — Trois directions avant tout code

Produis TROIS variations de la direction artistique imposée. La thèse (le temps
comme héros) et les jetons de couleur sont fixes ; tu fais varier composition,
échelle typographique et traitement du compte à rebours.

Pour chacune : un nom, trois lignes de rationnel, un wireframe ASCII du héros,
et l'élément signature. N'écris pas une ligne de code avant que l'humain ait
choisi.

Autocritique obligatoire avant de présenter : pour chaque direction, demande-toi
si tu produirais la même chose pour une pâtisserie de Lyon ou un food truck de
Berlin. Si oui, la direction n'est pas ancrée dans ce sujet — remplace-la.

## Phase 2 — Construction, par lots

Lot 1  Structure, jetons, machine à états hebdomadaire, héros
Lot 2  Catalogue typographique des produits, feston, offres, extras
Lot 3  Panier en en-tête, carnet de commande, annulation, vidage
Lot 4  Livraison, géolocalisation, composition et envoi du message WhatsApp
Lot 5  Accessibilité, responsive 360px, reduced-motion, passe de contraste

Livre un lot à la fois. Attends validation avant le suivant.

## Phase 3 — Passe de retrait

Avant de rendre : relis la page et retire UN élément. Le plus décoratif.
Documente lequel et pourquoi.

# Exigences EARS

[Reporte ici les sections A à G du document — elles sont normatives.]

# Exemples concrets

Compte à rebours, mardi 26 août 2026 à 14h30 :
  état    : COMMANDES OUVERTES
  libellé : « Fermeture des commandes dans »
  valeur  : 0 J · 33 H · 30 MIN     (jusqu'au mercredi 23h59)
  frise   : LUN [MAR] MER·clôture JEU·livraison VEN SAM DIM

Compte à rebours, samedi 29 août 2026 à 09h00 :
  état    : COMMANDES FERMÉES
  libellé : « Prochaine fournée dans »
  valeur  : 4 J · 15 H · 00 MIN
  carnet  : « Cette commande partira sur la fournée de jeudi »

Bloc produit sans photo :
  PASTEL POISSON FUMÉ                            250 F
  Poisson fumé, œuf, légumes croquants,          pièce
  herbes et épices.
  [−] 3 [+]

Message WhatsApp généré — format à conserver À L'IDENTIQUE :
  Bonjour Made by Ischou !
  Je souhaite passer commande :

  • 4 × Pastel Classique — 1000F
  • 2 × Crêpe Chocolat — 1000F

  Total produits : 2000F

  Extras : Noix de coco râpée

  Note : bien épicé

  Livraison : Oui
  Nom : Kodjo
  Position GPS : https://maps.google.com/?q=6.172500,1.231400
  Adresse : Agidogomé, à côté de la pharmacie Ave Maria
  (Livraison partout à Lomé à partir de 1000F)

  Pour une livraison le jeudi. Merci !

Erreur de géolocalisation refusée (err.code === 1) :
  « Vous avez refusé le partage de position. Indiquez votre adresse ci-dessous,
    c'est parfait aussi. »
  → ni excuse, ni formulation vague, ni terme technique.

# Données produits — source de vérité

PASTELS — 250 F la pièce
  pastel-classique      Pastel Classique
                        Sardine, œuf, carotte, oignon, poivron, persil, épices.
  pastel-gourmand       Pastel Gourmand
                        Sardine, saucisse, œuf, légumes frais et épices.
  pastel-poisson-fume   Pastel Poisson Fumé
                        Poisson fumé, œuf, légumes croquants, herbes, épices.

CRÊPES — 500 F la pièce
  crepe-chocolat            Crêpe Chocolat — chocolat fondant (Nutella).
  crepe-vanille             Crêpe Vanille [NOUVEAU] — crème vanillée maison.
  crepe-banane-chocolat     Crêpe Banane Chocolat — banane fraîche, chocolat.

OFFRES PASTELS
  offre-2    2 pastels    500 F
  offre-4    4 pastels   1000 F
  offre-10  10 pastels   2200 F

EXTRAS (offerts, multi-sélection)
  Éclats de biscuits · Noix de coco râpée · Amandes effilées

CONFIG
  whatsapp     : "22871303911"   (international, sans + ni espaces)
  devise       : "F"
  livraisonMin : 1000

Adresse : Agidogomé, Ave Maria, Rue Mélonku, Lomé
Téléphones : 71 30 39 11 · 97 11 56 38

# Zones grises — NE TRANCHE PAS SEUL

Les flyers imprimés se contredisent. Le tableau ci-dessus suit les flyers 1/3/4.
Ne « corrige » pas ces valeurs :
  offre moyenne   : 4 pastels 1000F (retenu)  vs  5 pastels 1000F
  grande offre    : 10 pastels 2200F (retenu) vs  10 pastels 2000F
  vente à l'unité : 250F/pièce (retenu)       vs  lots uniquement
Un seul des deux numéros reçoit WhatsApp — lequel reste à confirmer.
Face à une ambiguïté de cet ordre : pose la question, ne comble pas le vide.

# Format de livraison

Fichier : index.html, autonome, encodage UTF-8, lang="fr".
Ordre interne : jetons :root → composants → machine à états → panier → carnet →
WhatsApp → init.

Pour chaque lot, rends compte ainsi :
  - ce qui a changé, où (nom de section ou de fonction), et pourquoi
  - les décisions de design prises et leur justification tirée du sujet
  - ce que tu as retiré
  - les questions ouvertes
Pas de récit de ton propre processus. Pas de liste de fichiers touchés
quand il n'y en a qu'un.

# Critères de réception

[ ] La page est complète et convaincante sans aucun fichier image
[ ] Le héros ne contient ni photo, ni accroche générique, ni preuve sociale
[ ] Le compte à rebours change réellement d'état selon le jour
[ ] La frise de semaine est dérivée de la date, non codée en dur
[ ] Aucune barre flottante ne recouvre le contenu
[ ] Le panier vit dans l'en-tête et n'y décale jamais la mise en page
[ ] Vider le panier est confirmable et réversible
[ ] Retirer une ligne offre une annulation pendant 5 secondes
[ ] Le carnet se ferme par bouton, par Échap et par le voile
[ ] Le focus est piégé dans le carnet puis restitué au déclencheur
[ ] Le message WhatsApp est identique au format de référence
[ ] Le champ adresse fonctionne sans géolocalisation
[ ] Aucune couleur hors jetons
[ ] Trois familles typographiques, pas une de plus
[ ] Zéro émoji-icône, zéro dégradé décoratif, zéro blob
[ ] Contraste ≥ 4.5:1, crème sur framboise et ambre sur framboise vérifiés
[ ] Utilisable de 360px à 1920px
[ ] prefers-reduced-motion respecté, compte à rebours inclus
[ ] Zéro erreur console
[ ] Un élément a été retiré à la passe finale, et documenté
```

---

## Mode d'emploi

**Plan gratuit Codex** — la fenêtre est limitée, donc :

1. Colle le prompt **entier** au premier message, avec l'`index.html` actuel en
   pièce jointe ou en contexte.
2. Exige la **Phase 1 seule** d'abord — trois directions, aucun code. C'est peu
   coûteux en tokens et c'est là que se joue la qualité.
3. Choisis une direction, puis demande **un lot à la fois** (§Workflow Phase 2).
   Un lot par conversation si la fenêtre sature ; recolle alors les sections
   `Contraintes`, `Jetons`, `Interdits` en tête — ce sont les trois blocs qui
   empêchent la dérive.
4. Reporte les exigences EARS §A–G dans le prompt à l'endroit indiqué, ou
   attache ce fichier au projet.

**Le passage qui fait le plus de travail** est le bloc `Interdits`. Un agent de
code laissé libre sur un sujet food converge vers le même gabarit ; la liste de
rejet automatique est ce qui casse cette convergence.

**La Phase 3** — retirer un élément avant de livrer — n'est pas une coquetterie.
C'est le seul garde-fou contre l'accumulation d'effets qui fait qu'une maquette
« sent » la génération automatique.
