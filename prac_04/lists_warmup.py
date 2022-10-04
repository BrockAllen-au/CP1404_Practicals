"""
CP1404/CP5632 - Practical_04
Without running the code, write down your answers to these questions
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]
print(f"numbers[0]:\n{numbers[0]}")  # Result 3

# numbers[-1]
print(f"numbers[-1]:\n{numbers[-1]}")  # Result 2

# numbers[3]
print(f"numbers[3]:\n{numbers[3]}")  # Result 1

# numbers[:-1]
print(f"numbers[:-1]:\n{numbers[:-1]}")
# Result - the list of all numbers except the last index (2)
# [3, 1, 4, 1, 5, 9]

# numbers[3:4]
print(f"numbers[3:4]:\n{numbers[3:4]}")
# Result - the list with only the third index (1)
# [1]

# 5 in numbers
print(f"5 in numbers:\n{5 in numbers}")
# Result - True

# 7 in numbers
print(f"7 in numbers:\n{7 in numbers}")
# Result - False

# "3" in numbers
print(f'"3" in numbers:\n{"3" in numbers}')
# Result - False

# numbers + [6, 5, 3]
print(f'numbers + [6, 5, 3]:\n{numbers + [6, 5, 3]}')
# Result - numbers list will have 6, 5, 3 on the end of the list

print(f"\nInitial numbers list:\n{numbers}")

# Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
print(f"1. {numbers}")

# Change the last element of numbers to 1
numbers[-1] = 1
print(f"2. {numbers}")

# Get all the elements from numbers except the first two (slice)
# numbers[2:]
print(f"3. {numbers[2:]}")

# Check if 9 is an element of numbers
# 9 in numbers
print(f"4. Is 9 in numbers? {9 in numbers}")
