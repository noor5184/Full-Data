"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2024-11-08"
-------------------------------------------------------
"""
# Imports
import random
import math
from random import randint

# Constants
MONTHS = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"]

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

def get_month_name(m):
    """
    -------------------------------------------------------
    Returns the name of a month given its number.
    Use: name = get_month_name(m)
    -------------------------------------------------------
    Parameters:
        m - month number (int 1 <= m <= 12)
    Returns:
        name - matching month, 1 = "January", 12 = "December" (str)
    -------------------------------------------------------
    """

    return MONTHS[m - 1]

def get_lotto_numbers(n, low, high):
    """
    -------------------------------------------------------
    Generates a sorted list of unique lottery numbers.
    Requires import: from random import randint
    Use: numbers = get_lotto_numbers(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of lottery numbers to generate (int > 0)
        low - low value of the lottery number range (int >= 0)
        high - high value of the lottery number range (int > low)
    Returns:
        numbers - a list of unique random lottery numbers (list of int)
    -------------------------------------------------------
    """
    
    
    numbers = set() 
    
    while len(numbers) < n:
        numbers.add(random.randint(low, high))
    
    return sorted(numbers)  
    
    
    
    # numbers = sorted(random.sample(range(low, high + 1), n))
    
    #return numbers
    
def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    # Generate a list of 'n' random integers between 'low' and 'high'
    values = [random.randint(low, high) for i in range(n)]
    
    return values


def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """
    negatives = len([x for x in values if x < 0])
    positives = len([x for x in values if x > 0])
    zeroes = len([x for x in values if x == 0])
    evens = len([x for x in values if x % 2 == 0])
    odds = len([x for x in values if x % 2 != 0])

    return negatives, positives, zeroes, evens, odds




def many_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns a list of
    all indexes of its occurrence.
    User: indexes = many_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        indexes - a list of indexes of the location of value in values,
                  [] if not found (list of int).
    -------------------------------------------------------
    """
    indexes = []
    start = 0
    
    # Loop to find all occurrences of 'value' using list.index
    while True:
        try:
            # Find the next occurrence of 'value' starting from 'start'
            index = values.index(value, start)
            indexes.append(index)
            # Move the start position to the next element after the found index
            start = index + 1
        except ValueError:
            # No more occurrences found, exit the loop
            break
    
    return indexes
    


def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sums(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """
    target = []
    for i in range(len(source1)):
        target.append(source1[i] + source2[i])
    
    return target

