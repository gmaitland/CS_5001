"""
    CS 5001
    10/23/2023
    Align Online Module 3 - numbers_inefficient.py
    Garfield Maitland
"""

"""
    This program prints exactly one message for a number between 1 and 5.
    
    In this version of the program, the sequential if statements all must run
    one after the other making this a less efficient version of this example.
    
This code is less efficient than a more efficient implementation.
"""


def main():
    number = int(input("Enter integer between 1 and 5 (inclusive)"))

    if number == 1:
        print("one")
    if number == 2:
        print("two")
    if number == 3:
        print("three")
    if number == 4:
        print("four")
    if number == 5:
        print("five")
    print("Done")


main()
