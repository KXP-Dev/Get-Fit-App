import csv
from prettytable import PrettyTable


def view_bmi(bmi):
    print("Viewing BMI history")
    table = PrettyTable(["Date", "BMI", "Category"])
    try:
        with open(bmi, "r") as open_bmi:
            reader = csv.reader(open_bmi)
            next(reader)
            for row in reader:
                table.add_row([row[0], row[1], row[2]])
        print(table)
    except FileNotFoundError:
        print(f"{bmi} file not found.")
        input("Press Enter to confirm continue from error...")
    except Exception as e:
        print(f"Something went wrong: {e}")
        input("Press Enter to confirm continue from error...")
    input("Press Enter to go back to menu...")
