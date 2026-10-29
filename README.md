# Proposition Alain Carrier

Site statique autonome en français québécois. La nouvelle proposition V2 est `site/index.html` à la racine; la première proposition V1 reste consultable dans `site/v1/index.html` (`/v1/` sur l'hébergement). Les fichiers à publier, après validation seulement, sont dans `site/`. Ouvrir `site/index.html` directement ou servir `site/` avec `python3 -m http.server 8000 --directory site`. Les chemins sont relatifs et compatibles avec un hébergement statique.

## Hébergement de la proposition

- URL : https://alain-carrier-proposition.pages.dev/
- Cloudflare Pages, projet `alain-carrier-proposition`, relié au dépôt GitHub `decados/alain-carrier-proposition`.
- Branche de production : `main`; aucune commande de build; répertoire publié : `site`.
- Les changements de `main` sont validés par GitHub Actions, puis un deploy hook limité à ce projet déclenche Cloudflare Pages. Cloudflare récupère les fichiers directement du dépôt GitHub. Aucune clé API Cloudflare générale n'est transmise à GitHub.
- GitHub Pages est désactivé; seul Cloudflare publie le site.
- La prévisualisation reste publique et non indexable par sa balise `noindex,nofollow`; il ne s'agit pas d'un accès privé ni du lancement officiel.

Les deux versions ne possèdent aucun backend, formulaire, stockage local, traceur ou dépendance de compilation. En V2, le choix de sujet met à jour localement le lien `mailto:`; seul le clic explicite ouvre un brouillon modifiable. Aucun message n'est envoyé automatiquement. Un lien courriel direct et un lien mailto par défaut demeurent disponibles sans JavaScript.

Contrôles : `python3 -m unittest discover -s tests -v`; `node --check site/v2.js` et `site/v1/script.js`; `node /home/hermes/.hermes/skills/creative/taste-skill/scripts/lint.mjs site/index.html site/v2.css site/v2.js`; `TMPDIR=/home/hermes/alain-carrier-proposition node /home/hermes/.hermes/skills/creative/taste-skill/scripts/inspect.mjs site/index.html --out screenshots-v2`. Les captures de V2 sont hors `site/`, dans `screenshots-v2/` (non commises). `NOTES-V2.md`, `REFERENCE-REVIEW-V2.md`, `REVIEW-V2.md` et `SOURCES.md` documentent la direction et la provenance. Les notes et captures V1 historiques sont conservées.

Avant publication : faire approuver la copie, les photographies et leurs droits, la portée géographique et l'adresse de contact; retirer la mention « Proposition de site — pour validation »; décider explicitement de la levée de `noindex,nofollow` et de `robots.txt` après approbation. Aucune disponibilité, aucun tarif, aucun délai n'est affirmé.
