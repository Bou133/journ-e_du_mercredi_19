"""exercice7.py
"""


__author__ = "Achile"


def fibonacci(n: int) -> int:
    """calcul le nombre de digits
    """
    if (n == 1 or n == 2 or n == 0):
        return 1
    else:
        ul = []
        ul.insert(0, 0)
        ul.insert(1, 1)
        while(n > 1):
            ul[n] = (ul[n-2] + ul[n-1])
        return ul[n]



print(fibonacci(6))
