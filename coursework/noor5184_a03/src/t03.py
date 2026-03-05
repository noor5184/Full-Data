"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-09-27"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import stack_reverse
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




s = Stack()
for v in [1, 2, 3, 4, 5]:
    s.push(v)

print("Before reverse (top→bottom):", list(reversed(s._values)))

stack_reverse(s)

print("After reverse (top→bottom):", list(reversed(s._values)))
