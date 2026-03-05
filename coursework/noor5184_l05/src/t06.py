"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-10-10"
-------------------------------------------------------
"""
# Imports
from functions import bag_to_set

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
    print("========================================")
    print("Testing Recursive Bag to Set Function")
    print("========================================\n")

    tests = [
        [4, 5, 3, 4, 5, 2, 2, 4],
        [1, 2, 3, 3, 2, 1],
        ["a", "b", "a", "c", "b", "d"],
        [],
        [10, 10, 10],
        [7, 8, 9]
    ]

    for bag in tests:
        print(f"Original list: {bag}")
        result = bag_to_set(bag)
        print(f"New list (unique values, order preserved): {result}\n")

    print("========================================")
    print("All tests completed.")
    print("========================================")

if __name__ == "__main__":
    main()

