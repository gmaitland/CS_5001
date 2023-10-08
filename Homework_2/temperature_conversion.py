'''
CS5001
Fall 2023
Garfield Maitland
Homework 2: Temperature Converter Starter Code (temperature_conversion.py)
'''

FAHRENHEIT_BASE = 32

def convert_fahrenheit_to_celsius(temperature):
    """
    Function -- convert_fahrenheit_to_celsius
    Converts temperature from F to C
    Parameters:
    temperature (float) -- the original temperature in Fahrenheit
    Returns a float value representing the original temperature converted
    to Celsius
    """
    return (temperature - FAHRENHEIT_BASE) * 5/9

def convert_celsius_to_fahrenheit(temperature):
    '''
    Function -- convert_celsius_to_fahrenheit
    Converts temperature from C to F
    Parameters:
    temperature (float) -- the original temperature in Celsius
    Returns a float value representing the original temperature converted
    to Fahrenheit
    '''
    return ((temperature / 5) * 9) + FAHRENHEIT_BASE
