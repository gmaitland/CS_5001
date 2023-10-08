from chessboard import check_valid_row, check_valid_column

BLACK = "BLACK"
WHITE = "WHITE"


def black_or_white(row, column):
    """
    Function: black_or_white()
        If both the column & row are even then we know the square is BLACK
        If both the column & row are odd then we know the square is BLACK
        If the column and row are not the same we know the square is WHITE

    Parameters:
        row int: Is an int that represents the selected hex value.
        column int: Is an int that represents the hex value.

    Preconditions:
        None

    Returns:
        BLACK if both column and row are even
        BLACK if both column and row are odd
        WHITE if one or the other is even and odd
    """
    row = int(row)
    column = column.lower()
    if check_valid_row(row) and check_valid_column(column):
        if row % 2 == 0 and ord(column) % 2 == 0:
            return BLACK
        elif row % 2 != 0 and ord(column) % 2 != 0:
            return BLACK
        else:
            return WHITE