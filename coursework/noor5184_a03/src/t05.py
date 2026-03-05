"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-09-27"
-------------------------------------------------------
"""
# Imports
from functions import postfix
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




tests = [
    "12 5 -",                
    "4 5 + 12 * 2 3 * -",     
    "5 1 2 + 4 * + 3 -"       
]

for expr in tests:
    print(expr, "=", postfix(expr))
