import csv
from utils import get_float_input, get_date_input

def update_measurement(measurements):
    print("Update measurement")
    weight = get_float_input("Enter your weight in kilograms: ")
    height = get_float_input("Enter your height in cm: ")
    date = get_date_input("Today's date (dd/mm/yyyy): ")
    with open(measurements, "a", newline='') as open_measurements:
        writer = csv.writer(open_measurements)
        writer.writerow([date, height, weight])
    input("Press Enter to go back to menu...")