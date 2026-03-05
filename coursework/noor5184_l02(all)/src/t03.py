"""
-------------------------------------------------------
[Lab 2, Task 3 ]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2024-09-19"
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


LGCOST = 75.00
SMCOST = 50.00

lgDog = int(input("Number of large dogs groomed: \n"))
smDog = int(input("Number of small dogs groomed: \n"))

total = int((LGCOST*lgDog) + (SMCOST*smDog))

print("Total earned for the day: $", total)
