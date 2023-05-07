import csv
from prettytable import PrettyTable
from utils import get_date_input

def search_measurements(measurements):
    print("Search Measurements")
    search_term = get_date_input("Enter the date of measurement (dd/mm/yyyy): ")
    try:
        with open(measurements, "r") as open_measurements:
            reader = csv.reader(open_measurements)
            matching_rows = [row for row in reader if search_term.strftime("%d/%m/%Y") == row[0]]
            if len(matching_rows) == 0:
                print(f"No measurements found with date {search_term.strftime('%d/%m/%Y')}.")
            else:
                table = PrettyTable()
                table.field_names = ["Date", "Height (cm)", "Weight (kg)"]
                for row in matching_rows:
                    table.add_row([row[0], row[1], row[2]])
                print(table)
    except Exception as e:
        print(f"Something went wrong: {e}")
        input("Press Enter to confirm continue from error...")
    input("Press Enter to go back to menu...")