# outilsprof

Package LaTeX d'outils pour l'enseignement (collège).

## Auteur

Jean Roussie — Collège La Boétie, Sarlat (Dordogne)

## Installation

### Installation locale (recommandée)

1. Copiez `outilsprof.sty` dans `~/Library/texmf/tex/latex/outilsprof/` (macOS) ou dans `~/texmf/tex/latex/outilsprof/` (Linux)
2. Lancez `texhash ~/Library/texmf` (ou `mktexlsr`)
3. Dans votre document : `\usepackage{outilsprof}`

### Installation globale

Placez `outilsprof.sty` dans un dossier reconnu par TeX Live, puis lancez `texhash`.

## Commandes disponibles

- `\axegradue` et `\axegraduepoints` — axe gradué horizontal
- `\reperegradue` et `\reperegraduepoints` — repère orthogonal gradué
- Boîtes colorées — mise en valeur pédagogique
- `\division` — division euclidienne posée
- `\addition`, `\soustraction`, `\multiplication` — opérations posées
- Masquage de chiffres avec `|` dans les opérations
- `\unite` — grandeur avec unité
- `\degre` — angle en degrés, minutes, secondes
- `\dureeminute`, `\dureeheure`, `\dureejour`, `\dureesemaine` — durées
- `\additiondurees`, `\soustractiondurees`, `\additionangles`, `\soustractionangles` — opérations posées sur durées et angles

* * *

## `\axegradue`

Trace un axe gradué horizontal avec TikZ.

### Paramètres nommés

Clé | Description | Défaut
---|---|---
`longueur` | Largeur relative (0.8 = 80% de `\textwidth`) | `0.8`
`debut` | Début de la graduation | `0`
`fin` | Fin de la graduation | `100`
`pas` | Pas entre nombres repères | `10`
`nombre` | Nombre de sous-intervalles entre repères | `2`
`points` | Liste `{A/120, B/340/blue}` | vide

### Exemples

    \axegradue
    \axegradue[longueur=0.8, fin=400, pas=100, nombre=5]
    \axegradue[debut=100, fin=500, pas=100, nombre=5]
    \axegradue[points={A/120, B/340/blue, C/60/green}]

### Syntaxe des points

- `nom/position` → intérieur rouge, étiquette noire
- `nom/position/couleur` → intérieur de la couleur, étiquette noire

### `\axegraduepoints`

Variante avec les points en argument obligatoire.

    \axegraduepoints[longueur=0.8, fin=400, pas=100, nombre=5]{A/120, B/340/blue}

* * *

## `\reperegradue`

Trace un repère orthogonal gradué avec TikZ.

### Paramètres nommés

Clé | Description | Défaut
---|---|---
`longueur` | Largeur relative (0.8 = 80% de `\textwidth`) | `0.8`
`bg` | Coin bas-gauche `(x,y)` | `{(-10,-10)}`
`hd` | Coin haut-droit `(x,y)` | `{(10,10)}`
`origine` | Intersection des axes `(x,y)` | `{(0,0)}`
`grille` | Pas de la grille fine (0 = pas de grille) | `1`
`pasx` | Pas entre repères sur l'axe des abscisses | `1`
`pasy` | Pas entre repères sur l'axe des ordonnées | `1`
`nombrex` | Nb de sous-intervalles entre repères (x) | `1`
`nombrey` | Nb de sous-intervalles entre repères (y) | `1`
`points` | Liste `{A/(4,5), B/(-2,3)/blue}` | vide
`affichernom` | Afficher le nom du point | `true`
`affichercoords` | Afficher les coordonnées du point | `false`

### Remarque importante

Les valeurs de `bg`, `hd` et `origine` contiennent une virgule. **Elles doivent être protégées par des accolades**, sinon `l3keys` interprète la virgule comme un séparateur de clés :

    % ❌ Ne fonctionne pas
    \reperegradue[bg=(-5,-5), hd=(5,5)]

    % ✅ Correct
    \reperegradue[bg={(-5,-5)}, hd={(5,5)}]

La liste `points` **n'a pas besoin** de cette protection : la virgule interne aux parenthèses est automatiquement détectée et protégée par le package.

