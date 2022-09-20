"""
CP1404/CP5632 - Practical
A program to quickly work out the total price for a number of items, each with different prices.
"""

total_cost = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_cost += price_of_item

if total_cost > 100:
    total_cost *= 0.9  # Apply a 10% discount

print(f"Total price for {number_of_items} items is ${total_cost:.2f}")
