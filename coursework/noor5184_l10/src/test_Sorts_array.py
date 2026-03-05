"""
-------------------------------------------------------
Tests various array-based sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2025-11-21"
-------------------------------------------------------
"""
# Imports
import random
from Number import Number
from Sorts_array import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
    from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    values = []

    for i in range(SIZE):
        values.append(Number(i))

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
    from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    values = []

    for i in range(SIZE - 1, -1, -1):
        values.append(Number(i))

    return values



def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: arrays = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """
    arrays = []

    for _ in range(TESTS):
        row = []
        for _ in range(SIZE):
            value = random.randint(0, XRANGE)
            row.append(Number(value))
        arrays.append(row)

    return arrays



def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """
    
    """
    # Sorted list test
    values = create_sorted()
    Number.comparisons = 0
    Sorts.swaps = 0
    func(values)
    sorted_comparisons = Number.comparisons

    # Reversed list test
    values = create_reversed()
    Number.comparisons = 0
    Sorts.swaps = 0
    func(values)
    reversed_comparisons = Number.comparisons

    # Random lists test
    lists = create_randoms()
    total = 0

    for a in lists:
        Number.comparisons = 0
        Sorts.swaps = 0
        func(a)
        total += Number.comparisons

    average = total / TESTS

    # Display results
    print(f"{title}")
    print(f"Sorted:       {sorted_comparisons:>10}")
    print(f"Reversed:     {reversed_comparisons:>10}")
    print(f"Random avg:   {average:>10.2f}")

    return
    
    """
    
    # In-order list
    values = create_sorted()
    Number.comparisons = 0
    Sorts.swaps = 0
    func(values)
    in_order_comp = Number.comparisons
    in_order_swaps = Sorts.swaps

    # Reversed list
    values = create_reversed()
    Number.comparisons = 0
    Sorts.swaps = 0
    func(values)
    reversed_comp = Number.comparisons
    reversed_swaps = Sorts.swaps

    # Random lists (TESTS arrays of length SIZE)
    arrays = create_randoms()
    total_comp = 0
    total_swaps = 0

    for a in arrays:
        Number.comparisons = 0
        Sorts.swaps = 0
        func(a)
        total_comp += Number.comparisons
        total_swaps += Sorts.swaps

    random_comp = total_comp / TESTS
    random_swaps = total_swaps / TESTS

    # Use rounding for swaps to avoid float truncation errors
    in_swaps_int = round(in_order_swaps)
    rev_swaps_int = round(reversed_swaps)

    print(f"{title:13s}"
          f"{in_order_comp:8d}{reversed_comp:8d}{random_comp:11.2f}"
          f"{in_swaps_int:8d}{rev_swaps_int:8d}{random_swaps:11.2f}")

    return




if __name__ == "__main__":
    print(f"n: {SIZE}")
    print(f"{'Algorithm':13s}"
          f"{'In Order':>8}{'Reversed':>8}{'Random':>11}"
          f"{'In Order':>8}{'Reversed':>8}{'Random':>11}")
    print("-" * 80)

    for title, func in SORTS:
        test_sort(title, func)



