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
from Hash_Set_BST import Hash_Set
from functions import insert_words, comparison_total

# Constants
FILE = "gibbon.txt"
CAPACITY = 20

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
    # Open file
    fv = open(FILE, "r", encoding="utf-8")

    # Create BST-bucket Hash_Set
    hash_set = Hash_Set(CAPACITY)

    # Insert words from file
    insert_words(fv, hash_set)
    fv.close()

    # Total comparisons + word with max comparisons
    total, max_word = comparison_total(hash_set)

    print("Using linked BST Hash_Set")
    print(f"Total Comparisons: {total:,}")
    print(f"Word with maximum comparisons '{max_word.word}': {max_word.comparisons:,}")


if __name__ == "__main__":
    main()
