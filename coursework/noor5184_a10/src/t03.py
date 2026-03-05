"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-11-29"
-------------------------------------------------------
"""
# Imports
from Sorts_array import Sorts
# Constants

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
    arrays = [
        [],
        [5],
        [5, 4, 3, 2, 1, 0],
        [3, 1, 4, 1, 5, 9, 2, 6, 5],
        [10, 10, 3, 3, 3, 0, 100, 9, 9],
    ]

    test_number = 1

    for values in arrays:
        data = values[:]
        Sorts.swaps = 0
        print(f"Gnome Sort Test {test_number}")
        print("Original:", data)
        Sorts.gnome_sort(data)
        print("Sorted:  ", data)
        print("Swaps:   ", Sorts.swaps)
        print()
        test_number += 1

    return


if __name__ == "__main__":
    main()