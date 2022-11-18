"""
CP1404/CP5632 Practical
Unreliable Car class
"""
import random
from car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that has a chance to not drive."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return f"{super().__str__()}, reliability: {self.reliability}"

    def drive(self, distance):
        """Drive only if distance provided is less than the reliability provided."""
        reliability_test = random.randint(0, 100)
        if reliability_test > self.reliability:
            distance = 0
        elif distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance
