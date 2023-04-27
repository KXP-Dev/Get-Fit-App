from function_1 import update_measurement
from function_2 import view_measurements
from function_3 import calculate_bmi

print ("Welcome to the Get Fit! app")

measurements = "measurements.csv"

try:
    open_measurements = open(measurements, "r")
    open_measurements.close()
    print("Log loaded")
except FileNotFoundError as e:
    open_measurements = open(measurements, "w")
    open_measurements.write("Measurements\n")
    open_measurements.close()
    print("Created new log")

def create_menu():
    print("1. Enter 1 to update your measurements")
    print("2. Enter 2 to view your measurements")
    print("3. Enter 3 to calculate your BMI")
    print("4. Enter 4 to add an excersise")
    print("5. Enter 5 to view excersise history")
    print("6. Enter 6 to exit")
    choice = input("Enter your selection: ")
    return choice

user_choice = ""

while user_choice != "6":
    user_choice = create_menu()

    if (user_choice == "1"):
        update_measurement(measurements)
    elif (user_choice == "2"):
        view_measurements(measurements)
    elif (user_choice == "3"):
        calculate_bmi()
    elif (user_choice == "4"):
        print("Add excersise")
    elif (user_choice == "5"):
        print("View excersise history")
    elif (user_choice == "6"):
        continue
    else:
        print("Invalid Input")
        
print("Thank you for using the Get Fit! app")