"""
CP1404/CP5632 - Practical_03
In your console, type in the following (run each print line multiple times),
and write the answers to the questions below in comments
import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
"""
# What did you see on line 1?
# After multiple times run, the following numbers were observed:
# 10, 8, 10, 9, 15, 7, 19
# What was the smallest number you could have seen? What was the largest?
# 5 & 20

# What did you see on line 2?
# After multiple times run, the following numbers were observed:
# 9, 9, 3, 5, 3, 3, 5
# What was the smallest number you could have seen? What was the largest?
# 3 & 9
# Could line 2 have produced a 4?
# No, as the start range is 3 and increments in 2's

# What did you see on line 3?
# After multiple times run, the following numbers were observed:
# 3.148966946615765, 4.53941486430838, 3.4748171038248583, 4.0584761505813916
# What was the smallest number you could have seen? What was the largest?
# 2.50000000000 & 5.50000000000

from random import randrange

print(f"Random number: {randrange(1, 101)}")
