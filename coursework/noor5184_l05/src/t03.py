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
from functions import vowel_count

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
    print("Testing Recursive Vowel Count Function")
    print("========================================\n")

    tests = [
        "Recursion",
        "AEIOU",
        "Python",
        "sky",
        "beautiful day",
        "WLU Computer Science"
    ]

    for text in tests:
        print(f"Analyzing: '{text}'")
        count = vowel_count(text)
        print(f"Result: The string '{text}' contains {count} vowel(s).\n")

    print("========================================")
    print("All tests completed.")
    print("========================================")

if __name__ == "__main__":
    main()
