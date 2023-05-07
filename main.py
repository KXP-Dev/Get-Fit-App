from utils import print_color
from function_1 import update_measurement
from function_2 import view_measurements
from function_3 import calculate_bmi
from function_4 import add_exercise
from function_5 import view_exercises
from function_6 import search_exercises
from function_7 import search_measurements
from function_8 import view_bmi

print_color("Welcome to the Get Fit! app", "yellow_bold")

measurements = "measurements.csv"
exercises = "exercises.csv"
bmi = "bmi.csv"

try:
    open_measurements = open(measurements, "r")
    open_measurements.close()
    print_color("Measurement CSV Loaded", "green")
except FileNotFoundError as e:
    open_measurements = open(measurements, "w")
    open_measurements.write("Measurements\n")
    open_measurements.close()
    print_color("Created Measurement CSV", "light_blue")
    
try:
    open_exercises = open(exercises, "r")
    open_exercises.close()
    print_color("Exercise CSV Loaded", "green")
except FileNotFoundError as e:
    open_exercises = open(exercises, "w")
    open_exercises.write("Exercises\n")
    open_exercises.close()
    print_color("Created Exercise CSV", "light_blue")
    
try:
    open_bmi = open(bmi, "r")
    open_bmi.close()
    print_color("BMI CSV Loaded", "green")
except FileNotFoundError as e:
    open_bmi = open(bmi, "w")
    open_bmi.write("BMI\n")
    open_bmi.close()
    print_color("Created BMI CSV", "light_blue")

def main_menu():
    print_color("Main Menu", "white_bold")
    print_color("Enter 1 for measurements", "cyan")
    print_color("Enter 2 for exercises", "cyan")
    print_color("Enter 3 for BMI", "cyan")
    print_color("Enter 4 to exit Get Fit! app", "cyan")
    choice = input("Enter your selection: ")
    return choice

def measurements_submenu():
    print_color("Measurements Menu", "white_bold")
    print_color("1. Enter 1 to add your measurements", "cyan")
    print_color("2. Enter 2 to view measurement history", "cyan")
    print_color("3. Enter 3 to search measurement history", "cyan")
    print_color("4. Enter 4 to return to main menu", "cyan")
    choice = input("Enter your selection: ")
    return choice

def exercise_submenu():
    print_color("Exercise Menu", "white_bold")
    print_color("1. Enter 1 to add an exercise", "cyan")
    print_color("2. Enter 2 to view exercise history", "cyan")
    print_color("3. Enter 3 to search exercise history", "cyan")
    print_color("4. Enter 4 to return to main menu", "cyan")
    choice = input ("Enter your selection: ")
    return choice

def bmi_submenu():
    print_color("BMI Menu", "white_bold")
    print_color("1. Enter 1 to calculate your BMI", "cyan")
    print_color("2. Enter 2 to view your BMI history", "cyan")
    print_color("3. Enter 3 to return to main menu", "cyan")
    choice = input("Enter your selection: ")
    return choice

user_choice = ""

while user_choice != "4":
    user_choice = main_menu()
    
    try:
        if user_choice not in ["1", "2", "3", "4"]:
            raise ValueError("Invalid Input. Enter a selection between 1 and 4")
        
        if user_choice == "1":
            measurements_choice = ""
            while measurements_choice != "4":
                measurements_choice = measurements_submenu()
                
                try:
                    if measurements_choice not in ["1", "2", "3", "4"]:
                        raise ValueError("Invalid Input. Enter a selection between 1 and 4")
                        
                    if measurements_choice == "1":
                        update_measurement(measurements)
                    elif measurements_choice == "2":
                        view_measurements(measurements)
                    elif measurements_choice == "3":
                        search_measurements(measurements)
                        
                except ValueError as ve:
                    print(ve)
                    input("Press Enter to confirm continue from error...")
                except Exception as e:
                    print(f"Something went wrong: {e}")
                    input("Press Enter to confirm continue from error...")
                    
        elif user_choice == "2":
            exercise_choice = ""
            while exercise_choice != "4":
                exercise_choice = exercise_submenu()
                
                try:
                    if exercise_choice not in ["1", "2", "3", "4"]:
                        raise ValueError("Invalid Input. Enter a selection between 1 and 4")
                        
                    if exercise_choice == "1":
                        add_exercise(exercises)
                    elif exercise_choice == "2":
                        view_exercises(exercises)
                    elif exercise_choice == "3":
                        search_exercises(exercises)
                        
                except ValueError as ve:
                    print(ve)
                    input("Press Enter to confirm continue from error...")
                except Exception as e:
                    print(f"Something went wrong: {e}")
                    input("Press Enter to confirm continue from error...")
                    
        elif user_choice == "3":
            bmi_choice = ""
            while bmi_choice != "3":
                bmi_choice = bmi_submenu()
                
                try:
                    if bmi_choice not in ["1", "2", "3"]:
                        raise ValueError("Invalid Input. Enter a selection between 1 and 3")
                        
                    if bmi_choice == "1":
                        calculate_bmi()
                    elif bmi_choice == "2":
                        view_bmi(bmi)
                        
                except ValueError as ve:
                    print(ve)
                    input("Press Enter to confirm continue from error...")
                except Exception as e:
                    print(f"Something went wrong: {e}")
                    input("Press Enter to confirm continue from error...")
                    
    except ValueError as ve:
        print(ve)
        input("Press Enter to confirm continue from error...")
    except Exception as e:
        print(f"Something went wrong: {e}")
        input("Press Enter to confirm continue from error...")
            
print_color("Thank you for using the Get Fit! app", "red_bold")