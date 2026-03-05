"""
-------------------------------------------------------
[Assignment 2, Task 3]
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


dateInp = int(input("Enter a date in the format YYYYMMDD: "))

yr = dateInp // 10000
mo = (dateInp % 10000) // 100
da = dateInp % 100
print()
print(f"The reformatted date: {yr}/{mo}/{da}")
