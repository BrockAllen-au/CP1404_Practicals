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
NUMBERS_TO_GENERATE = 6  # How many numbers to pick on each line


def main():
    """Lottery quick pick generator program."""
    number_of_quick_picks = get_valid_number("How many quick picks? ")
    generate_quick_picks(number_of_quick_picks)


def generate_quick_picks(number_of_quick_picks):
    """Generate n number of lottery quick picks"""
    for i in range(number_of_quick_picks):
        picks = []
        for j in range(NUMBERS_TO_GENERATE):
            number = randrange(START_RANGE, END_RANGE)
            while number in picks:
                # If number already in list, generate a new one
                number = randrange(START_RANGE, END_RANGE)
            picks.append(number)
        picks.sort()
        for number in picks:
            print(f"{number:2}", end=" ")
        print()


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
