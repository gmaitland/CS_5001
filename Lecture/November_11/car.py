"""
    Garfield Maitland
    CS 5001
    11/14/2023
    Lecture - car.py
"""


class Car:
    """
        This is the Car class. It simulates doing car stuff
    """

    def __init__(self, name, year, mileage=0):
        """ constructor for the Car class """
        self.name = name
        self.year = year
        self.mileage = mileage

    def register(self, year_reg):
        print(f"Registering {self.name} for year {year_reg}")

    def drive(self):
        print(f"Driving {self.name} ")
        self.mileage += 20
