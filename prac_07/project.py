"""
CP1404 Practical - Project Class.
"""
import datetime


class Project:
    """A class to represent a project."""

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion_percentage=0):
        """Initialise a project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """String representation of a project instance."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, " \
               f"estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"

    def is_complete(self):
        """Tests if the project is 100% complete."""
        return self.completion_percentage == 100

    def __lt__(self, other):
        """Used for sorting projects by priority."""
        return self.priority < other.priority


if __name__ == "__main__":
    test_project = Project("Build Car Park", "12/09/2021", 2, 60000.0, 95)
    test_completed_project = Project("Read 7 Habits Book", "13/12/2021", 6, 99.0, 100)
    "Read 7 Habits Book	13/12/2021	6	99.0	100"
    print(test_project)
    print("Project complete? expect False, returned: ", test_project.is_complete())
    print(test_completed_project)
    print("Project complete? expect True, returned: ", test_completed_project.is_complete())
