"""
-------------------------------------------------------
[Assignment 6, Task 3]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2024-11-03"
-------------------------------------------------------
"""
# Imports
from functions import interest_table
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


princ = float(input("Principal: "))
intr = float(input("Interest: "))
mnthly = float(input("Monthly Payment:"))


print()
interest_table(princ, intr, mnthly)
