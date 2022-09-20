"""
CP1404/CP5632 - Practical
Using the general pattern of a menu-driven program
"""

MENU = "(H)ello\n" \
       "(G)oodbye\n" \
       "(Q)uit"

name = input("Enter name: ").title()
print(MENU)
menu_choice = input(">>> ").upper()
while menu_choice != 'Q':
    if menu_choice == 'H':
        print(f"Hello {name}")
    elif menu_choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    menu_choice = input(">>> ").upper()

print("Finished.")
