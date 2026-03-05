"""
-------------------------------------------------------
[Lab 2, Task 7 ]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2024-09-20"
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


flyers = int(input("Number of flyers: "))
volun = int(input("Number of volunteers: "))

flyPer = flyers // volun
flyLeft = flyers % volun

print("Flyers per volunteer: ", flyPer)
print("Flyers left over: ", flyLeft)
