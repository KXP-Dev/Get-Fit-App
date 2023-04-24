import csv

def update_measurement(measurements):
    print("Update measurement")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in cm: "))
    date = input("Today's date: ")
    with open(measurements, "a", newline='')as open_measurements:
        writer = csv.writer(open_measurements)
        writer.writerow(["Date", " Height (cm)", " Weight (kg)"])
        writer.writerow([date, height, weight])