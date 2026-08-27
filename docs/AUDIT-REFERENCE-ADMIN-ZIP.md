# Audit de la référence admin fournie

## Ce que contient la référence

Le ZIP contient douze écrans HTML d’administration : un tableau de bord, des produits, commandes, clients, collections, navigation, pages, personnalisation, médias, réductions, réglages et utilisateurs. Son expérience principale repose sur une navigation latérale persistante, une barre supérieure sobre, des cartes d’indicateurs, des tableaux denses, des actions par ligne et des fiches d’édition.

> Le ZIP contient explicitement des chiffres et commandes de démonstration. Ils ne doivent pas être transférés vers Made by Ischou, ni être montrés comme réels.

## Transposition retenue pour Made by Ischou

| Référence du ZIP | Adaptation Made by Ischou | Décision |
| --- | --- | --- |
| Tableau de bord | Trafic, événements de panier, intentions WhatsApp, références actives, activité récente | À construire avec données réelles uniquement. |
| Produits | Prix, disponibilité, description et image des 17 références validées | À conserver ; aucune création de produit fictif. |
| Commandes / clients | Commandes uniquement après consentement explicite ; aucun import WhatsApp automatique | À préparer, non alimenté sans consentement. |
| Médias | Bibliothèque des visuels réellement utilisés par la boutique | À réserver à une phase avec stockage média sécurisé. |
| Réglages | Informations opérationnelles réellement confirmées | À conserver progressivement. |
| Collections, menus, pages, réductions, utilisateurs | CMS, promotions ou gestion d’utilisateurs non nécessaires à la landing actuelle | À ne pas afficher pour le moment. |

## Principes de refonte

La Preview gardera les contrôles Firebase et les routes Vercel existants. L’interface remplacera les onglets actuels par une navigation latérale inspirée de la référence, avec une version mobile repliable. Le tableau de bord distinguera clairement les données réellement mesurées des zones encore non collectées ; aucun chiffre d’affaires, client, stock, avis ou commande ne sera simulé.
