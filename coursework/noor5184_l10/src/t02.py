"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-11-21"
-------------------------------------------------------
"""
# Imports
import test_Sorts_List_linked as TS

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
    """
    -------------------------------------------------------
    Displays the comparison table for all linked-list sorts
    defined in Sorts_List_linked, using the helper functions
    and test_sort in test_Sorts_List_linked.
    -------------------------------------------------------
    """
    print(f"n: {TS.SIZE}")
    print(
        f"{'Algorithm':13s}"
        f"{'In Order':>8}{'Reversed':>8}{'Random':>11}"
        f"{'In Order':>8}{'Reversed':>8}{'Random':>11}"
    )
    print("-" * 80)

    for title, func in TS.SORTS:
        TS.test_sort(title, func)


if __name__ == "__main__":
    main()