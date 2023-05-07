import csv
from prettytable import PrettyTable


def view_exercises(exercises):
    print("Viewing exercise history")
    table = PrettyTable(["Exercise", "Date", "Sets", "Repetitions"])
    try:
        with open(exercises, "r") as open_exercises:
            reader = csv.reader(open_exercises)
            next(reader)
            for row in reader:
                table.add_row(row)
        print(table)
    except FileNotFoundError:
        print(f"{exercises} file not found.")
        input("Press Enter to confirm continue from error...")
    input("Press Enter to go back to menu...")
