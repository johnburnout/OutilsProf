#!/usr/bin/env python3
"""
Calcule les étapes d'une division euclidienne
pour la commande LaTeX \\division du package outilsprof.

Usage :
    python division_etapes.py                  # demande tout
    python division_etapes.py 1234             # demande le diviseur
    python division_etapes.py 1234 56          # calcule direct
    python division_etapes.py 1234 56 789      # ignore le 3e argument

Exemples :
    $ python division_etapes.py 1234 56
    \\division[dividende=1234, diviseur=56, solution, etapes={112, 112}]

    $ python division_etapes.py 987654 321
    \\division[dividende=987654, diviseur=321, solution, etapes={963, 2247, 1926}]
"""

import sys


# ------------------------------------------------------------
# Calcul des étapes
# ------------------------------------------------------------
def etapes_division(dividende: int, diviseur: int) -> tuple[list[int], int, int]:
    """
    Calcule les produits partiels d'une division euclidienne.

    Retourne :
        (etapes, quotient, reste)
    où `etapes` est la liste des produits partiels (un par étape),
    dans l'ordre où ils apparaissent dans la division posée.
    """
    if diviseur == 0:
        raise ValueError("Le diviseur ne peut pas être zéro.")

    quotient = dividende // diviseur
    reste = dividende % diviseur

    # Liste des chiffres du dividende
    chiffres = [int(c) for c in str(dividende)]

    etapes = []
    partiel = 0

    for chiffre in chiffres:
        partiel = partiel * 10 + chiffre

        if partiel >= diviseur:
            # Quotient partiel = chiffre du quotient
            q_partiel = partiel // diviseur
            # Produit partiel
            produit = q_partiel * diviseur
            etapes.append(produit)
            # Nouveau partiel = reste partiel
            partiel = partiel - produit

    return etapes, quotient, reste


# ------------------------------------------------------------
# Formatage LaTeX
# ------------------------------------------------------------
def format_latex(etapes: list[int]) -> str:
    """Formate la liste des étapes pour LaTeX."""
    return "{" + ", ".join(str(e) for e in etapes) + "}"


def commande_latex(dividende: int, diviseur: int) -> str:
    """Retourne la commande \\division complète."""
    etapes, quotient, reste = etapes_division(dividende, diviseur)
    if etapes:
        etapes_str = format_latex(etapes)
        return (f"\\division[dividende={dividende}, diviseur={diviseur}, "
                f"solution, etapes={etapes_str}]")
    else:
        return (f"\\division[dividende={dividende}, diviseur={diviseur}, "
                f"solution]")


# ------------------------------------------------------------
# Saisie interactive avec validation
# ------------------------------------------------------------
def demander_entier(prompt: str) -> int:
    """
    Demande un entier à l'utilisateur, avec validation.
    Redemande tant que la saisie n'est pas un entier valide.
    """
    while True:
        try:
            valeur = input(prompt).strip()
            return int(valeur)
        except ValueError:
            print(f"  Erreur : '{valeur}' n'est pas un entier valide.")
            print("  Réessayez.")


def demander_diviseur() -> int:
    """
    Demande le diviseur, en s'assurant qu'il n'est pas nul.
    """
    while True:
        diviseur = demander_entier("Diviseur  : ")
        if diviseur == 0:
            print("  Erreur : le diviseur ne peut pas être zéro.")
            print("  Réessayez.")
        else:
            return diviseur


# ------------------------------------------------------------
# Programme principal
# ------------------------------------------------------------
def main():
    # Analyse des arguments de la ligne de commande
    args = sys.argv[1:]

    dividende = None
    diviseur = None

    # Cas 1 : 2 arguments ou plus → on prend les deux premiers
    if len(args) >= 2:
        try:
            dividende = int(args[0])
            diviseur = int(args[1])
            if diviseur == 0:
                print("Erreur : le diviseur ne peut pas être zéro.")
                sys.exit(1)
        except ValueError:
            print("Erreur : les arguments doivent être des entiers.")
            print(f"Reçu : {args[0]!r}, {args[1]!r}")
            sys.exit(1)

    # Cas 2 : 1 argument → on a le dividende, on demande le diviseur
    elif len(args) == 1:
        try:
            dividende = int(args[0])
        except ValueError:
            print(f"Erreur : '{args[0]}' n'est pas un entier valide.")
            sys.exit(1)
        print(f"Dividende : {dividende}")
        diviseur = demander_diviseur()

    # Cas 3 : aucun argument → on demande tout
    else:
        print("=== Calcul des étapes d'une division euclidienne ===")
        print()
        dividende = demander_entier("Dividende : ")
        diviseur = demander_diviseur()

    # Calcul
    etapes, quotient, reste = etapes_division(dividende, diviseur)

    # Affichage
    print()
    print("=" * 50)
    print(f"Dividende : {dividende}")
    print(f"Diviseur  : {diviseur}")
    print(f"Quotient  : {quotient}")
    print(f"Reste     : {reste}")
    print(f"Étapes    : {etapes}")
    print("=" * 50)
    print()
    print("Commande LaTeX :")
    print()
    print(commande_latex(dividende, diviseur))
    print()


if __name__ == "__main__":
    main()