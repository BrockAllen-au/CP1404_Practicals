"""
CP1404/CP5632 Practical - My Guitars Program - Client Side.
"""
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Main guitar display program."""
    guitars = []
    load_guitars(guitars, FILENAME)
    print("My guitars!")
    get_guitars(guitars)
    guitars.sort()
    display_guitars(guitars)
    save_guitars(guitars, FILENAME)


def save_guitars(guitars, filename):
    """Save current list of guitars to csv file."""
    out_file = open(filename, "w")
    for guitar in guitars:
        print(guitar.name, guitar.year, guitar.cost, file=out_file, sep=",")
    out_file.close()


def get_guitars(guitars):
    """Prompts user for new guitars until name is blank."""
    guitar_name = input("Name: ")
    while guitar_name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(guitar_name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar, "added.\n")
        guitar_name = input("Name: ")


def display_guitars(guitars):
    """Displays guitar details."""
    width = max([len(guitar.name) for guitar in guitars])
    for i, guitar in enumerate(guitars, start=1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>{width}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def load_guitars(guitars, filename):
    """Loads guitar information from a csv file."""
    in_file = open(filename, "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)


if __name__ == "__main__":
    main()
