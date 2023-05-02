import csv
from prettytable import PrettyTable

def search_measurements(measurements):
    print("Search Measurements")
    search_term = input("Enter the date of measurement: ")
    with open(measurements, "r") as open_measurements:
        reader = csv.reader(open_measurements)
        matching_rows = [row for row in reader if search_term.lower() in row [0].lower()]
        if len(matching_rows) == 0:
            print("No measurements found with that date.")
        else:
            table = PrettyTable()
            table.field_names = ["Date", "Weight", "Height"]
            for row in matching_rows:
                table.add_row(row)
            print(table)
    input("Press Enter to go back to menu...")