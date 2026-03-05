"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-11-22"
-------------------------------------------------------
"""
# Imports
from Hash_Set_sorted import Hash_Set
from functions import insert_words, comparison_total

# Constants
HASH_CAPACITY = 20
FILENAME = "gibbon.txt"


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """


def main():
    fv = open(FILENAME, "r", encoding="utf-8")
    hash_set = Hash_Set(HASH_CAPACITY)

    insert_words(fv, hash_set)
    fv.close()

    total, max_word = comparison_total(hash_set)

    print("Using array-based Sorted List Hash_Set")
    print(f"Total Comparisons: {total:,}")
    print(f"Word with maximum comparisons '{max_word.word}': {max_word.comparisons:,}")


if __name__ == "__main__":
    main()
