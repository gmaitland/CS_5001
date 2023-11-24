"""
    Garfield Maitland
    CS 5001
    11/23/2023
    Align Online Module 7 - factorial_debugging.py
"""

''' Align Online
    CS5001
    Sample code for Module 9: Recursion.
    Example of debugging techniques for a recursive function 
'''

"""
    Practicing debugging techniques for a recursive function. We 
    can do this by using print statements.
"""


def r_factorial(n, level):
    """
    function: r_factorial, a recursive solution for calculating the factorial
    param:    positive integer, to calculate the factorial of
    return:   the factorial of n
    """
    print("> " * level, "r_factorial(", n, "): START")
    if n == 1:
        return 1
    else:
        product = r_factorial(n - 1, level + 1) * n
        print("> " * level, "r_factorial(", n, "): END: return", product)
    return product


# Learn how to use the debugger. Shows an instantaneous snapshot.
