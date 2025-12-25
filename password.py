"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Steven Dinh
File created: October 11, 2024
******************************
This file contains two functions that evaluate the input (password)
and returns a numerical value representing the strength.
The function 'count_groups' checks four conditions against the input,
and outputs a value based on the character types present.
The 'password_strength' function utilizes the helper function 'count_groups' to
determine the strength of the password, using the groups present and the length of the password.
"""

def count_groups(pwd):
    # CONSTANTS
    LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"
    UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    DIGITS = "0123456789"
    SYMBOLS = "!@#$%^&*/?-+=,.|~"

    # conditions to check in password
    has_lowercase = has_uppercase = has_digit = has_symbol = False

    # cycle through the password, and check if that character is in the constants
    # then equate them to true if they are present
    for char in pwd:
        if char in LOWERCASE_LETTERS:
            has_lowercase = True
        elif char in UPPERCASE_LETTERS:
            has_uppercase = True
        elif char in DIGITS:
            has_digit = True
        elif char in SYMBOLS:
            has_symbol = True
    # True = 1, and False = 0
    # returns all the values added up to show how many groups are present
    return has_lowercase + has_uppercase + has_digit + has_symbol

def password_strength(pwd):
    # Looks for whitespace, indent, and newline characters are in the password
    # If it is found that there is one, immediately return 0
    for char in pwd:
        if char in [' ','\t','\n']:
            return 0
    #Variable
    groups = count_groups(pwd)
    # The length of the password has different conditions depending on its length
    # The shorter it is, the lower the strength is
    # and uses the groups present to evaluate the strength
    if len(pwd) < 5:
        return 0
    # Length between 5-8
    elif 5 <= len(pwd) <= 8:
        if groups == 1:
            return 1
        elif 2 <= groups <= 3:
            return 2
        elif groups == 4:
            return 3
    # Length between 9-12
    elif 9 <= len(pwd) <= 12:
        if groups == 1:
            return 2
        elif 2 <= groups <= 3:
            return 3
        elif groups == 4:
            return 4
    # Length greater than 12
    elif len(pwd) > 12:
        if groups == 1:
            return 3
        elif 2 <= groups <= 3:
            return 4
        elif groups == 4:
            return 5
    
    return 0 # default return value

