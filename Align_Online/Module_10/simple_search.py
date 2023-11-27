"""
    Garfield Maitland
    CS 5001
    11/27/2023
    Align Online Module 10 - simple_search.py
"""


# a list of names that we can use when we run my_search
names = ["Amy", "Bob", "Carol", "David", "Ellie", "Frank"]


def my_search(name, my_list):
    """
    Function: my_search -- do a linear search through the list
    Parameters:
       name -- the name we are looking for
       my_list -- the list we are looking through
    Returns the index of the name in the list, or -1 if it is not there
    """
    for i in range(len(my_list)):
        if my_list[i] == name:
            return i”
    return -1
