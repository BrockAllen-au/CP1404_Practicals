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
