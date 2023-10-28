"""
    CS 5001
    10/28/2023
    Align Online Module 6 - pizza_version4.py
    Garfield Maitland
"""

"""
    Module: Handing Exceptions
    
    Now we are using the try and except blocks of code in an effort to forgive,
    the user of their error.
"""


def get_slices(pies, folks):
    '''
        Function: get_slices that calculates the number of slices of pizza
        Params:   pies, the number of pies
                  folks, the number of people
        Returns:  the number of slices per person
    '''
    if not isinstance(folks, int):
        raise TypeError("folks must be an integer")
    if folks <= 0:
        raise ValueError("folks must be positive")
    if not isinstance(pies, int):
        raise TypeError("pies must be an integer")
    if pies < 0:
        raise ValueError("pies must be non-negative")
    slices = pies * 8 // folks
    return slices


def main():
    try:
        pizzas = int(input("How many pizzas did you order? "))
        people = int(input("How many people are there? "))
        slices = get_slices(pizzas, people)
        print(pizzas, "pizzas split", people,
              "ways is", slices, "slices each")

    except TypeError as ex:
        print("Invalid type:", ex)
    except ValueError as ex:
        print("Something went wrong. You goofed", ex)







"""
    except TypeError as ex:
        print("Invalid type:", type(ex), ex)
    except ValueError as ex:
        print("Invalid value:", type(ex), ex)
"""



main()
