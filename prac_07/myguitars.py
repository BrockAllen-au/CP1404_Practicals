"""
CP1404/CP5632 Practical - My Guitars Program - Client Side.
"""
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Main guitar display program."""
    guitars = []
    process_guitars(guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def process_guitars(guitars):
    """Processes guitar information from a csv file."""
    in_file = open(FILENAME, "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)


if __name__ == "__main__":
    main()
