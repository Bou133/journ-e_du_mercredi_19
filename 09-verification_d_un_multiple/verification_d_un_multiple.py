"""exercice9.py
"""

__author__ = "boudom_a"


def is_multiple(n: int, m: int) -> bool:
    """vérification d'un multiple
    """
    if ( n % m == 0):
        return True
    else:
        return False

print(is_multiple(12, 4))
print(is_multiple(10, 3))