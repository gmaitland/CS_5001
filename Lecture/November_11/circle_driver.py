"""
    Garfield Maitland
    CS 5001
    11/14/2023
    Lecture - circle_driver.py
"""

from circle import Circle


def main():
    c = Circle(2, 1, 1)
    cc = Circle(3)
    copy = Circle(2, 1, 1)

    print(c)
    print(c.get_area())

    print(cc)
    print(cc.get_area())

    print(c == copy)

    # Checking the equivalence of the object instance


if __name__ == "__main__":
    main()
