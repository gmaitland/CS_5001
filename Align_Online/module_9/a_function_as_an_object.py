"""
    This program has a few working parts
"""

def apply_to_all (lst, a_function, a_value):
    """
        Applies a function to each element of a list
    """
    out = []
    for item in lst:
        out.append(a_function(item, a_value))
    return out


def multiply(item, value):
    return item * value


def main():
    a_list = [1, 2, 3, 4, 5]
    b_list = apply_to_all(a_list, multiply, 5) # multiply by 5
    print(b_list)


if __name__ == "__main__":
    main()