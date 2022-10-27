"""CP1404/CP5632 Practical - ProgrammingLanguage Class."""


class ProgrammingLanguage:
    """Represent a programming language"""

    def __init__(self, language_name="", typing="", reflection=False, year=0):
        """Initialise a programming language instance."""
        self.language_name = language_name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of ProgrammingLanguage."""
        return f"{self.language_name}, {self.typing} Typing, Reflection={self.reflection}, " \
               f"First appeared in {self.year}"

    def is_dynamic(self):
        """Tests if language typing is dynamic."""
        return self.typing == "Dynamic"