### Exemples

    % Repère par défaut : fenêtre [-10,10]×[-10,10], grille de 1
    \reperegradue

    % Fenêtre plus petite
    \reperegradue[bg={(-5,-5)}, hd={(5,5)}, grille=1]

    % Fenêtre avec grille plus fine
    \reperegradue[bg={(-4,-2)}, hd={(3,6)}, grille=0.5]

    % Origine décalée
    \reperegradue[bg={(-5,-5)}, hd={(5,5)}, origine={(2,3)}]

    % Grille désactivée
    \reperegradue[grille=0]

    % Graduations principales personnalisées
    \reperegradue[bg={(-10,-10)}, hd={(10,10)}, pasx=2, pasy=2]
    \reperegradue[bg={(-10,-10)}, hd={(10,10)},
                  pasx=5, pasy=5, nombrex=5, nombrey=5]

    % Repère avec points, syntaxe naturelle
    \reperegradue[points={A/(4,5), B/(-2,3)/blue, C/(1,-2)/green}]

    % Repère avec coordonnées affichées sous les noms
    \reperegradue[points={A/(4,5), B/(-2,3)/blue},
                  affichernom=true, affichercoords=true]

    % Repère sans nom mais avec coordonnées
    \reperegradue[points={A/(4,5), B/(-2,3)/blue},
                  affichernom=false, affichercoords=true]

    % Repère avec points seulement (aucune étiquette)
    \reperegradue[points={A/(4,5), B/(-2,3)/blue},
                  affichernom=false, affichercoords=false]

### Syntaxe des points

- `nom/(x,y)` → intérieur rouge (défaut), étiquette noire
- `nom/(x,y)/couleur` → intérieur de la couleur spécifiée

La couleur peut être n'importe quelle couleur TikZ, y compris les couleurs composées (`orange!80!black`, `red!70`, etc.).

### Étiquette de l'intersection des axes

Le package affiche automatiquement l'étiquette appropriée au point d'intersection des axes :

- Si l'origine est `(0,0)` → affiche **O**
- Sinon → affiche **Ω(a;b)** où `a` et `b` sont les coordonnées de l'intersection

    \reperegradue                              % → affiche "O"
    \reperegradue[origine={(2,3)}]             % → affiche "Ω(2;3)"
    \reperegradue[origine={(-2,-3)}]           % → affiche "Ω(-2;-3)"
    \reperegradue[origine={(0,3)}]             % → affiche "Ω(0;3)"

### `\reperegraduepoints`

Variante avec les points en argument obligatoire.

    \reperegraduepoints[bg={(-5,-5)}, hd={(5,5)}]{A/(2,3), B/(-1,-2)/orange}

* * *

## Boîtes colorées

Trois boîtes thématiques sont disponibles, chacune avec une couleur par défaut modifiable via un argument optionnel.

### `\begin{retenir}[couleur] ... \end{retenir}`

Boîte « À retenir absolument » — couleur par défaut : **bleu**.

    \begin{retenir}
        Le théorème de Pythagore : $a^2 + b^2 = c^2$.
    \end{retenir}

    \begin{retenir}[orange]
        Version personnalisée en orange.
    \end{retenir}

### `\begin{vigilance}[couleur] ... \end{vigilance}`

Boîte « Attention ! » — couleur par défaut : **rouge**.

    \begin{vigilance}
        Ne pas oublier de vérifier les unités !
    \end{vigilance}

    \begin{vigilance}[purple]
        Version personnalisée en violet.
    \end{vigilance}

### `\begin{methode}[couleur] ... \end{methode}`

Boîte « Méthode de résolution » — couleur par défaut : **vert**.

    \begin{methode}
        1. Identifier les données \\
        2. Choisir la formule \\
        3. Calculer
    \end{methode}

### Commandes équivalentes

Les mêmes boîtes sont accessibles sous forme de commandes :

    \boiteRetenir{Contenu}
    \boiteRetenir[orange]{Contenu personnalisé}

    \boiteVigilance{Contenu}
    \boiteVigilance[purple]{Contenu personnalisé}

    \boiteMethode{Contenu}
    \boiteMethode[cyan]{Contenu personnalisé}

### `\boitecalcul[largeur][hauteur]{contenu}`

