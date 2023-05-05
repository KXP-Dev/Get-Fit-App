from function_1 import update_measurement
from function_2 import view_measurements
from function_3 import calculate_bmi
from function_4 import add_exercise
from function_5 import view_exercises
from function_6 import search_exercises
from function_7 import search_measurements

print ("Welcome to the Get Fit! app")

measurements = "measurements.csv"
exercises = "exercises.csv"
bmi = "bmi.csv"

# This will try to open CSV files. If they exist it will close. If they don't exist they will be created.
try:
    open_measurements = open(measurements, "r")
    open_measurements.close()
    print("Log loaded")
except FileNotFoundError as e:
    open_measurements = open(measurements, "w")
    open_measurements.write("Measurements\n")
    open_measurements.close()
    print("Created new log")
    
try:
    open_exercises = open(exercises, "r")
    open_exercises.close()
    print("Excersises loaded")
except FileNotFoundError as e:
    open_exercises = open(exercises, "w")
    open_exercises.write("Exercises\n")
    open_exercises.close()
    print("Created exercise log")
    
try:
    open_bmi = open(bmi, "r")
    open_bmi.close()
    print("BMI history loaded")
except FileNotFoundError as e:
    open_bmi = open(bmi, "w")
    open_bmi.write("BMI\n")
    open_bmi.close()
    print("BMI log created")

# This code shows what will visually appear in the terminal and will ask for user input choice and return the selection.
def main_menu():
    print("Main Menu")
    print("Enter 1 for measurements")
    print("Enter 2 for exercises")
    print("Enter 3 for BMI calculator ")
    print("Enter 4 to exit Get Fit! app")
    choice = input("Enter your selection: ")
    return choice

def measurements_submenu():
    print("Measurements Menu")
    print("1. Enter 1 to add your measurements")
    print("2. Enter 2 to view measurement history")
    print("3. Enter 3 to search measurement history")
    print("4. Enter 4 to return to main menu")
    choice = input("Enter your selection: ")
    return choice

def exercise_submenu():
    print("Exercise Menu")
    print("1. Enter 1 to add an exercise")
    print("2. Enter 2 to view exercise history")
    print("3. Enter 3 to search exercise history")
    print("4. Enter 4 to return to main menu")
    choice = input ("Enter your selection: ")
    return choice

user_choice = ""

#This code shows how the user will navigate the menus using conditionals.
while user_choice != "4":
    user_choice = main_menu()
    
    if user_choice == "1":
        measurements_choice = ""
        while measurements_choice != "4":
            measurements_choice = measurements_submenu()
            
            if measurements_choice == "1":
                update_measurement(measurements)
            elif measurements_choice == "2":
                view_measurements(measurements)
            elif measurements_choice == "3":
                search_measurements(measurements)
            elif measurements_choice == "4":
                continue
            else:
                print("Invalid input")
                
    elif user_choice == "2":
        exercise_choice = ""
        while exercise_choice != "4":
            exercise_choice = exercise_submenu()
            
            if exercise_choice == "1":
                add_exercise(exercises)
            elif exercise_choice == "2":
                view_exercises(exercises)
            elif exercise_choice == "3":
                search_exercises(exercises)
            elif exercise_choice == "4":
                continue
            else:
                print("Invalid input")
                
    elif user_choice == "3":
        calculate_bmi()
        
    elif user_choice == "4":
        continue
    else:
        print("Invalid input")
            
print("Thank you for using the Get Fit! app")