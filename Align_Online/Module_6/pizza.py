"""
    CS 5001
    10/28/2023
    Align Online Module 6 - pizza.py
    Garfield Maitland
"""

"""
Module: Handing Exceptions

This is the code that we are starting with in module 10.  Many changes 
will be made to the code and there will be a couple of different versions
as we cover the material in this module.
"""


def get_slices(pies, folks):
    """
        Function: get_slices that calculates the number of slices of pizza
        Params:   pies, the number of pies
                  folks, the number of people
        Returns:  the number of slices per person
    """
    if pies <= 0:
        raise ValueError("You big dummy \n"
                         "You can't have negative pizzas \n"
                         "Unless you expect people to bring their \n"
                         "Own pizza.")
    if not isinstance(folks, int) or folks <= 0:
        raise ValueError("You big dummy \n"
                         "Folks, should be greater than 0")
    if not isinstance(pies, int):
        raise TypeError("pies must be an integer")
    """
        if folks != 0:
        slices = pies * 8 // folks
        return slices
    """

def main():
    # get two integers from the user
    pizzas = int(input("How many pizzas did you order? "))
    people = int(input("How many people are there? "))
    slices = get_slices(pizzas, people)
    print(pizzas, "pizzas split", people, "ways is", slices, "slices each")


main()
