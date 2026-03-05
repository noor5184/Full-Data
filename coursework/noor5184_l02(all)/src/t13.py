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


MIDWEIGHT = 0.35
EXAMWEIGHT = 0.65

midMark = float(input("Midterm mark (%): \n"))
examMark = float(input("Exam mark (%): \n"))

final = (midMark * MIDWEIGHT) + (examMark * EXAMWEIGHT)

print("Final Grade (%): ", final)
