import csv
from prettytable import PrettyTable

def view_excersises(excersises):
    print("Viewing excersise history")
    with open(excersises, "r") as open_excersises:
        reader = csv.reader(open_excersises)
        for row in reader:
            print(", ".join(row))