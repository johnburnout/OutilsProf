# Changelog

Toutes les modifications notables de ce projet sont documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/)
et ce projet adhère au [Semantic Versioning](https://semver.org/lang/fr/).

## [1.10] - 2026-09-24

### Ajouté
- Section 2 : commande `\reponse` pour tracer une ligne à compléter
  de longueur fixe (6 cm par défaut, modifiable via un argument
  optionnel).
- Section 2 : commande `\grandeReponse` pour tracer une ligne à
  compléter sur une fraction de `\textwidth` (1 par défaut).
- Rendu basé sur `\rule[-0.5ex]{longueur}{0.4pt}` : trait net,
  positionné sous la ligne de base, épaisseur contrôlée.

### Exemples
\reponse              → ligne de 6 cm
\reponse[3cm]         → ligne de 3 cm
\grandeReponse        → ligne sur toute la largeur
\grandeReponse[0.5]   → ligne sur 50 % de la largeur

### Version
- 1.9 → 1.10

## [1.9] - 2026-09-23

### Ajouté
- Masquage de chiffres avec `|` dans les opérations de nombres
  (`\addition`, `\soustraction`, `\multiplication`) : le chiffre
  qui suit le `|` est utilisé dans le calcul mais remplacé par
  un underscore bas à l'affichage.
- Même fonctionnalité pour les opérations sur durées et angles
  (`\additiondurees`, `\soustractiondurees`, `\additionangles`,
  `\soustractionangles`).

### Exemple
\addition[solution]{1|4, 56}   →  « 1 _ » + « 5 6 » = « 7 0 »

## [1.8] - 2026-09-23

### Ajouté
- Section 4-A : commande `\unite{nombre}{unité}` pour afficher une
  grandeur avec son unité, via `\SI` de `siunitx` (typographie
  française automatique : virgule décimale, espace insécable).
- Section 4-B : commande `\degre{degrés+minutes+secondes}` pour les
  angles en degrés, minutes et secondes.
- Section 4-C : commandes `\dureeminute`, `\dureeheure`,
  `\dureejour` et `\dureesemaine` pour les durées, du plus petit
  point de départ au plus grand.
- Section 4-D : commandes `\additiondurees`, `\soustractiondurees`,
  `\additionangles` et `\soustractionangles` pour poser les
  opérations sur durées et angles.
  - Retenues et emprunts gérés automatiquement.
  - Colonnes alignées verticalement (j/h/min/s ou °/′/″).
  - Composantes nulles à droite masquées.
  - Trait ajusté à la dernière colonne utilisée par les termes.
  - Signe « − » affiché si le résultat est négatif.
  - Option `solution` pour afficher ou masquer le résultat.
- Déclaration des unités personnalisées `\jour` (j) et
  `\semaine` (sem) via `\DeclareSIUnit`.

### Corrigé
- Section 1-B : `\reperegradue` écrasait la commande publique
  `\unite` par une variable interne (facteur d'échelle du repère).
  La variable est renommée `\repereUnite`, ce qui évite le conflit.
- Section 4-B : `\degre` était déjà défini par `babel french`.
  Utilisation de `\RenewDocumentCommand` pour éviter l'erreur
  « Command \degre already defined ».
- Section 4-A et 4-C : utilisation de `\SI` (siunitx v2) au lieu
  de `\qty` (siunitx v3), pour compatibilité avec TexpadTeX.

### Version
- 1.7.2 → 1.8

## [1.7.2] - 2026-09-22

### Modifié
- Section 2 : les boîtes colorées (`\boiteRetenir`, `\boiteVigilance`,
  `\boiteMethode` et les environnements `retenir`, `vigilance`,
  `methode`) sont désormais centrées horizontalement.
- `\boitecalcul` reste inchangée : elle possède déjà sa propre
  largeur fixe.

### Version
- 1.7.1 → 1.7.2

## [1.7.1] - 2026-09-18

### Ajouté
- Utilitaire `outils/division_etapes.py` pour calculer
  automatiquement les étapes d'une division euclidienne et
  générer la commande `\division` correspondante.
- Option `-o` / `--tex` du script pour écrire un fichier `.tex`
  autonome, prêt à compiler.

### Corrigé
- Section 3-A : affichage complet du reste dans `\division`
  quand celui-ci comporte plusieurs chiffres (bug de
  collision entre la variable source et la variable
  destination de `\__div_char:nn`).

### Version
- 1.7 → 1.7.1

## [1.7] - 2026-09-17

### Corrigé
- Section 3-B, `\addition` : correction de l'erreur
  « Illegal unit of measure (pt inserted) » lors du calcul
  de `\l_tmpa_dim`. Utilisation d'une variable dédiée
  `\l__op_nbchiffres_int` et calcul explicite.
- Section 3-A, `\division` : la syntaxe attend désormais une
  seule liste d'options
  `\division[dividende=..., diviseur=..., solution, etapes={...}]`.

### Ajouté
- `\l__op_nbchiffres_int` déclarée dans la section 3-B.

### Version
- 1.6 → 1.7

## [1.6] - 2026-09-16

### Ajouté
- Section 3-A : commande `\division` pour poser une division
  euclidienne en TikZ, avec options `dividende`, `diviseur`,
  `solution` et `etapes`.
- Section 3-B : commandes `\addition`, `\soustraction` et
  `\multiplication` pour poser les opérations élémentaires
  en TikZ, avec options `solution` et `taille`.
- Rendu entièrement TikZ : plus aucun `\halign` ni `&`.

### Modifié
- Déclaration explicite de `\l__op_solution_bool` dans la
  section 3-B.

### Supprimé
- Les `\typeout` de débogage hérités des versions précédentes.

### Compatibilité
- expl3 2017/12/16 (TexpadTeX), boucles via
  `\int_while_do:nNnn`.

### Version
- 1.5 → 1.6

## [1.5] - 2026-09-15

### Modifié
- `\boitecalcul` : le contenu devient facultatif (3ᵉ argument
  optionnel).

### Corrigé
- Mise à jour de `\ProvidesPackage` (cohérence version/date).

### Version
- 1.3 → 1.5

> **Note** : la version 1.4 n'a pas fait l'objet d'une
> publication séparée.

## [1.3] - 2026-09-12

### Corrigé
- Section 3-A : décalage de la division ajusté.
- Suppression des `\typeout` de débogage.

### Version
- 1.2 → 1.3

## [1.2] - 2026-09-11

### Ajouté
- Boîtes colorées pour la mise en valeur pédagogique :
  - Environnement `retenir` (bleu par défaut) et commande
    `\boiteRetenir`
  - Environnement `vigilance` (rouge par défaut) et commande
    `\boiteVigilance`
  - Environnement `methode` (vert par défaut) et commande
    `\boiteMethode`
  - Commande `\boitecalcul` avec dimensions réglables
- Couleurs par défaut personnalisables : `couleurRetenir`,
  `couleurVigilance`, `couleurMethode`
- Chaque boîte accepte un argument optionnel pour changer sa
  couleur
- Nouvelle commande `\reperegradue` : trace un repère orthogonal
  gradué avec TikZ
  - Fenêtre rectangulaire personnalisable via `bg` et `hd`
  - Position de l'intersection des axes personnalisable via
    `origine`
  - Grille fine optionnelle via `grille`
  - Graduations principales et secondaires indépendantes sur
    chaque axe (`pasx`, `pasy`, `nombrex`, `nombrey`)
  - Placement de points avec syntaxe naturelle
    `points={A/(4,5), B/(-2,3)/blue, C/(1,-2)/green}`
    (les virgules internes aux parenthèses sont automatiquement
    protégées)
- Nouvelle commande `\reperegraduepoints` : variante de
  `\reperegradue` avec les points en argument obligatoire
- Étiquette dynamique au point d'intersection des axes :
  - `O` si l'origine est `(0,0)`
  - `Ω(a;b)` sinon, avec les coordonnées de l'intersection
- Nouvelles options pour les étiquettes de points :
  - `affichernom` (booléen, `true` par défaut) : afficher le
    nom du point
  - `affichercoords` (booléen, `false` par défaut) : afficher
    les coordonnées du point sous la forme `(x;y)`

### Modifié
- Section 1-B du package : `\reperegradue` bénéficie de toutes
  les améliorations issues des tests intensifs
- Le découpage de la liste `points` est désormais robuste : les
  virgules internes aux parenthèses sont détectées et protégées,
  ce qui permet la syntaxe naturelle sans accolades
  supplémentaires

### Corrigé
- Bug d'unités TikZ : les coordonnées des tracés sont maintenant
  explicitement en points (`pt`), ce qui évite un débordement
  vertical et horizontal du `tikzpicture`
- Bug de découpage des points multiples : `\foreach` traite
  correctement chaque point individuellement
- Bug d'affichage des couleurs : la couleur d'un point ne
  s'affiche plus à côté de son étiquette
- Bug `(NaN,NaN)` : les coordonnées vides ne sont plus transmises
  à `\pgfmathsetmacro`

## [1.0] - 2026-09-10

### Ajouté
- Première version de `\axegradue` : trace un axe gradué
  horizontal avec TikZ
  - Paramètres nommés : `longueur`, `debut`, `fin`, `pas`,
    `nombre`, `points`
  - Placement de points avec syntaxe `nom/position` ou
    `nom/position/couleur`
- Première version de `\axegraduepoints` : variante avec les
  points en argument obligatoire