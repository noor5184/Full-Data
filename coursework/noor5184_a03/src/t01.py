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
from functions import stack_split_alt

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
    s.push(v)

t1, t2 = stack_split_alt(s)

def drain_to_list(st):
    out = []
    while not st.is_empty():
        out.append(st.pop())
    out.reverse()
    return out

print("target1 top→bottom:", drain_to_list(t1))
print("target2 top→bottom:", drain_to_list(t2))