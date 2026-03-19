"""exercice03.py
"""

__author__ = "Achile"


def average(a: float, b: float, c: float) -> float:
    """Affiche le resultat d'une moyenne"""
    liste = [a, b, c]
    l = len(liste)
    somme = 0
    for i in range (0, l):
        somme = somme + liste[i]
    result = (somme / l)
    return result
