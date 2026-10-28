# Revue visuelle et vérification de la proposition

ROUND 2 — captures finales inspectées aux largeurs 1440, 768 et 390 px.
Seen in one second: une feuille claire sur un fond bleu profond.
Idea: la parole personnelle d'Alain devient une lettre, prolongée par des feuillets de préparation.
Live thing: cocher souvenirs, valeurs et musique avant d'ouvrir explicitement un brouillon de courriel.
Layout words by section: hero=feuille/photo / approche=split / lettre=page / préparation=feuillet / FAQ=index / contact=champ partagé / pied=signature.
Scores subjectifs: design 7 · utilisabilité 8 · créativité 7 · contenu 7 → ensemble 7,3/10. Aucun plafond bloquant du rubric. Photographies de nature génériques, notamment voiliers et mer, et typographie de repli sont les principales limites esthétiques.
Top three points restants :
1. `desktop-page-01.jpg` : le passage entre l'approche et la lettre conserve un grand repos visuel; acceptable comme respiration, mais pourrait être resserré.
2. `tablet-page-01.jpg` : les images de mer ne documentent pas le Grand-Montréal; remplacer par photographies locales autorisées si possible.
3. `mobile-fold.jpg` : titre à deux lignes lisible mais relativement petit face au grand feuillet; compromis pour conserver la formule entière.

Vérifications réelles :
- `python3 -m unittest discover -s tests -v` : 4 tests réussis (ancres, chemins/images, noindex/robots, contact, structure clavier/mobile, absence de stockage et d'envoi applicatif).
- `node …/taste-skill/scripts/lint.mjs site` : 0 FAIL, 0 WARN.
- `TMPDIR=/home/hermes/alain-carrier-proposition node …/taste-skill/scripts/inspect.mjs site/index.html` : 0 FAIL à 1440, 768, 390; 4 WARN (nombre de tailles typographiques, pas de vidéo, polices système plutôt que polices tirées, respiration de 420 px). Aucune vidéo identifiée qui représenterait honnêtement Alain; choix de ne pas utiliser une vidéo décorative. Polices système pour une page autonome sans requête externe. Les variantes de tailles proviennent surtout des échelles responsive et des notes.
- Navigateur réel sur `file://` : aucun débordement horizontal (`scrollWidth == clientWidth` aux trois largeurs); `mailto:` initial et après sélection des trois sujets vérifiés sans ouvrir de client mail; une case s'active à la barre d'espace; la FAQ native s'ouvre à la barre d'espace et se referme avec Entrée en focus clavier (événements CDP keyDown/char/keyUp); `window.onerror`/rejets non gérés : aucun événement dans le parcours testé; mode reduced-motion : animation de la photo d'ambiance absente et défilement auto. Les liens d'ancres et images locales ont aussi été contrôlés par tests statiques.

Captures locales non destinées au déploiement : `screenshots/desktop-fold.jpg`, `desktop-page-01.jpg`, `desktop-page-02.jpg`, `tablet-fold.jpg`, `tablet-page-01.jpg`, `mobile-fold.jpg`, `mobile-page-01.jpg`.

La publication reste bloquée jusqu'à approbation des textes, de la portée et des images; le retrait du noindex et du bandeau est une décision de lancement, pas un automatisme.
