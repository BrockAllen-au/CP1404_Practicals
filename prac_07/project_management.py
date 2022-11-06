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
            load_new_file(projects)
        elif menu_choice == "S":
            new_save_file = input("Enter new save file: ")
            save_projects(new_save_file, projects)
        elif menu_choice == "D":
            display_projects_status(projects)
        elif menu_choice == "F":
            filter_projects(projects)
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


def load_new_file(projects):
    """Gets a new valid file to load."""
    invalid_input = True
    while invalid_input:
        try:
            new_project_file = input("Enter file you wish to load: ")
            load_projects(new_project_file, projects)
            invalid_input = False
        except FileNotFoundError:
            print(f"Unable to find file {new_project_file}")


def filter_projects(projects):
    """Displays projects from a specified date range."""
    filter_date = get_valid_date("Show projects that start after date (dd/mm/yyyy): ")
    filtered_projects = [project for project in projects if project.start_date >= filter_date]
    filtered_projects.sort(key=attrgetter("start_date"))
    for project in filtered_projects:
        print(project)


def get_valid_date(prompt):
    """Gets valid date from user."""
    invalid_input = True
    while invalid_input:
        try:
            filter_date_string = input(prompt)
            date = datetime.datetime.strptime(filter_date_string, "%d/%m/%Y").date()
            invalid_input = False
        except ValueError:
            print("Enter a valid date in format d/m/yyyy")
    return date


def update_project(projects):
    """Update a projects completion and priority."""
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
    """Adds a new project to the list of projects."""
    name = input("Name: ")
    while name == "":
        print("Enter valid name.")
        name = input("Name: ")
    date = get_valid_date("Start date (dd/mm/yyyy): ")
    priority = get_valid_number("Priority: ", 1, 10)
    cost = get_valid_float("Cost estimate: $")
    completion = get_valid_number("Percent complete: ", 0, 100)
    new_project = Project(name, date, priority, cost, completion)
    projects.append(new_project)


def get_valid_float(prompt):
    """Gets a valid float point number."""
    invalid_input = True
    while invalid_input:
        try:
            number = float(input(prompt))
            invalid_input = False
        except ValueError:
            print("Enter valid number.")
    return number


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
        project.start_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
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