Boîte neutre pour les calculs, centrée horizontalement et verticalement.

**Paramètres optionnels :**

Argument | Description | Défaut
---|---|---
largeur | Largeur de la boîte | `10cm`
hauteur | Hauteur de la boîte | `3cm`

    \boitecalcul{$2 + 2 = 4$}
    \boitecalcul[8cm][4cm]{$\frac{3}{4} + \frac{1}{2} = \frac{5}{4}$}

### Couleurs par défaut

Les couleurs par défaut sont définies et peuvent être redéfinies dans le préambule du document :

    \definecolor{couleurRetenir}{RGB}{0,102,204}    % Bleu
    \definecolor{couleurVigilance}{RGB}{204,0,0}    % Rouge
    \definecolor{couleurMethode}{RGB}{0,153,76}     % Vert

  ### Lignes de réponse

Deux commandes pour créer des lignes à compléter dans les exercices.

```latex
\reponse           % ligne de 6 cm
\reponse[3cm]      % ligne de 3 cm
\grandeReponse     % ligne sur toute la largeur
\grandeReponse[0.5] % ligne sur 50 % de la largeur
```

Paramètres :

| Commande | Argument | Défaut | Description |
|---|---|---|---|
| `\reponse` | longueur (avec unité) | `6cm` | longueur de la ligne |
| `\grandeReponse` | facteur (sans unité) | `1` | fraction de `\textwidth` |

* * *

## Opérations posées

Le package fournit trois commandes pour poser les opérations
élémentaires : `\addition`, `\soustraction` et `\multiplication`.
Le rendu est entièrement en TikZ (aucun `\halign`, aucun `&`),
ce qui garantit un comportement identique quel que soit le moteur
(pdfLaTeX, LuaLaTeX, XeLaTeX, TexpadTeX).

### Options communes

Les trois commandes partagent les mêmes options nommées :

Clé | Description | Défaut
---|---|---
`solution` | Affiche le résultat | `false`
`taille` | Taille de police (`normalsize`, `large`, `Large`, `small`…) | `normalsize`

### `\addition[options]{terme1, terme2, ...}`

Pose une addition de deux termes ou plus. Les termes sont séparés
par des virgules et affichés les uns sous les autres, précédés du
signe `+`.

```latex
\addition{1234, 5678}
\addition[solution]{1234, 5678}
\addition[solution, taille=large]{1234, 5678, 91011}
```

### `\soustraction[options]{terme1, terme2}`

Pose une soustraction de deux termes. La commande **gère
automatiquement l'ordre** : si le premier terme est plus petit que
le second, ils sont échangés pour éviter un résultat négatif.

```latex
\soustraction{853, 476}
\soustraction[solution]{853, 476}
\soustraction[solution]{476, 853}
```

> **Attention** : `\soustraction` attend **exactement deux termes**.
> Toute autre quantité déclenche une erreur explicite.

### `\multiplication[options]{facteur1, facteur2}`

Pose une multiplication de deux facteurs. Si le multiplicateur
(second facteur) comporte plusieurs chiffres :
- l'espace des produits partiels est toujours réservé, avec un
  trait de séparation sous ces lignes ;
- les **valeurs** des produits partiels et le **résultat final**
  ne s'affichent que si l'option `solution` est activée.

```latex
\multiplication{234, 56}
\multiplication[solution]{234, 56}
\multiplication[solution, taille=large]{1234, 567}
```

> **Attention** : `\multiplication` attend **exactement deux facteurs**.

### Masquage de chiffres

Pour créer des exercices à trous, un `|` placé devant un chiffre
dans un terme indique que ce chiffre doit être utilisé dans le
calcul mais remplacé par un underscore bas à l'affichage.

```latex
\addition[solution]{1|4, 56}
```

Affiche :

```text
    1 _
+   5 6
─────────
    7 0
```

Le chiffre `4` est bien utilisé dans le calcul (`14 + 56 = 70`),
mais masqué par un `_` dans l'énoncé.

#### Règles

- `|` masque **le chiffre qui suit** : `1|4` → `1 _`
- `|` en fin de nombre masque un `0` implicite : `47|` → `4 7 _`
- Deux `|` consécutifs masquent deux chiffres : `||4` → `_ _`
- Le résultat n'est **jamais masqué**, seulement les termes

