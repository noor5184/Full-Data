"""
-------------------------------------------------------
[Assignment 2, Task 2]
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


numInp = int(input("Enter a positive digit number:"))

numleft = numInp // 10
numRight = numInp % 10

diff = numleft - numRight
print()
print(f"The difference of the digits of{numInp: d} is {diff: d}")
