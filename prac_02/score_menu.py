"""
CP1404/ - Practical_02 Score with menu program
"""
from score import calculate_result

MENU = "(G)et score\n(D)isplay result\n(P)rint stars\n(Q)uit"


def main():
    """Score results program with menu"""
    score = 0
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "D":
            result = calculate_result(score)
            print(f"Result: {result}")
        elif choice == "P":
            print_characters(int(score))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>>").upper()


def get_valid_score():
    """Validate an entered score"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def print_characters(length, character='*'):
    """Print a line of characters for length n"""
    print(length * character)


if __name__ == '__main__':
    main()
