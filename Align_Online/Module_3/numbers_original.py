"""
    CS 5001
    10/23/2023
    Align Online Module 3 - numbers_original.py
    Garfield Maitland
"""


"""
    Our code prints the written word of a number between 1 and 5
    inclusive of the numbers 1 and 5. We are using if, elif
    and else 
"""

def main():
    number = int(input("Enter integer between 1 and 5 (inclusive)"))

    if number == 1:
        print("one")
    else:
        if number == 2:
            print("two")
        else:
            if number == 3:
                print("three")
            else:
                if number == 4:
                    print("four")
                else:
                    print("five")

    print("Done")


main()
