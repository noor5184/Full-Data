"""
-------------------------------------------------------
Tests various linked sorting functions.
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

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

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
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted List of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()

    for i in range(SIZE):
        values.append(Number(i))

    return values



def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()

    for i in range(SIZE - 1, -1, -1):
        values.append(Number(i))

    return values



def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """
    lists = []

    for _ in range(TESTS):
        lst = List()
        for _ in range(SIZE):
            value = random.randint(0, XRANGE)
            lst.append(Number(value))
        lists.append(lst)

    return lists



def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
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

    # Random lists
    lists = create_randoms()
    total_comp = 0
    total_swaps = 0

    for lst in lists:
        Number.comparisons = 0
        Sorts.swaps = 0
        func(lst)
        total_comp += Number.comparisons
        total_swaps += Sorts.swaps

    random_comp = total_comp / TESTS
    random_swaps = total_swaps / TESTS

    # Round swaps to avoid any tiny float issues
    in_swaps_int = round(in_order_swaps)
    rev_swaps_int = round(reversed_swaps)

    print(
        f"{title:13s}"
        f"{in_order_comp:8d}{reversed_comp:8d}{random_comp:11.2f}"
        f"{in_swaps_int:8d}{rev_swaps_int:8d}{random_swaps:11.2f}"
    )

    return


