"""
    Garfield Maitland
    CS 5001
    11/14/2023
    Lecture - Car.py
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

    def get_mileage(self):
        return self.mileage

    def drive(self):
        print(f"Driving {self.name} ")
        self.mileage += 20

    def __str__(self): # toString
        return f"{self.name} with Mileage: {self.mileage}"
