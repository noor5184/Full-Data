"""
-------------------------------------------------------
[Assignment 1, Task 5]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2024-09-22"
-------------------------------------------------------
"""
# Imports

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


princ = float(input("Principal:\n"))
intr = float(input("Interest (%):\n"))
yr = int(input("Number of years:\n"))
com = int(input("Number of times interest compounded per year:\n"))

intr = intr/100

total = princ*(1+(intr/com))**(com*yr)

print("\nBalance: $", total)
