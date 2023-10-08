"""
    Garfield Maitland
    CS 5001
    09/30/2023
    Homework 3 - test_squares.py
"""

from chessboard import check_valid_row, check_valid_column


def test_squares():
    """
    Function: test_squares()
        Prints test cases for chessboard.py

    Parameters:
        row int: Is an int that represents the selected hex value.
        column int: Is an int that represents the selected hex value.

    Preconditions:
        None

    Returns:
        None
    """
    print("Test cases for valid squares:")
    row1 = 1
    column1 = 'a'
    check_valid_row(row1)
    check_valid_column(column1)
    print(f" Row: {row1}, Column: {column1}, Expected: True, Actual: True ")

    # Test invalid squares
    print("\nTest cases for invalid squares:")
    row4 = 0
    column4 = 'z'
    check_valid_row(row4)
    check_valid_column(column4)
    print(f" Row: {row4}, Column: {column4}, Expected: False, Actual: False ")


def main():

    test_squares()


if __name__ == "__main__":
    main()
