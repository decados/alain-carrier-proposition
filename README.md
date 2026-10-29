# Proposition Alain Carrier

Site statique autonome en français québécois. Les fichiers à publier, après validation seulement, sont dans `site/`. Ouvrir `site/index.html` directement ou servir `site/` avec `python3 -m http.server 8000 --directory site`. Les chemins sont relatifs et compatibles avec un hébergement statique.

## Hébergement de la proposition

- URL : https://alain-carrier-proposition.pages.dev/
- Cloudflare Pages, projet `alain-carrier-proposition`, relié au dépôt GitHub `decados/alain-carrier-proposition`.
- Branche de production : `main`; aucune commande de build; répertoire publié : `site`.
- Cloudflare déploie automatiquement les changements de `main`. GitHub Actions exécute uniquement les validations, sans publication GitHub Pages.
- La prévisualisation reste publique et non indexable par sa balise `noindex,nofollow`; il ne s'agit pas d'un accès privé ni du lancement officiel.

Le site ne possède aucun backend, formulaire, stockage local, traceur ou dépendance de compilation. Les choix de sujet restent dans la page et ne sont insérés dans un brouillon `mailto:` que lors du clic sur « Préparer mon courriel ». Aucun message n'est envoyé automatiquement. Un lien courriel direct demeure disponible sans JavaScript.

Contrôles : `python3 tests/test_site.py`; `node /home/hermes/.hermes/skills/creative/taste-skill/scripts/lint.mjs site`; `node /home/hermes/.hermes/skills/creative/taste-skill/scripts/inspect.mjs site/index.html`. Les captures de revue sont hors `site/`, dans `screenshots/` (non commises).

Avant publication : faire approuver la copie, les photographies et leurs droits, la portée géographique et l'adresse de contact; retirer la mention « Proposition de site — pour validation »; décider explicitement de la levée de `noindex,nofollow` et de `robots.txt` après approbation. Aucune disponibilité, aucun tarif, aucun délai n'est affirmé.
