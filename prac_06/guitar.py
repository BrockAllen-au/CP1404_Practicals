"""
CP1404/CP5632 Practical - Guitar Class.
Expected time to write class: 20mins
Start time: 6:30pm
End time: 6:45pm
"""
CURRENT_YEAR = 2022


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
        return age >= 50
