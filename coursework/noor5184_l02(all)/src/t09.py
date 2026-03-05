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


PI = 3.14

"""2πrh+2πr^2"""

diam = float(input("Diameter of container base (cm): "))
height = float(input("Height of container (cm): "))
costMtr = float(input("Cost of material ($/cm^2): "))
numCon = int(input("Number of containers: "))

rad = diam / 2.0

saC = PI*(rad**2)
sa1 = (2 * PI * rad * height) + (2 * PI * (rad**2))
saF1 = sa1 - saC
cost1 = saF1 * costMtr
cost2 = cost1 * numCon

print("\nThe total cost of one containers is $", cost1)
print("The total cost of all containers is $", cost2)
