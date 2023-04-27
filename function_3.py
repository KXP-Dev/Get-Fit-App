def calculate_bmi():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = round(weight / (height ** 2), 2)
    print("Your BMI is:", bmi)