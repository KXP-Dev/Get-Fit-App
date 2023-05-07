import csv
from utils import get_date_input, get_float_input, get_string_input


def add_exercise(exercises):
    print("Add Exercise")
    try:
        with open(exercises, "a", newline='') as open_exercises:
            writer = csv.writer(open_exercises)
            exercise_name = get_string_input(
                "Enter the name of the exercise: ")
            exercise_date = get_date_input(
                "Enter the date of the exercise (dd/mm/yyyy): ")
            sets = get_float_input("Enter the number of sets: ")
            repetitions = get_string_input(
                "Enter the number of repetitions (Each set is seperated by slashes): ")
            writer.writerow([exercise_name, exercise_date, sets, repetitions])
        print("Exercise added successfully")
    except Exception as e:
        print(f"Something went wrong: {e}")
        input("Press Enter to confirm continue from error...")
    input("Press Enter to go back to menu...")
