"""
    Garfield Maitland
    CS 5001
    11/14/2023
    Lecture - car_driver.py
"""

from car import Car


def main():
    car = Car("Corolla", 2018, 45000)
    other_car = Car("Mustang", 2023, 2)
    smart_car = Car("Smart Car", 2020, 17000)

    car.register(2023)
    other_car.register(2024)
    smart_car.register(2021)

    other_car.drive()

    print(car)
    print(car.get_mileage() + 1 ) # Legal but not recommended


if __name__ == "__main__":
    main()
