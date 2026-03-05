"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2024-09-19"
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


food = float(input("Food Charge: $"))
tax = float(input("Sales Tax in (%): "))
tip = float(input("Tip in (%): "))

tax = tax / 100
tip = tip/100

taxChrg = food * tax
tipChrg = food * tip

total = food + taxChrg + tipChrg

print("\nCost of meal:")
print("Subtotal: ", food)
print("Tax: ", taxChrg)
print("Tip: ", tipChrg)
print("\n----------------------------\n")
print("Total: $", total)
