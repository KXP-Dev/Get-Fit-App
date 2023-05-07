import os
from pathlib import Path

# This test checks if my csv handling is working as expected when creating a csv if it doesn't exist yet.
def test_create_csv():
    os.remove("measurements.csv")
    assert Path("measurements.csv").is_file() == False
    try:
        open_measurements = open("measurements.csv", "r")
        open_measurements.close()
    except FileNotFoundError as e:
        open_measurements = open("measurements.csv", "w")
        open_measurements.write("Measurements\n")
        open_measurements.close()
    assert Path("measurements.csv").is_file() == True

# This test checks the csv handling of my terminal app by making sure if an existing csv file exists it will load it.
def test_load_csv():
    with open("measurements.csv", "w") as f:
        f.write("Measurements\n")
    try:
        open_measurements = open("measurements.csv", "r")
        open_measurements.close()
        print("Measurement CSV Loaded")
    except FileNotFoundError as e:
        print("Measurement CSV not found")

    assert Path("measurements.csv").is_file() == True