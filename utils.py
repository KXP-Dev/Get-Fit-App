from datetime import datetime
from colorama import Fore, Style

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 300:
                return value
            else:
                print("Unreasonable Number. Please enter a number between 0 and 300.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"Something went wrong: {e}")

def get_date_input(prompt):
    while True:
        try:
            value = datetime.strptime(input(prompt), "%d/%m/%Y").date()
            return value
        except ValueError:
            print("Invalid input. Please enter a date in the format dd/mm/yyyy.")
        except Exception as e:
            print(f"Something went wrong: {e}")
            
def get_string_input(prompt):
    while True:
        try:
            string_text = input(prompt)
            if not string_text:
                raise ValueError("Invalid input. Please enter an exercise")
            else:
                return string_text
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Something went wrong: {e}")
        
def print_color(text, color):
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
    elif color == "white_bold":
        print(Fore.WHITE + Style.BRIGHT + text)
    else:
        print(text)