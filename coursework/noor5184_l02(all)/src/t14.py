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


MILK = 4.0/6.0
BUTTER = 8.0 / 6.0
FLOUR = 0.5 / 6.0
SALT = 2.0/6.0

servings = int(input("Enter servings of Mac & Cheese: "))

MILK = MILK*servings
BUTTER = BUTTER*servings
FLOUR = FLOUR*servings
SALT = SALT * servings

print(servings, " servings of Mac & Cheese requires:")
print("milk (cups): ", MILK)
print("butter (tablespoons): ", BUTTER)
print("flour (cups): ", FLOUR)
print("salt (teaspoons): ", SALT)
