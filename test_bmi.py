import os
from pathlib import Path
import csv
from utils import get_float_input, get_date_input
import pytest
from function_3 import calculate_bmi


def test_bmi_csv_created():
    os.remove("bmi.csv")
    assert Path("bmi.csv").is_file() == False
    # Call the code block that creates the CSV
    try:
        open_bmi = open("bmi.csv", "r")
        open_bmi.close()
    except FileNotFoundError as e:
        open_bmi = open("bmi.csv", "w")
        open_bmi.write("BMI\n")
        open_bmi.close()
    # Check that the CSV now exists
    assert Path("bmi.csv").is_file() == True
    
import pytest

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
weight = 70 # kg
height = 1.75 # meters
bmi = calculate_bmi(weight, height)
print("Your BMI is:", bmi)

def test_calculate_bmi():
    # Test case 1: Normal BMI
    weight = 80 # kg
    height = 1.75 # meters
    expected_bmi = 22.86
    
    assert calculate_bmi(weight, height) == pytest.approx(expected_bmi, 0.01)
