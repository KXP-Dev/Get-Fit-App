import csv
from utils import get_date_input
from prettytable import PrettyTable

def add_exercise(excersises):
    print("Add Excersise")
    with open(excersises, "a") as file:
        exercise_name = input("Enter the name of the exercise: ")
        exercise_date = input("Enter the date of the exercise (yyyy-mm-dd): ")
        sets = input("Enter the number of sets: ")
        repetitions = input("Enter the number of repetitions: ")
        file.write(f"{exercise_name},{exercise_date},{sets},{repetitions}\n")
    print("Exercise added successfully")