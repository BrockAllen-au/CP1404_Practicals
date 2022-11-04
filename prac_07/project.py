"""
CP1404 Practical - Project Class.
"""


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
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, " \
               f"completion: {self.completion_percentage}%"


if __name__ == "__main__":
    test_project = Project("Build Car Park", "12/09/2021", 2, 60000.0, 95)
    print(test_project)
