"""
    Garfield Maitland
    CS 5001
    11/21/2023
    Practice - a_function_as_an_object.py
"""

"""
    This program has a few working parts. At a high level, we have defined 3 functions.
    We have the apply_to_all() function, the multiply() function and of course,
    we have our main function. The apply_to_all() function is where the majority
    of the functionality is happening. In that function we have three parameters
    the 1st parameter is for a list. The 2nd parameter calls a function. The 3rd
    and final parameter stores a value.

    In our main function, we have declared, assigned, and initialized a list called
    a_list. The we DAI another list called b_list. b_list has function calls within
    it's implementation. b_list calls the function apply_to_all() with the multiply()
    function nested within it. It's last parameter is the argument 5.

    b_list calls apply_to_all() which has a temporary empty list, and a for loop. The
    for loop appends values to the empty list. Additionally, it calls the 2nd argument
    passed in, which is a function, and in this instance is the multiply() function.
    The multiply function takes in each element passed by the for apply_to_all for loop
    and multiplies it by the value, and returns it to the caller function and stores
    it into the out = [] list. After all the elements of lst have been iterated through
    the value is returned to main. And is then printed.
"""


def apply_to_all(lst, a_function, a_value):
    """
        Applies a function to each element of a list
    """
    out = []
    for item in lst:
        out.append(a_function(item, a_value))
    return out


def multiply(item, value):
    return item * value


def divide(item, value):
    return item / value


def main():
    a_list = [1, 2, 3, 4, 5]
    b_list = apply_to_all(a_list, multiply, 5) # multiply by 5
    print(b_list)
    c_list = apply_to_all(a_list, divide, 5) # divide by 5
    print(c_list)
    d_list = apply_to_all(b_list, divide, 5) # divide by 5
    print(d_list)


if __name__ == "__main__":
    main()