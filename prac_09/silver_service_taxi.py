"""
CP1404/CP5632 Practical
Silver Service Taxi class
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that has a specialised fare cost."""

    def __init__(self, name, fuel, fanciness: float):
        """Initialise an instance of a Silver Service Taxi."""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness
        self.flagfall = 4.5

    def __str__(self):
        """String representation of Silver Service Taxi and fare."""
        return f"{super().__str__()}"
