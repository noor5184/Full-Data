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
from functions import to_power

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
    print("Testing Recursive Power Function (base ^ power)")
    print("========================================\n")

    tests = [
        (2, 3),
        (5, 0),   
        (3, 1),   
        (2, -2),  
        (-2, 3),
        (-3, 2),
        (10, -1)
    ]

    for base, power in tests:
        print(f"Calculating {base}^{power} ...")
        result = to_power(base, power)
        print(f"Result: {base}^{power} = {result}\n")

    print("========================================")
    print("All tests completed.")
    print("========================================")

if __name__ == "__main__":
    main()
