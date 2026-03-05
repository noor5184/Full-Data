"""
-------------------------------------------------------
Tests for BST_linked methods: __contains__, node_counts,
parent (iterative), and parent_r (recursive).
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:      169105184
Email:   Noor5184@mylaurier.ca
__updated__ = "2025-11-22"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

# Constants
VALUES = [8, 3, 10, 1, 6, 14, 4, 7, 13]
SEARCH_KEYS = [3, 5, 14, 20]
PARENT_KEYS = [1, 3, 6, 8, 13, 42]


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
    """
    -------------------------------------------------------
    Builds a BST of integers and tests:
        - __contains__
        - node_counts
        - parent  (iterative)
        - parent_r (recursive)
    Use: main()
    -------------------------------------------------------
    Returns:
        None
    ------------------------------------------------------
    """
    bst = BST()

    for value in VALUES:
        bst.insert(value)

    print("BST contents (inorder):", bst.inorder())
    print()

    print("Testing __contains__:")
    for key in SEARCH_KEYS:
        print(f"{key} in bst: {key in bst}")
    print()

    zero, one, two = bst.node_counts()
    print("Testing node_counts:")
    print(f"Zero-child nodes : {zero}")
    print(f"One-child nodes  : {one}")
    print(f"Two-child nodes  : {two}")
    print()

    print("Testing parent (iterative):")
    for key in PARENT_KEYS:
        parent_value = bst.parent(key)
        print(f"parent({key})  -> {parent_value}")
    print()

    print("Testing parent_r (recursive):")
    for key in PARENT_KEYS:
        parent_value = bst.parent_r(key)
        print(f"parent_r({key}) -> {parent_value}")


if __name__ == "__main__":
    main()
