"""
    CS 5001
    10/23/2023
    Align Online Module 4 - temps_hot.py
    Garfield Maitland
"""

"""
    Using code to count the hot days in a list. We have two lists.
    The lists are initialized in an uppercase variable. Ok, that
    is how we use the range method, in a list.
"""

HIGH_TEMPS = [92, 84, 98, 87, 94, 86, 75, 81, 91, 96, 75,
              74, 78, 78, 76, 79, 77, 91, 83, 77, 79, 74,
              78, 86, 88, 87, 84, 82, 82, 81, 83]

HUMIDITY = [84, 90, 87, 74, 87, 79, 58, 72, 68, 76, 84,
            84, 93, 87, 93, 93, 97, 93, 61, 78, 81, 97,
            87, 87, 93, 93, 87, 87, 78, 84, 84]


def main():
    heat_days = 0 # the initialized variable
    for i in range(len(HIGH_TEMPS)):
        if HIGH_TEMPS[i] > 93 and HUMIDITY[i] > 65: # the conditional
            heat_days += 1 # the update statement
    print("We had", heat_days, "super HOT days in July!")


main()
