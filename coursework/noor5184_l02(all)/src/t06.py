"""
-------------------------------------------------------
[Lab 2, Task 6]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2024-09-20"
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


MNTHSINYR = 12
princ = int(input("Mortgage principal ($): \n"))
time = int(input("Number of years: \n"))
intrest = int(input("Yearly interest rate (%): \n"))


time = time*MNTHSINYR
intrest = intrest / MNTHSINYR


mnthlyPymt = (princ * (intrest*((1+intrest)**time))) / \
    (((1 + intrest)**time) - 1)

print("The monthly payments are: $ ", mnthlyPymt)
