"""
    CS 5001
    10/23/2023
    Align Online Module 3 - bad_example.py
    Garfield Maitland
"""
"""
    This is for a loop. However it is not a great example
    because as it is currently implemented, it reads,
    10 positive values from user input
"""


def main():
    counter = 1
    while counter != -1:
        value = int(input("Enter value: "))
        if value > 0:
            counter += 1
        if counter > 10:
            counter = -1
    print("Done!")


main()
