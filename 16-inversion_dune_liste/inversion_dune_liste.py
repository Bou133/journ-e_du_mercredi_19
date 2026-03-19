"""exercice11.py
"""


__author__ = "boudom_a"


def reverse_list(lst: list) -> list:
    """trouve l'inversion de la liste
    """
    m = []
    z = len(lst)
    for i in range(0, z):
        m.insert(i, lst[z-1-i])
    return m
