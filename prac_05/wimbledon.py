"""
CP1404/CP5632 Practical
Wimbledon winners program
"""


def main():
    """Wimbledon winners and countries program."""
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        winner = get_winners(in_file)
        print(winner)


def get_winners(file):
    """Will retrieve the winner and country from list."""
    wimbledon_winner = {}
    lines = file.readlines()
    for line in lines:
        line = line.strip().split(",")
        wimbledon_winner[line[2]] = line[1]
    return wimbledon_winner


main()
