"""
-------------------------------------------------------
[Assignment 2, Task 4]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2024-09-29"
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


flyer = int(input("Number of flyers:"))
ppl = int(input("Number of delivery people:"))

perPpl = flyer // ppl
left = flyer % ppl

print()
print("Flyers per delivery person:", perPpl)
print("Flyers left over:", left)
