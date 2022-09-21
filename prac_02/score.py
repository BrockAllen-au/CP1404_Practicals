"""
CP1404/CP5632 - Practical_02 Score program refactoring
"""
import random


def main():
    """Score results calculator program"""
    score = float(input("Enter score: "))
    result = calculate_result(score)
    print(f"Result: {result}")
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    result = calculate_result(random_score)
    print(f"Result: {result}")


def calculate_result(score):
    """Calculate the result based on the score provided"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
