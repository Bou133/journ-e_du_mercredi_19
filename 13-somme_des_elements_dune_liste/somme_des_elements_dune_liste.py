
"""exercice13.py
"""


__author__ = "boudom_a"


def sum_list(numbers: list) -> int:
    """verification d'un triangle rectangle
    """
    long = len(numbers)
    somme = 0
    for i in range(0, long):
        somme = somme + numbers[i]
    return somme
