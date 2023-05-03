from datetime import datetime

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_date_input(prompt):
    while True:
        try:
            value = datetime.strptime(input(prompt), "%d/%m/%Y").date()
            return value
        except ValueError:
            print("Invalid input. Please enter a date in the format dd/mm/yyyy.")
            
def get_string_input(prompt):
    while True:
        string_text = input(prompt)
        if not string_text:
            print("Empty value. Please enter text")
        else:
            return string_text