# Password Strength Checker & Generator

This project is a Python-based utility to evaluate the strength of passwords and generate strong, random passwords. It was developed as part of CS 1026 - Assignment 2.

## Features

- **Password Strength Evaluation**: Analyzes passwords based on length and variety of character types (lowercase, uppercase, digits, and symbols).
- **Random Password Generation**: Generates a secure random password of a fixed length (15 characters) upon request.
- **Minimum Requirement Check**: Ensures that a user-provided or generated password meets a specified minimum strength threshold.

## File Structure

- `driver.py`: The main entry point of the application. It prompts the user for a minimum strength requirement and initiates the password processing.
- `login.py`: Manages the user interaction for password input. It allows users to either type their own password or generate one.
- `password.py`: Contains the core logic for calculating password strength. It uses a scoring system based on character groups and password length.
- `generate.py`: Provides the functionality to generate a random password using a wide range of characters.

## Strength Scoring System

The strength of a password is rated on a scale of 0 to 5:
- **0**: Very weak (e.g., length < 5 or contains whitespace).
- **1-5**: Increasing levels of strength based on length and the number of character groups used (lowercase, uppercase, digits, symbols).

## How to Use

1. Run the `driver.py` script:
   ```bash
   python driver.py
   ```
2. Enter the minimum strength you want for your password (e.g., 3).
3. Follow the prompt to either:
   - Type in a password you want to check.
   - Type `X` to have the system generate a strong password for you.
4. The system will provide feedback on whether the password meets the minimum requirement.

## Author

- **Steven Dinh**
- Created: October 11, 2024
