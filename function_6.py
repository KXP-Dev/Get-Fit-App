import csv
from prettytable import PrettyTable

def search_exercises(exercises):
    print("Search Exercises")
    search_term = input("Enter the exercise name to search for: ")
    with open(exercises, "r") as open_exercises:
        reader = csv.reader(open_exercises)
        matching_rows = [row for row in reader if search_term.lower() in row[0].lower()]
        if len(matching_rows) == 0:
            print("No exercises found with that name.")
        else:
            table = PrettyTable()
            table.field_names = ["Exercise Name", "Date", "Sets", "Repetitions"]
            for row in matching_rows:
                table.add_row(row)
            print(table)
    input("Press Enter to go back to menu...")