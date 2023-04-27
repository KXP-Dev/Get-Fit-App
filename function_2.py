import csv

def view_measurements(measurements):
    print("Viewing measurement history")
    with open(measurements, "r") as open_measurements:
        reader = csv.reader(open_measurements)
        for row in reader:
            print(", ".join(row))