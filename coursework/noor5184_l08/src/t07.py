"""
-------------------------------------------------------
[Lab 8, Task 7]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2024-11-08"
-------------------------------------------------------
"""
# Imports
from functions import generate_integer_list
from functions import list_categorize
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
print("Make a List: ")
print("--------------")
n = int(input("Number of values to generate: "))
low = int(input("Low value range: "))
high = int(input("High value range: "))\

values = generate_integer_list(n,low,high)

print("\nList details: ")
print("----------------")
print("negatives, positives, zeroes, evens, odds")
print(list_categorize(values))