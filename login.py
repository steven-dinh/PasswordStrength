"""
******************************
CS 1026 - Assignment 2 – Password Strength
Code by: Steven Dinh
File created: October 11, 2024
******************************
This file prompts the user for an input to generate a password or check the strength of their own password.
It imports the 'password_strength' function from password.py and the function 'generate_password' from generate.py.
The 'process_password' function prompts the user to input a strength level,
and for a password or to generate a password
then, checks it's strength and provides feedback whether it meets the minimum strength requirement.
"""
# IMPORT FUNCTIONS
from password import password_strength
from generate import generate_password

def process_password(min_strength):
    # while loop to continue loop until password meets the strength requirement
    while True:
        user_input = input("Type in a new password or type X for a randomly generated password: ")
        # makes sure that the input will equal x by removing whitespace and making it lowercase
        if user_input.strip().lower() == "x":
            random_password = generate_password(15) #generate the password, of 15 length
            random_strength = password_strength(random_password) # calculate the strength from the password
            print(f"Generated password: {random_password}")
            print(f"Strength: {random_strength}")
            break
        #if user does not generate, it will take the input and calculate the strength
        strength = password_strength(user_input)
        #if strength meets the minimum strength requirements, exit loop
        if strength >= min_strength:
            print(f"You entered {user_input}")
            print(f"Your password strength has a strength of {strength}")
            print("Your password is strong enough! Thank you.")
            break
        # If the strength does not meet the minimum strength, gives feedback
        # then restarts loop
        else:
            print(f"You entered {user_input}")
            print(f"Your password strength has a strength of {strength}")
            print("Your password is not strong enough. Please create a new password that is stronger.")
