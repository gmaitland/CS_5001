"""
    CS 5001
    10/23/2023
    Align Online Module 3 - days_of_month.py
    Garfield Maitland
"""

"""
CS 5001: Intensive Foundations of Computer Science
Module: Boolean Expressions & Conditionals
Lesson 3-5: Logical Operators

This determines the number of days given a month entered into the keyboard
assuming 3-letter abbreviations.  It then prints the number of days.

This is the program we wrote in Lesson 3-5.
"""


def main():
    month = input("Enter month (3 letter abbreviation please): ")
    # determine the number of days
    if month == "Feb": # Conditional Statement
        days = 28 # Code Block Body
    elif month == "Sep" or month == "Apr" or month == "Jun" or month == "Nov":
        days = 30 # Code Block Body
    else:
        days = 31
    print(month, "has", days, "days")


main()

"""
    How to improve? Have the conditional have the .titled() or .capitalized() method
"""