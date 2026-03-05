"""
-------------------------------------------------------
[Assignment 2, Task 1]
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


TAX = 0.185

sales = float(input("Enter the total sales: $"))

total = sales*TAX

print()
print("Projected Tax Report")
print("--------------------------")
print("Total sales:   $", sales)
print("Annual tax:    %", TAX*100)
print("--------------------------")
print("Tax:           $", total)
