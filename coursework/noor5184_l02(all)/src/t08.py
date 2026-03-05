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


height = float(input("Enter your height (m): "))
weight = float(input("Enter your weight (kg): "))
upperLim = int(input(
    "Enter your upper limit BMI (23 if you are from South East Asia and Southern China, 25 for everyone else): "))

bmi = weight / (height ** 2)
bmiPrime = bmi / upperLim

print("Body Mass Index (kg/m^2) = ", bmi)
print("BMI Prime = ", bmiPrime)
