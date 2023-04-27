def calculate_bmi():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = round(weight / (height ** 2), 2)
    print("Your BMI is:", bmi)
    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("You have a healthy weight.")
    elif bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")