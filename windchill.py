'''
CS5001
Fall 2023
Garfield Maitland
Homework 2: windchill.py
'''

from temperature_conversion import convert_fahrenheit_to_celsius, convert_celsius_to_fahrenheit

def calculate_windchill(temperature, speed):
    '''
    Function: calculate_windchill()
    Calculates windchill based on international formula (Metric)
    Parameters:
        temperature (float) - Temperature in Fahrenheit
        speed (float) - Wind speed in miles per hour
    Returns:
        windchill index (float) in Fahrenheit based on the formula
    Require:
        Temperature and speed in metric units (Fahrenheit and miles per hour)
    Ensure:
        Metric to imperial unit conversions prior to calculation
    '''

    # Convert temperature to Celsius (metric unit)
    temperature_celsius = convert_fahrenheit_to_celsius(temperature)

    # Calculate windchill index in metric units
    windchill_metric = 13.12 + 0.6215 * temperature_celsius - 11.37 * (speed ** 0.16) + 0.3965 * temperature_celsius * (speed ** 0.16)

    # Convert windchill index to Fahrenheit (imperial unit)
    windchill_imperial = convert_celsius_to_fahrenheit(windchill_metric)

    return windchill_imperial

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)


