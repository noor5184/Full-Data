"""
-------------------------------------------------------
[Lab 3,Task 14]
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


minsInp = int(input("Enter number of minutes: "))

MINSPERDY = 1440
MINSPERHR = 60

days = minsInp // MINSPERDY
mins = minsInp - (MINSPERDY*days)

hours = mins // MINSPERHR
mins = mins - (MINSPERHR*hours)

print(f"There are{days: d} days, {hours: d} hours, and{
      mins: d} minutes in{minsInp: d} minutes")
