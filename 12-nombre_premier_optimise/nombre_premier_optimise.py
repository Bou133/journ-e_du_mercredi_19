
"""exercice13.py
"""


__author__ = "boudom_a"


def is_prime_optimized(n: int) -> bool:
    """verification d'un nombre premier
    """
    resultat = []
    for j in range(0, n):
        resultat[j] = n % j
    if (resultat == 0):
        return False
    else:
        return True
