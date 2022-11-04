"""
CP1404 Practical - Project Management Program - Client Side.
Estimated completion time: 2.5 hours
Actual completion time:
"""
import datetime

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n" \
       "- (A)dd new project\n- (U)pdate project\n- (Q)uit"


def main():
    """Project Management Program."""
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            print("Load chosen")  # Printing for troubleshooting
        elif menu_choice == "S":
            print("Save chosen")
        elif menu_choice == "D":
            print("Display chosen")
        elif menu_choice == "F":
            print("Filter chosen")
        elif menu_choice == "A":
            print("Add chosen")
        elif menu_choice == "U":
            print("Update chosen")
        else:
            print("Invalid option")
        print(MENU)
        menu_choice = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


if __name__ == "__main__":
    main()
