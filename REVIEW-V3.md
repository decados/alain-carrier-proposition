# Revue V3 — vérification locale, non déployée

## Avant / après réellement vus
Avant : `screenshots-v3/before/{desktop,tablet,mobile}-fold.jpg` et pages. V2 à 1440/768/390 : 0 FAIL, 3 WARN Taste, dont marges décalées et premier écran insuffisamment identifié sur deux formats selon l'inspecteur. Le premier écran montre un logo ACR de 64 × 48 px (51 × 40 px sur téléphone), un portrait sur près de la moitié de chaque écran desktop/tablette et une colonne de lecture étroite sombre. Le portrait demeure sticky sur tout le parcours et revient encore au pied. La critique visuelle est plus importante que ce compteur : la marque propre à Alain n'est presque pas lisible.

Après : `screenshots-v3/final-check/{desktop,tablet,mobile}-fold.jpg`, les feuilles `*-page-*.jpg` et `mobile-320-fold.png`. ACR est lisible à 236 × 177 px sur desktop, 185 × 138 px sur tablette et 166 × 124 px sur téléphone, sans crop du monogramme; il revient au pied. Photo réelle présente au premier écran, mais plus sticky ni répétée. La proposition funéraire, le métier, le territoire et l'action contact sont visibles sur téléphone. L'alternance de champs clair / vert ardoise / clair rend la progression moins monotone que V2. Le portrait reste une image ancienne prise devant un décor marin; ce n'est pas une photographie de cérémonie.

ROUND 1 — après première construction (`after-pass1`)
Seen in one second: ACR puis Alain et son portrait.
Idea (one sentence): l'authentique monogramme ACR, agrandi, introduit une parole personnelle plutôt qu'un catalogue funéraire.
Live thing: deux sujets de courriel modifient le mailto sans envoi.
Layout words by section: hero=présence / cérémonie=énoncé / approche=bande / parole=vis-à-vis / parcours=champ / contact=vis-à-vis / footer=marque.
Scores: design 6 · usability 7 · creativity 6.5 · content 7 → calcul brut 6.5, plafonné à 6.0 par les FAIL.
Caps applied: FAIL citations trop grandes et nombre de vraies images insuffisant.
Top three problems :
1. `after-pass1/desktop-fold.jpg` : portrait recadré au front et trop serré. Passer à la photo originale plus large avec tête et costume visibles.
2. `after-pass1/mobile-page-01.jpg` : citation sur plusieurs lignes, traitée comme un titre. Réduire sa taille sans couper le texte attribué.
3. `after-pass1/desktop-page-01.jpg` : ouverture de la section cérémonie trop verbale. Raccourcir la phrase dominante et conserver le détail dans la seconde colonne.

ROUND 2 — rendu final (`final-check`)
Seen in one second: ACR et Alain, avec sa photographie à droite sur grand écran et près du métier sur mobile.
Idea (one sentence): l'identité ACR réelle sert de signature aux étapes de la page, plutôt qu'une métaphore de deuil.
Live thing: choix hommage/question pour composer un courriel, sans stockage ni soumission.
Layout words by section: hero=présence / cérémonie=énoncé / approche=bande / parole=vis-à-vis / parcours=champ / contact=vis-à-vis / footer=marque.
Scores: design 6.5 · usability 8 · creativity 6.5 · content 7.5 → calcul brut 7.05, plafonné à 6.0 par le FAIL restant.
Caps applied: l'inspecteur compte trois éléments raster, mais seulement une photographie unique, donc FAIL `few-pictures`; plafonds Taste image et FAIL appliqués. Ce n'est PAS un gate 0 FAIL ni une preuve d'excellence esthétique.
Top three problèmes restant :
1. `final-check/desktop-page-01.jpg` : certains champs de texte en vis-à-vis restent austères, avec peu d'images de la pratique. Il faudrait de vrais portraits ou documents autorisés d'Alain en situation, non un paysage ajouté pour le score.
2. `final-check/mobile-page-01.jpg` : le bloc contact est plus standard que le premier écran; l'identité ACR ne s'y répète pas pour ne pas saturer.
3. `final-check/desktop-fold.jpg` : le portrait historique a une qualité/lumière différente de la typographie et des surfaces contemporaines; une séance portrait autorisée améliorerait le résultat plus qu'un effet CSS.

## Résultats techniques exacts
- `python3 -m unittest discover -s tests -v` : 4 tests OK. V1/V2/V3 : ancres, liens/assets relatifs, noindex,nofollow et robots. V2 HTML/CSS/JS identiques byte-à-byte à l'ancien HEAD, copiés avec ses assets; V1 inchangée.
- `node --check` : scripts V1, V2, V3 sans erreur. `lint.mjs site/index.html site/styles.css site/script.js` : 0 FAIL, 0 WARN.
- `inspect.mjs` final à 1440, 768, 390 : 1 FAIL (`few-pictures`), 2 WARN (`size-count` : 12 tailles CSS mesurées; `no-footage`). Pas d'overflow horizontal, images chargées, `consoleErrors: []` aux trois largeurs; 19 éléments bougent dans la mesure desktop. Polices DM Sans et Newsreader chargées depuis les fichiers locaux. Aucun clip honnête d'Alain disponible; une vidéo d'ambiance générique serait déplacée.
- Navigateur local : 320 px, scrollWidth 305 pour innerWidth 320 (15 px de scrollbar, aucun débordement). À 1440/768/390, même absence de débordement; navigation directe `/v1/`, `/v2/` et `/` chargée. Choix radio : sujets et corps distincts dans les URL mailto; lien direct et mailto par défaut présents sans JS. Détail texte intégral ouvert; Shift+Tab sur le lien d'évitement le rend visible à `top:12px` avec focus. Reduced motion : `scroll-behavior:auto`, durée d'animation limitée par CSS. Aucune requête de formulaire, analytique ou stockage.

## Limites de livraison
Le gate visuel est volontairement déclaré en échec plutôt que gonflé avec une image de Louis, le même portrait répété ou une vue de Montréal trompeuse. Les tailles typographiques distinctes mériteraient un resserrement ultérieur, mais sont lisibles. Confirmer les droits du portrait/logo, le courriel, les affiliations, l'étendue du Grand-Montréal et la copie métier avant toute publication. Aucun push ni déploiement réalisé ici.
