"""
    CS 5001
    10/22/2023
    Align Online Module 2 - return_statements
    Garfield Maitland
"""

"""
Practice with return statements and convert,
Tugboat's weight from stone to pounds.
"""


def get_pounds_weight(stone_weight):
    """
        Function get_pounds_weight
        Parameters: number, weight in stone
        Return: number, weight in pounds
    """
    pounds = stone_weight * 14
    return pounds


def main():
    stone = 5.3
    # same variable name as in the function above
    pounds = get_pounds_weight(stone)
    print("Your dog weighs", pounds, "pounds!")


main()

"""
Created a function to convert stone weight to
pounds. Then we had that function return the
value which was assigned to the pounds variable
to the function caller, which was main. The most
complex portion of the code was the arithmetic
that happened at line 19, and the function
declaration which spans line 13 to line 20
"""
