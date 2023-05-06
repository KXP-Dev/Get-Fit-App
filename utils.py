from datetime import datetime
from colorama import init, Fore, Style

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
        
def print_color(text, color):
    init(autoreset=True)
    if color == "yellow_bold":
        print(Fore.YELLOW + Style.BRIGHT + text)
    elif color == "green":
        print(Fore.GREEN + text)
    elif color == "light_blue":
        print(Fore.LIGHTBLUE_EX + text)
    elif color == "red_bold":
        print(Fore.RED + Style.BRIGHT + text)
    elif color == "cyan":
        print(Fore.CYAN + text)
    else:
        print(text)