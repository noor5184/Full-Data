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


SECPERDAY = 86400
SECPERHR = 3600
SECPERMIN = 60
secondsInp = int(input("Number of seconds: "))

days = secondsInp // SECPERDAY
secondsInp = secondsInp - (SECPERDAY*days)

hours = secondsInp // SECPERHR
secondsInp = secondsInp - (SECPERHR*hours)

mins = secondsInp // SECPERMIN
secondsInp = secondsInp - (SECPERMIN*mins)

secs = secondsInp % SECPERMIN

print("Days:", days, "Hours:", hours, "Minutes:", mins, "Seconds:", secs)
