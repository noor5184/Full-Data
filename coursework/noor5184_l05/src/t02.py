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
from functions import gcd

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
    print("Testing Recursive Greatest Common Divisor (GCD) Function")
    print("========================================\n")

    tests = [
        (48, 18),
        (20, 8),
        (17, 13),
        (100, 25),
        (81, 27),
        (42, 56)
    ]

    for m, n in tests:
        print(f"Calculating gcd({m}, {n})...")
        result = gcd(m, n)
        print(f"Result: The GCD of {m} and {n} is {result}\n")

    print("========================================")
    print("All tests completed.")
    print("========================================")

if __name__ == "__main__":
    main()
