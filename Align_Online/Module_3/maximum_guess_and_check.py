"""
    CS 5001
    10/23/2023
    Align Online Module 3 - maximum_guess_and_check.py
    Garfield Maitland
"""

"""
    This code implements the "Guess and Check" algorithm to find the maximum of
    the five numbers entered into the keyboard.  It "guesses" that the first number
    is the maximum and then "checks" each of the other four numbers against the
    current guess correcting the guess as necessary.
"""


def main():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    third = int(input("Enter third number: "))
    fourth = int(input("Enter fourth number: "))
    fifth = int(input("Enter fifth number: "))

    # compute the maximum
    max = first
    if second > max:
        max = second
    if third > max:
        max = third
    if fourth > max:
        max = fourth
    if fifth > max:
        max = fifth
    # print result
    print("Maximum number is", max)


main()
