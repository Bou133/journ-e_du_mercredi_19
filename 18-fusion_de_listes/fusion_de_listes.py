"""exercice18.py
"""


__author__ = "Achile"


def merge_lists(list1: list, list2: list) -> list:
    """ calcul le nombre de digits d'un """
    enr_1 = set(list1)
    enr_2 = set(list2)
    enr_3 = {}
    enr_3 = enr_1.join(enr_2)
    enr_4 = list(enr_3)
    return enr_4

print(merge_lists([1, 2, 3], [3, 4, 5]))




