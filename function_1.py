import csv
from utils import get_float_input, get_date_input
# I've applied dry coding principles by importing re-used input functions which also handles input errors.

# This function allows the user to input their measurements into the CSV file.
def update_measurement(measurements):
    print("Update measurement")
    try:
        with open(measurements, "a", newline='') as open_measurements:
            writer = csv.writer(open_measurements)
            weight = get_float_input("Enter your weight in kilograms: ")
            height = get_float_input("Enter your height in cm: ")
            date = get_date_input("Today's date (dd/mm/yyyy): ")
            formatted_date = date.strftime("%d/%m/%Y")
            writer.writerow([formatted_date, height, weight])
        print("Measurement added successfully")
    except Exception as e:
        print(f"Something went wrong: {e}")
    input("Press Enter to go back to menu...")
    
# I used newline= for the purposes of making the CSV more readable and to also solve some problems when viewing/printing the CSV to the terminal.

# I have used formatted_date to change how the CSV stores the date input from the user. This also fixed problems with printing and searching the CSV files by date.