"""exercice2.py
"""


__author__ = "boudom_a"


def is_palindrome(word: str) -> bool:
    """vérification de palindromes"""
    chaine = tuple(word)
    long = len(chaine)
    for i in range(0, long):
        if (chaine[long-1-i] != chaine[i]):
            return False
        else:
            return True
