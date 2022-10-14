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
    countries, winner_to_count = process_records(records)
    display_records(countries, winner_to_count)


def display_records(countries, winner_to_count):
    """Displays winners and countries."""
    print("Wimbledon Champions:")
    for name, count in winner_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


def process_records(records):
    """Creates a dictionary of champions and a set of countries."""
    countries = set()
    winner_to_count = {}
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            winner_to_count[record[WINNER_INDEX]] += 1
        except KeyError:
            winner_to_count[record[WINNER_INDEX]] = 1
    return countries, winner_to_count


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
