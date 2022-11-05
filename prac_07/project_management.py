"""
CP1404 Practical - Project Management Program - Client Side.
Estimated completion time: 2.5 hours
Actual completion time:
"""
import datetime
from operator import attrgetter
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
            new_save_file = input("Enter new save file: ")
            save_projects(new_save_file, projects)
        elif menu_choice == "D":
            display_projects_status(projects)
        elif menu_choice == "F":
            filter_date_string = input("Show projects that start after date (dd/mm/yy): ")
            filter_projects(projects, filter_date_string)
        elif menu_choice == "A":
            print("Let's add a new project")
            add_new_project(projects)
        elif menu_choice == "U":
            display_projects(projects)
            update_project(projects)
        else:
            print("Invalid option")
        print(MENU)
        menu_choice = input(">>> ").upper()
    save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def filter_projects(projects, filter_date):
    """Displays projects from a specified date range."""
    filter_date = datetime.datetime.strptime(filter_date, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    filtered_projects.sort(key=attrgetter("start_date"))
    for project in filtered_projects:
        print(project)


def update_project(projects):
    project_choice = get_valid_number("Project choice: ", 0, len(projects) - 1)
    project = projects[project_choice]
    print(project)
    invalid_input = True
    while invalid_input:
        try:
            new_completion = input("New Percentage: ")
            if new_completion == "":
                invalid_input = False
                pass
            else:
                project.completion_percentage = int(new_completion)
                invalid_input = False
        except ValueError:
            print("Invalid input. Enter a whole integer.")
    invalid_input = True
    while invalid_input:
        try:
            new_priority = input("New Priority: ")
            if new_priority == "":
                invalid_input = False
                pass
            else:
                project.priority = int(new_priority)
                invalid_input = False
        except ValueError:
            print("Invalid input. Enter a whole integer.")


def get_valid_number(prompt, low, high):
    """Returns a valid integer from a given range."""
    invalid_input = True
    while invalid_input:
        try:
            number = int(input(prompt))
            while number < low or number > high:
                print(f"Invalid number. Enter a number from {low} - {high}.")
                number = int(input(prompt))
            invalid_input = False
        except ValueError:
            print(f"Invalid input. Please enter a whole number from {low} - {high}.")
    return number


def add_new_project(projects):
    name = input("Name: ")
    date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    new_project = Project(name, date, priority, cost, completion)
    projects.append(new_project)


def display_projects(projects):
    """Displays all projects."""
    for i, project in enumerate(projects):
        print(i, project)


def display_projects_status(projects):
    """Displays all projects ordered priority."""
    print("Incomplete projects:")
    for project in sorted(projects):
        if not project.is_complete():
            print(" ", project)
    print("Completed projects:")
    for project in sorted(projects):
        if project.is_complete():
            print(" ", project)


def load_projects(filename, projects):
    """Loads projects from a file."""
    in_file = open(filename, "r")
    in_file.readline()  # Reads the header line
    for line in in_file:
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
