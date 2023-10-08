'''
CS5001
Fall 2023
Garfield Maitland
Homework 2: windchill.py
'''

from temperature_conversion import (convert_fahrenheit_to_celsius,
                                    convert_celsius_to_fahrenheit
                                    )
MPH_KPH = 1.61


def calculate_windchill(temperature, speed):
    """
       Function: calculate_windchill()
       Calculates windchill based on international formula (Metric)

       Parameters:
           temperature (float) - Temperature in Fahrenheit
           speed (float) - Wind speed in miles per hour

       Returns:
           windchill index (float) in Fahrenheit based on the formula

       Require:
           Temperature and speed in metric units (Fahrenheit and MPH)

       Ensure:
           Metric to imperial unit conversions prior to calculation

       Examples:
       >>> calculate_windchill(32, 10)
       23.691426059765107
       >>> calculate_windchill(0, 30)
       -25.926882447797837
    """

    # Convert temperature to Celsius (metric unit)
    temperature_celsius = convert_fahrenheit_to_celsius(temperature)

    # Convert MPH to KPH
    speed = speed * MPH_KPH

    # Calculate windchill index in metric units
    windchill_metric = (13.12 + 0.6215 * temperature_celsius - 11.37 * (
            speed ** 0.16) + 0.3965 * temperature_celsius * (speed ** 0.16))

    # Convert windchill index to Fahrenheit (imperial unit)
    windchill_imperial = convert_celsius_to_fahrenheit(windchill_metric)

    return windchill_imperial


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
