"""
-------------------------------------------------------
[lab 9, Functions]
-------------------------------------------------------
Author:  Ali Noormohammadi
ID:  169105184
Email: Noor5184@mylaurier.ca
__updated__ = "2025-03-20"
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

def url_categorize(url):
    """
    -------------------------------------------------------
    Returns whether a URL represents a business, a non-profit,
    or another type of organization.
    Use: url_type = url_categorize(url)
    -------------------------------------------------------
    Parameters:
        url - the web address of the organization (str)
    Returns:
        url_type - the organization type (str):
            'business' if url ends with 'com'
            'non-profit' if url ends with 'org'
            'other' if url ends with something else
    -------------------------------------------------------
    """
    if url.endswith('.com'):
        phrase = 'business'
    elif url.endswith('.org'):
        phrase = 'non-profit'
    else:
        phrase = 'other'
    
    return phrase


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
    The first three letters describe the product category
    The next four digits are the product ID
    The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    pc = product_code[:3]  
    pi = product_code[3:7] 
    pq = product_code[7:]   
    
    return pc, pi, pq


def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and checks whether the various parts are valid.
    A product code has three parts:
    The first three letters describe the product category and must all be in upper case.
    The next four digits are the product ID.
    The remaining characters describe the product's qualifiers, such as colour, size, etc.,
    and always begin with an uppercase letter.
    Use: category, digits, qualifiers = validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        category - True if three upper-case characters, False otherwise (bool)
        digits - True if four digits, False otherwise (bool)
        qualifiers - True if starts with 1 upper-case letter, False otherwise (bool)
    -------------------------------------------------------
    """
    
    category = len(product_code) >= 3 and product_code[:3].isupper() and product_code[:3].isalpha()
    
    digits = len(product_code) >= 7 and product_code[3:7].isdigit()

    
    qualifiers = len(product_code) > 7 and product_code[7:8].isupper()

    return category, digits, qualifiers


def is_palindrome(s):
    """
    -------------------------------------------------------
    Checks whether the given string is a palindrome or not.
    A palindrome is a string that reads the same forwards as backwards.
    Case is ignored.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string to be checked (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    
    s = s.lower()
    
    return s == s[::-1]


def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    -------------------------------------------------------
    """
    uppr = sum(1 for char in txt if char.isupper())  
    lowr = sum(1 for char in txt if char.islower())  
    dgts = sum(1 for char in txt if char.isdigit())  
    whtspc = sum(1 for char in txt if char.isspace())  
    
    return uppr, lowr, dgts, whtspc
    
