"""
CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class.
Estimated completion time: 20mins
Start Time: 6:00pm
End Time: 6:21pm
"""
from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages = [
    ProgrammingLanguage("Python", "Dynamic", True, 1991),
    ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
    ProgrammingLanguage("Visual Basic", "Static", False, 1991),
]

print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.language_name)
