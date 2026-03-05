"""
-------------------------------------------------------
[lab 9, Task 10]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-03-20"
-------------------------------------------------------
"""
# Imports
from functions import text_analyze
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

txt = input("Enter Phrase:")

print("\nPhrase analysis: (uppr, lowr, dgts, whtspc) ")
print()
print(text_analyze(txt))