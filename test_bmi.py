import pytest


def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def calculate_bmi_category(weight, height):
    bmi = round(weight / (height ** 2), 2)
    if bmi < 18.5:
        category = "underweight"
    elif bmi < 25:
        category = "healthy weight"
    elif bmi < 30:
        category = "overweight"
    else:
        category = "obese"
    return category


def test_bmi_calculator():
    # Test case 1: Checking if the BMI formula works as expected.
    weight = 80  # kg
    height = 1.75  # meters
    expected_bmi = 26
    assert calculate_bmi(weight, height) == pytest.approx(expected_bmi, 0.01)


def test_bmi_fail_check():
    # Test case 2: Checking to see if the test fails to make sure the formula is working as expected.
    weight = 80  # kg
    height = 1.75  # meters
    expected_bmi = 31
    assert calculate_bmi(weight, height) == pytest.approx(expected_bmi, 0.01)


def test_underweight_category():
    # Test case 1: Checking if the BMI category function works as expected for the underweight category.
    weight = 50  # kg
    height = 1.75  # meters
    expected_category = "underweight"
    assert calculate_bmi_category(weight, height) == expected_category


def test_overweight_category():
    # Test case 2: Checking if the test fails for the overweight category.
    weight = 100  # kg
    height = 2  # meters
    expected_category = "obese"
    assert calculate_bmi_category(weight, height) == expected_category
