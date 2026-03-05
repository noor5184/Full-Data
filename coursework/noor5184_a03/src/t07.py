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
from functions import reroute
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




cars = [1, 2, 3, 4]

print("SSXSSXXX :", reroute("SSXSSXXX", cars)) 
print("SSXX     :", reroute("SSXX", cars))     
print("SXSXSX   :", reroute("SXSXSX", [10,20,30])) 
print("XXXX     :", reroute("XXXX", cars)) 
print("SSSSXXXX :", reroute("SSSSXXXX", cars)) 
print("bad char :", reroute("SSQX", cars))    
