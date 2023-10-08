"""
CS5001
Fall 2023
Garfield Maitland
Homework 2: test_temperature_conversion.py
"""

import temperature_conversion


def test_fahrenheit_to_celsius(expected_result, temperature):
    """
    Test the conversion of Fahrenheit to Celsius for a given temperature.

    Args:
        expected_result (float): The expected result of the Fahrenheit to Celsius conversion.
        temperature (float): The temperature in Fahrenheit to be converted.

    Returns:
        None
    """
    actual_result = temperature_conversion.convert_fahrenheit_to_celsius(temperature)
    print(f"Converting {temperature}°F to Celsius -- result: {actual_result:.1f}°C expected: {expected_result:.1f}°C")


def test_celsius_to_fahrenheit(expected_result, temperature):
    """
    Test the conversion of Celsius to Fahrenheit for a given temperature.

    Args:
        expected_result (float): The expected result of the Celsius to Fahrenheit conversion.
        temperature (float): The temperature in Celsius to be converted.

    Returns:
        None
    """
    actual_result = temperature_conversion.convert_celsius_to_fahrenheit(temperature)
    print(
        f"Converting {temperature}°C to Fahrenheit -- result: {actual_result:.1f}°F expected: {expected_result:.1f}°F")

def test_functions():
    print("Tests...")
    # Function 1 Tests
    test_expected0 = 0
    temperature0 = 32
    test_expected1 = 37.8
    temperature1 = 100
    test_expected2 = 100
    temperature2 = 212
    test_expected3 = 29.5
    temperature3 = 85.1
    test_expected4 = 537.8
    temperature4 = 1000
    test_fahrenheit_to_celsius(test_expected0, temperature0)  # Test 0: 32°F should be 0°C
    test_fahrenheit_to_celsius(test_expected1, temperature1)  # Test 1: 100°F should be 37.8°C
    test_fahrenheit_to_celsius(test_expected2, temperature2)  # Test 2: 212°F should be 100°C
    test_fahrenheit_to_celsius(test_expected3, temperature3)  # Test 3: 85.1°F should be 29.5°C
    test_fahrenheit_to_celsius(test_expected4, temperature4)  # Test 4: 1000°F should be 537.8°C

    # Function 2 Tests
    test_expected5 = 32
    temperature5 = 0
    test_expected6 = 100
    temperature6 = 37.8
    test_expected7 = 212
    temperature7 = 100
    test_celsius_to_fahrenheit(test_expected5, temperature5)  # Test 5: 0°C should be 32°F
    test_celsius_to_fahrenheit(test_expected6, temperature6)  # Test 6: 37.8°C should be 100°F
    test_celsius_to_fahrenheit(test_expected7, temperature7)  # Test 7: 100°C should be 212°F

def main():
    test_functions()

if __name__ == "__main__":
    main()
