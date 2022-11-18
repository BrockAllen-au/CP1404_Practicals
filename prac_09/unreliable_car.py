"""
CP1404/CP5632 Practical
Unreliable Car class
"""
from car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that has a chance to not drive."""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return f"{super().__str__()}, reliability: {self.reliability}"