#### Exemples

```latex
% Addition avec un chiffre masqué
\addition[solution]{1|4, 56}

% Soustraction avec deux chiffres masqués
\soustraction[solution]{8|3, 47|}

% Multiplication avec un chiffre masqué dans le multiplicateur
\multiplication[solution]{24, 5|6}
```

#### Sur les durées et les angles

Le même marqueur `|` s'applique aux opérations sur durées et angles,
composante par composante :

```latex
\additiondurees[solution]{3+1|2, 5+30}
% → « 3 j 1 _ h » + « 5 j 30 h » = « 3 j 17 h 30 min »

\additionangles[solution]{5|6+30, 12+45}
% → « 5 _° 30′ » + « 12° 45′ » = « 68° 15′ »
```

#### Combinaison avec `solution`

Le masquage est indépendant de l'option `solution` :

- `\addition[solution]{1|4, 56}` → termes masqués **et** résultat affiché
- `\addition{1|4, 56}` → termes masqués, résultat masqué

### `\division[options]`

Pose une division euclidienne. Voir la section dédiée
« Division euclidienne et utilitaire `division_etapes.py` »
ci-dessous pour la syntaxe complète.

```latex
\division[dividende=1234, diviseur=56, solution]
\division[dividende=87765, diviseur=123, solution, etapes={861, 123, 369}]
```

* * *

## Grandeurs, angles et durées

La section 4 regroupe quatre familles de commandes : les grandeurs
avec unités, les angles, les durées, et les opérations posées sur
ces deux dernières.

### `\unite{nombre}{unité}`

