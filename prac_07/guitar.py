"""
CP1404/CP5632 Practical - Guitar Class.
"""
CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """A Class to represent a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """String representation of Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, year=CURRENT_YEAR):
        """Returns how old the guitar is based on the year passed through."""
        return year - self.year

    def is_vintage(self, year=CURRENT_YEAR):
        """Tests if guitar is of vintage age."""
        age = self.get_age(year)
        return age >= VINTAGE_AGE

    def __lt__(self, other):
        """Used for sorting Guitars by release year."""
        return self.year < other.year
