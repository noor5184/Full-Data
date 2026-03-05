"""
-------------------------------------------------------
[Lab 3,Task 8]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2024-09-27"
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


dirt = float(input("Enter amount of dirt (m^3):"))
gravel = float(input("Enter amount of gravel (m^3):"))
sand = float(input("Enter amount of sand (m^3):"))

total = sand + gravel + dirt

phrase1 = "Material"
phrase2 = "Cubic Metres"
"""
phrase3 = "Dirt"
phrase4 = "Sand"
phrase5 = "Total"
"""
print()
print(f"{phrase1: >s}       {phrase2: >s}")
print(f"Dirt {dirt: 15.1f}")
print(f"Gravel {gravel: 13.1f}")
print(f"Sand {sand: 15.1f}")
print(f"Total {total: 14.1f}")
