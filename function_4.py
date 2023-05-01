import csv
from utils import get_date_input
from prettytable import PrettyTable

def add_exercise(exercises):
    print("Add Exercise")
    with open(exercises, "a") as open_exercises:
        exercise_name = input("Enter the name of the exercise: ")
        exercise_date = get_date_input("Enter the date of the exercise (dd/mm/yyyy): ")
        sets = input("Enter the number of sets: ")
        repetitions = input("Enter the number of repetitions (separated by slashes): ")
        open_exercises.write(f"{exercise_name},{exercise_date},{sets},{repetitions}\n")
    print("Exercise added successfully")
    input("Press Enter to go back to menu...")