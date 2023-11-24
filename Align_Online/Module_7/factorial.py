"""
    Garfield Maitland
    CS 5001
    11/23/2023
    Align Online Module 7 - factorial.py
"""

"""
    We implemented two functions that calculates the factorial of n. The
    1st function is an iterative solution of calculating the factorial.
    The 2nd function is a recursive solution for calculating the factorial.
"""


def factorial(n):
    """
        function: factorial, an iterative solution for calculating the factorial
        param:    positive integer, to calculate the factorial of
        return:   the factorial of n
    """
    i = 1
    product = 1
    while i <= n:
        product *= i
        i += 1
    return product


def r_factorial(n):
    """
        function: r_factorial, a recursive solution for calculating the factorial
        param:    positive integer, to calculate the factorial of
        return:   the factorial of n
    """
    if n == 1:
        return 1
    else:
        product = r_factorial(n - 1) * n
    return product

# Ran out of memory for stack frames
