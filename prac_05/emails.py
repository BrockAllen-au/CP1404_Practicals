"""
CP1404/CP5632 Practical
Email and name extractor program
"""


def main():
    """Create a dictionary of emails to names."""
    pass


def extract_name(email):
    """Extract the name from a provided email address."""
    parts = email.split("@")[0].split(".")
    name = (" ".join(parts)).title()
    name_confirmation = input(f"Is your name {name}? (Y/n)")
    if name_confirmation.upper() != "Y" and name_confirmation != "":
        name = input("Name: ").title()
    return name
