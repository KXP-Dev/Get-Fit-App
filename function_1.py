import csv
from utils import get_float_input, get_date_input

def update_measurement(measurements):
    print("Update measurement")
    with open(measurements, "a", newline='') as open_measurements:
        writer = csv.writer(open_measurements)
        weight = get_float_input("Enter your weight in kilograms: ")
        height = get_float_input("Enter your height in cm: ")
        date = get_date_input("Today's date (dd/mm/yyy): ")
        writer.writerow([date, height, weight])
    print("Measurement added successfully")
    input("Press Enter to go back to menu...")