Affiche une grandeur suivie de son unité, en respectant la
typographie française (virgule décimale, espace insécable avant
l'unité). Basée sur `\SI` de `siunitx`.

```latex
\unite{6}{m}              % → 6 m
\unite{2,5}{kg}           % → 2,5 kg
\unite{9,81}{m/s^2}       % → 9,81 m/s²
\unite{5}{m^2}            % → 5 m²
```

Pour les exposants, utilisez la notation `^2`, `^3` ou les macros
`\squared`, `\cubed` de `siunitx`.

### `\degre{degrés+minutes+secondes}`

Affiche un angle en degrés, minutes et secondes. Le séparateur est
le signe `+`. Les composantes manquantes sont implicitement 0.

```latex
\degre{56}                % → 56°
\degre{56+30}             % → 56°30′
\degre{56+30+15}          % → 56°30′15″
```

### Durées simples

Quatre commandes, une par point de départ. Le séparateur est encore
le `+`. Chaque commande descend automatiquement jusqu'à l'unité la
plus petite non nulle.

Commande | Exemple | Rendu
---|---|---
`\dureeminute{...}` | `\dureeminute{12+30}` | 12 min 30 s
`\dureeheure{...}` | `\dureeheure{5+45+30}` | 5 h 45 min 30 s
`\dureejour{...}` | `\dureejour{3+12+30+15}` | 3 j 12 h 30 min 15 s
`\dureesemaine{...}` | `\dureesemaine{2+3+12}` | 2 sem 3 j 12 h

### Opérations sur durées et angles

Quatre commandes pour poser les additions et soustractions de
durées et d'angles, avec **retenues et emprunts gérés
automatiquement**.

```latex
\additiondurees[solution]{3+12, 5+30}
\soustractiondurees[solution]{5+30, 2+45}
\additionangles[solution]{56+30, 12+45}
\soustractionangles[solution]{56+30+15, 12+45+30}
```

Chaque terme est une liste séparée par `+` :

- **Durées** : `jours+heures+minutes+secondes`
- **Angles** : `degrés+minutes+secondes`

**Option commune** :

Clé | Description | Défaut
---|---|---
`solution` | Affiche le résultat | `false`

**Comportement** :

- Les colonnes sont alignées verticalement (j/h/min/s ou °/′/″).
- Les composantes nulles à droite sont masquées.
- Le trait horizontal s'arrête à la dernière colonne utilisée par
  les termes.
- Si le résultat est négatif, un signe `−` est affiché devant.

**Exemple** :

```latex
\additiondurees[solution]{3+12+30, 5+30}
```

Donne :

```text
        3 j   12 h   30 min
+       5 j   30 h
─────────────────────────────
        9 j   18 h   30 min
```

**Cas particuliers** :

- Les retenues et emprunts ne sont **pas affichés visuellement**
  dans la pose.
- Une soustraction donnant un résultat négatif affiche le signe
  `−` : `\soustractionangles{12+45, 56+30}` → `− 43° 45′`.

**Attention à ne pas confondre** avec les commandes de la section 3
(`\addition`, `\soustraction`) qui opèrent sur des nombres nus.

* * *

## Division euclidienne et utilitaire `division_etapes.py`

La commande `\division` pose une division euclidienne complète
avec le dividende, le diviseur, la barre verticale, le quotient
et — si fournies — les étapes intermédiaires (produits partiels
à soustraire).

### Options de `\division`

Clé | Description | Défaut
---|---|---
`dividende` | Entier à diviser | `0`
`diviseur` | Entier diviseur (non nul) | `1`
`solution` | Affiche quotient et reste | `false`
`etapes` | Liste des produits partiels, séparés par des virgules | vide

> **Les nombres doivent être saisis sans espaces insécables (`~`).**
> Utilisez uniquement l'espace normal ou rien du tout.

### Calcul des étapes : `division_etapes.py`

Le script `outils/division_etapes.py` calcule automatiquement les
étapes d'une division euclidienne et génère la commande `\division`
correspondante, prête à copier dans un document LaTeX.

#### Utilisation

```bash
python3 division_etapes.py
python3 division_etapes.py 1234
python3 division_etapes.py 1234 56
python3 division_etapes.py 1234 56 -o division.tex
```

#### Sortie console

```text
$ python3 division_etapes.py 1234 56

==================================================
Dividende : 1234
Diviseur  : 56
Quotient  : 22
Reste     : 2
Étapes    : [112, 112]
==================================================

Commande LaTeX :

\division[dividende=1234, diviseur=56, solution, etapes={112, 112}]
```

#### Génération d'un fichier `.tex`

Avec l'option `-o` (ou `--tex`), le script écrit en plus un
fichier `.tex` complet, prêt à compiler :

```bash
python3 division_etapes.py 87765 123 -o division.tex
pdflatex division.tex
```

#### Comportement en cas d'erreur

Si les étapes fournies à `\division` ne correspondent pas au calcul
attendu, le package affiche une boîte d'erreur rouge à la place de
la division. C'est une sécurité pédagogique.

* * *

## Exemples

Un fichier de démonstration complet est disponible dans `examples/exemples.tex`. Pour le compiler :

    cd examples
    pdflatex exemples.tex

* * *

## Aide-mémoire rapide

    % Axe gradué
    \axegradue[fin=400, pas=100, nombre=5, points={A/120, B/340/blue}]

    % Repère par défaut
    \reperegradue

    % Repère personnalisé avec points
    \reperegradue[
        bg={(-6,-6)}, hd={(6,6)},
        origine={(0,0)},
        grille=1,
        pasx=1, pasy=1,
        nombrex=1, nombrey=1,
        points={A/(4,5), B/(-2,3)/blue, C/(1,-2)/green},
        affichernom=true,
        affichercoords=false
    ]

    % Boîtes
    \begin{retenir}[bleu] ... \end{retenir}
    \begin{vigilance}[rouge] ... \end{vigilance}
    \begin{methode}[vert] ... \end{methode}
    \boitecalcul[8cm][4cm]{...}

    % Opérations posées
    \addition[solution]{1234, 5678}
    \soustraction[solution]{853, 476}
    \multiplication[solution]{234, 56}
    \division[dividende=1234, diviseur=56, solution, etapes={112, 112}]

    % Masquage de chiffres
    \addition[solution]{1|4, 56}
    \additiondurees[solution]{3+1|2, 5+30}

    % Grandeurs, angles, durées
    \unite{9,81}{m/s^2}
    \degre{56+30+15}
    \dureeheure{5+45+30}
    \additionangles[solution]{56+30, 12+45}
    \soustractionangles[solution]{56+30+15, 12+45+30}

* * *

## Licence

MIT