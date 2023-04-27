import csv
from utils import get_float_input

def calculate_bmi():
    while True:
        height = get_float_input("Enter your height in cm: ")
        if height <= 50 or height > 300:
            print("Please enter a value between 50 and 300 cm. Fun fact, Robert Wadlow was the world's tallest man at 272 cm.")
        else:
            break
    height = height / 100
    while True:
        weight = get_float_input("Enter your weight in kg: ")
        if weight <= 2 or weight > 650:
            print("Please enter a value between 2 and 650 kg. Fun fact, Jon Brower Minnoch was the world's heaviest man at 635 kg.")
        else:
            break
    bmi = round(weight / (height ** 2), 2)
    if bmi < 18.5:
        category = "underweight"
    elif bmi < 25:
        category = "healthy weight"
    elif bmi < 30:
        category = "overweight"
    else:
        category = "obese"
    print("Your BMI is:", bmi)
    print("You are in the", category, "category.")
    input("Press Enter to go back to menu...")