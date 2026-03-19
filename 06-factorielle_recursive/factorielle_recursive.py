"""exercice1.py
"""


__author__ = "Achile"


def recursive_factorial(n: int) -> int:
    """factorielle recursive"""
    while (n > 1):
        n = n * (n - 1)
    return n
