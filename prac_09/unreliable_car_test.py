"""Test file for testing the unreliable_car class"""

from unreliable_car import UnreliableCar

old_trusty = UnreliableCar("Old Trusty", 100, 50)
print(old_trusty)

old_trusty.drive(60)

print(old_trusty)
