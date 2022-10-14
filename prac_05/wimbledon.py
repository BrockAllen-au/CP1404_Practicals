"""
CP1404/CP5632 Practical
Wimbledon winners program
"""
FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
WINNER_INDEX = 2


def main():
    """Wimbledon winners and countries program."""
    records = get_records(FILENAME)
    print(records)


def get_records(file):
    """Will retrieve the records from file."""
    records = []
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Removes the header
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()
