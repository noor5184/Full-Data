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
from functions import is_palindrome

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
    print("Testing Recursive Palindrome Function")
    print("========================================\n")

    tests = [
        "racecar",
        "A man, a plan, a canal: Panama",
        "No lemon, no melon",
        "Was it a car or a cat I saw?",
        "Recursion",
        "Hello",
        "Madam"
    ]

    for text in tests:
        result = is_palindrome(text)
        verdict = "is" if result else "is NOT"
        print(f"Testing: \"{text}\"")
        print(f"Result: The string {verdict} a palindrome.\n")

    print("========================================")
    print("All tests completed.")
    print("========================================")

if __name__ == "__main__":
    main()
