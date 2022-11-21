"""Test file for testing the silver service taxi class"""
from silver_service_taxi import SilverServiceTaxi

# Test output of Hummer taxi, fanciness of 4
hummer = SilverServiceTaxi("Hummer", 200, 4)
print(hummer)
print()

# Test output for 18km trip with fanciness of 2
silver_taxi = SilverServiceTaxi("Silver Taxi", 100, 2)
print(silver_taxi)
silver_taxi.drive(18)
print(silver_taxi)
print("18km trip will cost: $", silver_taxi.get_fare())
