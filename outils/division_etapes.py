#!/usr/bin/env python3
"""Version interactive du script."""

def etapes_division(dividende, diviseur):
    quotient = dividende // diviseur
    reste = dividende % diviseur
    chiffres = [int(c) for c in str(dividende)]
    etapes = []
    partiel = 0
    for chiffre in chiffres:
        partiel = partiel * 10 + chiffre
        if partiel >= diviseur:
            q = partiel // diviseur
            p = q * diviseur
            etapes.append(p)
            partiel = partiel - p
    return etapes, quotient, reste


def main():
    print("=== Calcul des étapes d'une division euclidienne ===\n")
    try:
        dividende = int(input("Dividende : "))
        diviseur = int(input("Diviseur  : "))
    except ValueError:
        print("Erreur : entrez des entiers.")
        return

    etapes, quotient, reste = etapes_division(dividende, diviseur)

    print()
    print(f"Quotient : {quotient}")
    print(f"Reste    : {reste}")
    print(f"Étapes   : {etapes}")
    print()
    print("Commande LaTeX :")
    print()
    if etapes:
        etapes_str = "{" + ", ".join(str(e) for e in etapes) + "}"
        print(f"\\division[dividende={dividende}, diviseur={diviseur}, "
              f"solution, etapes={etapes_str}]")
    else:
        print(f"\\division[dividende={dividende}, diviseur={diviseur}, "
              f"solution]")


if __name__ == "__main__":
    main()