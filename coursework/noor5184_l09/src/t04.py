"""
-------------------------------------------------------
[lab 9, Task 4]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-03-20"
-------------------------------------------------------
"""
# Imports
from functions import validate_code
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

code = input("Enter Code: ")

print("\nValidation: ")
print(validate_code(code))