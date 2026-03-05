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
from List_linked import List
from Sorts_List_linked import Sorts
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
    tests = [
        [],
        [5],
        [170, 45, 75, 90, 802, 24, 2, 66],
        [5, 4, 3, 2, 1, 0],
        [10, 10, 3, 3, 3, 0, 100, 9, 9],
        [-5, -10, 3, 0, -1],
        [-1, -1, 0, 1],
        [0, -2, 2],
        [-100, -1, -50, -3],
    ]

    index = 1

    for values in tests:
        lst = List()
        for v in values:
            lst.append(v)

        print(f"Radix Sort (Linked) Test {index}")
        print("Original:", values)
        Sorts.radix_sort(lst)
        print("Sorted:  ", [v for v in lst])
        print()
        index += 1

    return


if __name__ == "__main__":
    main()