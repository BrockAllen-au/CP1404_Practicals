"""
CP1404 Practical - Project Management Program - Client Side.
Estimated completion time: 2.5 hours
Actual completion time:
"""
import datetime
from project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n" \
       "- (A)dd new project\n- (U)pdate project\n- (Q)uit"
FILENAME = "projects.txt"


def main():
    """Project Management Program."""
    projects = []
    load_projects(FILENAME, projects)
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            new_project_file = input("Enter file you wish to load: ")
            load_projects(new_project_file, projects)
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


def load_projects(filename, projects):
    """Loads projects from a file."""
    in_file = open(filename, "r")
    in_file.readline()  # Reads the header line
    for line in in_file:
        # print(repr(line.strip().split("\t")))
        parts = line.strip().split("\t")
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)



if __name__ == "__main__":
    main()
