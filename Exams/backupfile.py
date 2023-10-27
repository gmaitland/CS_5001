"""
    CS 5001
    10/24/2023
    Midterm Exam - midterm.py
    Garfield Maitland
"""


# 10
def base_area(base_length: float, width: float) -> float:
    """
    Function: base_area()
        Calculates the base of a pyramid.

    Parameters:
        base_length (type: float)
        width (type: float)

    Returns:
        base = base_length x width -> float

    Defense:
        Clamp out-of-band values. Any base_length OR width <
        or equal to 0 are replaced with a 1.
    """
    if base_length <= 0:
        base_length = 1

    if width <= 0:
        width = 1

    base = base_length * width

    print(base)
    return base


def pyramid_volume(base: float, height: float):
    """
    Function: pyramid_volume()
        Calculates the volume of a pyramid.

    Parameters:
        base (type: float)
        height (type: float)

    Returns:
        volume -> float

    Defense:
        Clamp out-of-band values. Any base OR width <
        or equal to 0 are replaced with a 1.
    """
    if height <= 0:
        height = 1

    volume = (base * height) * (1 / 3)

    print(volume)
    return volume


# 11
def swap_them(a_list):
    """
    Function: swap_them()
        Swaps the order of a list.

    Parameters:
        a_list

    Returns:
        a_list

    Defense:
        None
    """
    a_list[0], a_list[-1] = a_list[-1], a_list[0]

    print(a_list)
    return a_list


# 12
def resequencing(a_list):
    """
    Function: resequencing()
        Orders a list in the correct order.

    Parameters:
        a_list

    Returns:
        a_string

    Defense:
        None
    """
    b_list = sorted(a_list)

    c_list = []
    for i in b_list:
        c_list.append(str(i))

    a_string = " ".join(c_list)

    print(a_string)
    return a_string


# 13
def text_talk(a_string):
    """
    Function: text_talk()
        Converts abbreviations into their full statements.

    Parameters:
        a_string

    Returns:
        a_string

    Defense:
        None
    """
    abbreviations = ["LOL", "TTYL", "IRL", "SMH"]
    statements = ["laugh out loud", "talk to you later", "in real life",
                  "shaking my head"]

    b_string = a_string.split()

    for i, word in enumerate(b_string):
        if word in abbreviations:
            index = abbreviations.index(word)
            b_string[i] = statements[index]

    c_string = ' '.join(b_string)
    a_string = c_string

    print(a_string)
    return a_string


# 14
def flipper(a_list):
    """
    Function: flipper()
        Converts abbreviations into their full statements.

    Parameters:
        a_list

    Returns:
        None

    Defense:
        None
    """
    i = 0
    while i < len(a_list):
        a_list[i] = not a_list[i]
        i += 1

    print(a_list)


# """

def main():
    # a = 10
    # b = 15
    # base_area(a, b)
    pyramid_volume(base_area(3, 3), 9)
    # print(volume)

    a_list = ["a", "b", "c", "d", "e"]
    swap_them(a_list)

    b_list = [5, 3, 4]
    resequencing(b_list)

    a_string = "Wow I had to LOL and TTYL after that."
    text_talk(a_string)

    a_list = [True, False, True, False, False]
    flipper(a_list)

main()

# """
