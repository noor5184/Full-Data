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
from Deque_linked import Deque
from Sorts_Deque_linked import Sorts
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
        [5, 4, 3, 2, 1, 0],
        [3, 1, 4, 1, 5, 9, 2, 6, 5],
        [10, 10, 3, 3, 3, 0, 100, 9, 9],
        [-5, -10, 3, 0, -1],
    ]

    index = 1

    for values in tests:
        dq = Deque()
        for v in values:
            dq.insert_rear(v)

        print(f"Gnome Sort (Deque) Test {index}")
        print("Original:", values)
        Sorts.swaps = 0
        Sorts.gnome_sort(dq)
        print("Sorted:  ", [x for x in dq])
        print("Swaps:   ", Sorts.swaps)
        print()
        index += 1

    return


if __name__ == "__main__":
    main()