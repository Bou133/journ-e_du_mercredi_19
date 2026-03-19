"""exercice20.py
"""

__author__ = "Achile"


def contains(lst: list, element) -> bool:
    length = len(lst)
    for i in range(0, length):
        if (element in lst):
            return True
        else:
            return False
