"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2024-11-03"
-------------------------------------------------------
"""
# Imports
import math
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


def total_wins():
    """
    -------------------------------------------------------
    Asks the user to enter the winning team names one by one, representing 
    the outcome of a series of games. The user should enter an empty string 
    to signal the end of the series. After all strings have been entered, 
    the function returns the counts of "purple" and "gold" wins.
    Use: result = total_wins()
    -------------------------------------------------------
    Parameters:
        None
    Returns:
        purple_count - count of "purple" wins (int)
        gold_count - count of "gold" wins (int)
    -------------------------------------------------------
    """
    purple_count = 0
    gold_count = 0

    while True:
        team = input("Enter the winning team: ").strip().lower()
        if team == "":
            break
        elif team == "purple":
            purple_count += 1
        elif team == "gold":
            gold_count += 1

    return purple_count, gold_count


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    -------------------------------------------------------
    """
    result = True

    if number <= 1:
        result = False
    elif number > 3:
        divisor = 2
        while divisor * divisor <= number:
            if number % divisor == 0:
                result = False
                break
            divisor += 1

    return result


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    -------------------------------------------------------
    """

    print(f"Principal: ${principal_amount: .2f}")
    print(f"Interest Rate: {interest_rate: .2f}%")
    print(f"Monthly Payment: ${payment: .2f}")
    print("-" * 40)
    print(f"{'Month': <10}{'Interest': <10}{'Payment': <10}{'Balance': <10}")
    print("-" * 40)


    month = 1
    balance = principal_amount
    monthly_rate = interest_rate / 100 / 12


    while balance > 0:

        interest = balance * monthly_rate

        if payment > balance + interest:
            payment = balance + interest
        # Update balance
        balance = balance + interest - payment

        print(f"{month: <10}{interest: .2f}     {payment: .2f}     {balance: .2f}")
        
        month += 1
        
    return


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    -------------------------------------------------------
    """
    count = 0
    number = abs(number)  

    while number > 0:
        number //= 10
        count += 1


    return count if count > 0 else 1

def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    -------------------------------------------------------
    """
    total = 0
    divisor = 1

    # Use a while loop to find factors and sum them
    while divisor < number:
        if number % divisor == 0:
            total += divisor
        divisor += 1

    return total