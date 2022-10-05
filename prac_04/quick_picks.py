"""
CP1404/CP5632 Practical
Lottery Quick Picks program
Write a program that asks the user how many "quick picks" they wish to generate
Each line consists of 6 random numbers between 1 and 45
Each line (quick pick) should not contain any repeated number
Each line of numbers should be displayed in sorted (ascending) order
Format the numbers, so they align neatly
"""

from random import randrange

START_RANGE = 1
END_RANGE = 46  # Randrange doesn't include final number in range


def main():
    """Lottery quick pick generator program."""
    number_of_quick_picks = get_valid_number("How many quick picks? ")


def get_valid_number(prompt):
    """Check that a valid number is received from user."""
    valid_input = False
    while not valid_input:
        try:
            number = int(input(prompt))
            valid_input = True
        except ValueError:
            print("Please enter a valid number")
    return number


main()
