# Références SEO et mesure d’audience

## Google Analytics

Google Analytics nécessite un compte, une propriété et un flux de données Web ; la collecte commence une fois la balise du site installée. L’identifiant de mesure du flux Web suit le format `G-…` et relie la landing à la propriété analytique. [1][2]

## Google Search Console et sitemap

La propriété Search Console doit être validée afin de protéger l’accès aux données de recherche. Pour une landing Vercel, une propriété de préfixe d’URL peut être validée par balise HTML ; une validation par DNS reste nécessaire pour une propriété de domaine complète. [3]

Un sitemap placé à la racine doit contenir des URL absolues canoniques. Il peut être référencé dans `robots.txt` et soumis dans le rapport Sitemaps. Sa soumission aide Google à découvrir les pages mais ne garantit pas leur exploration ou leur indexation. [4][5]

## Références

[1]: https://support.google.com/analytics/answer/9304153?hl=fr "Configurer Analytics pour un site Web et/ou une application — Google"
[2]: https://support.google.com/analytics/answer/12270356?hl=fr "ID de mesure GA4 — Google"
[3]: https://support.google.com/webmasters/answer/9008080?hl=fr "Valider la propriété de votre site — Google Search Console"
[4]: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap "Build and submit a sitemap — Google Search Central"
[5]: https://support.google.com/webmasters/answer/7451001?hl=fr "Gérer vos sitemaps à l’aide du rapport sur les sitemaps — Google"
