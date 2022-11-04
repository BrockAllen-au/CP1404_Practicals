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
    projects.sort()
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            new_project_file = input("Enter file you wish to load: ")
            load_projects(new_project_file, projects)
            projects.sort()
        elif menu_choice == "S":
            new_save_file = input("Enter new save file: ")
            save_projects(new_save_file, projects)
        elif menu_choice == "D":
            print("Display chosen")
            display_projects(projects)
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
    save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def display_projects(projects):
    print("Incomplete projects:")
    for project in projects:
        if not project.is_complete():
            print(f"\t{project}")
    print("Completed projects:")
    for project in projects:
        if project.is_complete():
            print(f"\t{project}")


def load_projects(filename, projects):
    """Loads projects from a file."""
    in_file = open(filename, "r")
    in_file.readline()  # Reads the header line
    for line in in_file:
        # print(repr(line.strip().split("\t")))
        parts = line.strip().split("\t")
        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)


def save_projects(filename, projects):
    """Saves projects to a file."""
    out_file = open(filename, "w")
    # Recreate file headers
    print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
    for project in projects:
        print(project.name, project.start_date, project.priority, project.cost_estimate, project.completion_percentage,
              file=out_file, sep="\t")
    out_file.close()


if __name__ == "__main__":
    main()
