"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Steven Dinh
File created: October 11, 2024
******************************
This file generates a password using the random module that chooses a character randomly from the
variable ALL_CHARS.
The function 'generate_password' takes an integer 'length' as an input and returns a
generated password of the specified length.
"""
import random

def generate_password(length):
    # CONSTANT
    ALL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*/?-+=,.|~"
    # Variable
    password = ""
    # In the given length, it will append random characters from the ALL_CHARS constant
    # into the empty password string, and make a password with the same amount of characters as given from length
    for i in range(length):
        password += random.choice(ALL_CHARS)
    return password
