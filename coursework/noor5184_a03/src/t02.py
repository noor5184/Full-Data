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
for v in [5, 7, 8, 9, 12, 14, 8][::-1]:
    s._values.append(v)  


t1, t2 = s.split_alt()

def show_stack(st):
   
    return list(reversed(st._values))

print("target1:", show_stack(t1))
print("target2:", show_stack(t2))
print("source (should be empty):", show_stack(s))
