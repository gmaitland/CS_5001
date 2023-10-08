"""
    Garfield Maitland
    CS 5001
    09/30/2023
    Homework 3 - chessboard.py
"""

# from color_square import black_or_white


def check_valid_row(row):
    """
    Function: check_valid_row()
        Checks the user input to determine if it is a valid row

    Parameters:
        row int: Is an int that represents the selected hex value.

    Preconditions:
        None

    Returns:
        True if it is a valid row
        False if it is an invalid row
    """
    row = int(row)
    if row >= 1 and row <= 8:
        print("Valid row")
        return True
    else:
        print("Invalid row number")
        return False


def check_valid_column(column):
    """
    Function: check_valid_column()
        Checks the user input to determine if it is a valid column

    Parameters:
        column int: Is an int that represents the selected hex value.

    Preconditions:
        None

    Returns:
        True if it is a valid column
        False if it is an invalid column
    """
    column = column.lower()
    if ord(column) >= 97 and ord(column) <= 104:
        print("Valid column")
        return True
    else:
        print("Invalid column coordinate")
        return False

"""
# def check_valid_input(row, column):
    
    Function: check_valid_input()
        Checks the user input to determine if it is a valid row and column
        Calls the check_valid_row() and the check_valid_column() methods
        Calls the black_or_white() method to determine BLACK or WHITE

    Parameters:
        row int: Is an int that represents the selected hex value.

    Preconditions:
        None

    Returns:
        None
    
    column = column.lower()
    if check_valid_row(row) and check_valid_column(column):
        square_color = black_or_white(row, column)
        if square_color:
            print(f"This is a valid {square_color} square")
        else:
            print("This is not a valid square")
    else:
        print("This is not a valid square")
"""


def main():
    row = int(input("What row? "))
    column = input("What column? ").lower()  # Convert to lowercase
    # check_valid_input(row, column)


if __name__ == "__main__":
    main()
