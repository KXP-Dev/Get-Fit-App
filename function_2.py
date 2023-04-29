import csv
from prettytable import PrettyTable

def view_measurements(measurements):
    print("Viewing measurement history")
    table = PrettyTable(["Date", "Height (cm)", "Weight (kg)"])
    with open(measurements, "r") as open_measurements:
        reader = csv.reader(open_measurements)
        next(reader)
        for row in reader:
            table.add_row(row)
    print(table)
    input("Press Enter to go back to menu...")
    