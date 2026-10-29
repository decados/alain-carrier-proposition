# Alain Carrier Rituel — site statique

Trois versions autonomes, sous `site/` :

- V3 actuelle : `site/index.html`, racine `/` sur https://alain-carrier-proposition.pages.dev/
- V2 archivée sans bandeau : `site/v2/index.html`, chemin `/v2/`
- V1 historique inchangée : `site/v1/index.html`, chemin `/v1/`

Ces URL publiques ne seront mises à jour qu'après revue, commit poussé et déploiement par la personne responsable. Le présent travail local ne pousse ni ne déploie. Chaque version garde ses propres CSS/JS et assets relatifs; V3 utilise `site/styles.css`, `site/script.js` et ses polices locales. Ouvrir directement les fichiers ou servir `site/` avec `python3 -m http.server 8000 --directory site`.

Aucun backend, formulaire transmis, cookie applicatif, analytique ni stockage. En V3, les radios changent uniquement le lien `mailto:`; sans JS, les liens ouvrent toujours le client de courriel. L'envoi reste une action du visiteur dans son logiciel. La prévisualisation publique reste `noindex,nofollow` avec `robots.txt` dans les trois répertoires; ce n'est pas une protection d'accès.

Vérification : `python3 -m unittest discover -s tests -v`, `node --check site/script.js`, `node --check site/v2/v2.js`, `node --check site/v1/script.js`, puis Taste lint/inspect détaillés dans `REVIEW-V3.md`. `RESEARCH-V3.md`, `NOTES-V3.md` et `SOURCES.md` donnent le raisonnement et la provenance. Captures non publiées dans `screenshots-v3/` (ignorées par Git).

Le workflow `.github/workflows/validate.yml` valide ces tests avant le deploy hook Cloudflare sur un push à `main`. Ne pas lever `noindex` ni décider du référencement sans approbation. Les textes proposés, les droits des portraits et du logo, l'adresse de contact, le périmètre géographique et le statut actuel des affiliations restent à confirmer avec Alain.
