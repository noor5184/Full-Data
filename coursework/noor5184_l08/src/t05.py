"""
-------------------------------------------------------
[Lab 8, Task 5]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2024-11-08"
-------------------------------------------------------
"""
# Imports
from functions import get_lotto_numbers
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

n = int(input("Number of lottery numbers to generate: "))
low = int(input("low value of the lottery number range: "))
high = int(input("High value of the lottery number range: "))


print(get_lotto_numbers(n,low,high))