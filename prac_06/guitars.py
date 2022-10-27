"""
CP1404/CP5632 Practical - Guitar Client code.
Expected time to write class: 25mins
Start time: 8:10pm
End time: 8:42
"""
from guitar import Guitar


def main():
    """My Guitars program"""
    guitars = []
    print("My guitars!")
    guitar_name = input("Name: ")
    while guitar_name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(guitar_name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar, "added.\n")
        guitar_name = input("Name: ")
    width = max([len(guitar.name) for guitar in guitars])
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, start=1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>{width}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()
