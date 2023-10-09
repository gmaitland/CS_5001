"""
    Garfield Maitland
    CS 5001
    10/02/2023
    Homework 4 - upc.py
"""


def is_valid_upc(list_of_integers):
    """
    Function: is_valid_upc()
        Takes a list of integers and determines if that list of integers
        can be evaluated as a upc number by checking its check digit

    Parameters:
        list_of_integers

    Preconditions:
        None

    Returns:
        is_valid
    """
    if (len(list_of_integers) < 2 or
            all(digit == 0 for digit in list_of_integers)):
        return False

    even_sum = sum(list_of_integers[-2::-2])
    odd_sum = sum(list_of_integers[-1::-2])

    check_digit = (even_sum * 3 + odd_sum) % 10

    is_valid = check_digit == 0

    return is_valid
