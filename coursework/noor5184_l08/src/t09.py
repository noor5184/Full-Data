"""
-------------------------------------------------------
[Lab 8, Task 9]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2024-11-08"
-------------------------------------------------------
"""
# Imports
from functions import many_search
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


values = [94, 96, -22, -79, -28, 96, -50, 71, 24, -32]
value = 96

print("Values: ",values)
print("Search Value: ",value)

print("Occurences: ", many_search(values, value))