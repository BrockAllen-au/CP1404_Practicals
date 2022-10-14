"""
CP1404/CP5632 Practical
Hex colour code program
"""

COLOUR_TO_CODE = {"AbsoluteZero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                  "Alizarin Crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                  "AntiqueWhite": "#faebd7", "Apricot": "#fbceb1", "Aqua": "#00ffff"}

colour_name = input("Enter colour name: ")
while colour_name != "":
    try:
        print(colour_name, "has colour code: ", code[colour_name])
    except KeyError:
        print("Invalid colour entered.")
    colour_name = input("Enter colour name: ")
