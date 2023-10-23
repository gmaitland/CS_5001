"""
    CS 5001
    10/23/2023
    Align Online Module 4 - tuple_example.py
    Garfield Maitland
"""

"""
    We are practicing creating tuples and observing their structure
    and, attributes and properties. We are also practicing how to use
    a while loop
"""


def main():
    weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")
    index = 0
    while index < len(weekdays):
        print(weekdays[index])
        index += 1


main()
