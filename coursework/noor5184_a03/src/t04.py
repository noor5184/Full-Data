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
    s._values.append(v)

print("before (top→bottom):", list(reversed(s._values)))
s.reverse()
print("after  (top→bottom):", list(reversed(s._values)))
