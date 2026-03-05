"""
-------------------------------------------------------
[Assignment 2, Task 5]
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


fL = float(input("Foundation length (m): "))
fW = float(input("Foundation width (m): "))
fH = float(input("Foundation height (m): "))
wH = float(input("Wall height (m): "))
cC = float(input("Cost of concrete ($/m^3): "))
cB = float(input("Cost of bricks ($/m^2): "))

fV = fL * fW * fH
fC = fV * cC

wallSm = (fW * wH)*2
wallBg = (fL * wH)*2
wallTotal = wallSm + wallBg
wallCost = wallTotal*cB

totalCost = fC + wallCost

print()
print(f"Concrete needed for foundation (m^3): {fV: .2f}")
print(f"Cost of concrete: ${fC: .2f}")
print(f"Bricks needed for walls (m^2): {wallTotal: .2f}")
print(f"Cost of bricks: ${wallCost: .2f}")
print(f"Total cost: ${totalCost: .2f}")
