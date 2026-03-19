"""exercice19.py
"""


__author__ = "Achile"


def is_anagram(word1: str, word2: str) -> bool:
    """trouve l'anagram
    """
    tw1 = tuple(word1)
    tw2 = tuple(word2)
    m = []
    z = len(tw1)
    for i in tw1:
        if (i in tw2):
            return True
        else:
            return False
    for j in tw2:
        if (j in tw1):
            return True
        else:
            return False
