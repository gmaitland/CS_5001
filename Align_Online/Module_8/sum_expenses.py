"""
    Garfield Maitland
    CS 5001
    11/09/2023
    Align Online Module 8 - sum_expenses.py
"""


"""
    Function calculates the sum of charges and returns it's last value.
"""


def sum_expenses(charges):
    """ 
    sum_expenses: calculates the sum of all the charges. 
    params: a list of charges
    returns: the sum of all the charges
    """

    sum = 0
    for i in range(len(charges)):
        if isinstance(charges[i], list): # seems like the list argument is a new param element
            sum += sum_expenses(charges[i]) # calculate the running sum
        else:
            sum += charges[i]
        print("DEBUG: i =", i, ", sum =", sum)
        print("Sum has been calculated")
    return sum


# a simple list of expenses
receipts = [10, 11, 10, 11, 13, 15, 16, 17, 18]

# a nested list of expenses
nested_receipts = [10, 11, [6, 2, 2], 11, 13]

# a nested list of nested lists of expenses
ugly_receipts = [1, 2, [3, 4, [5, 6, [7, 6, 8]]]]


