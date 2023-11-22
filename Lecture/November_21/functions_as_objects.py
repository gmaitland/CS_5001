"""
    Garfield Maitland
    CS 5001
    11/21/2023
    Lecture - functions_as_objects.py
"""


def apply_to_all(lst, a_function, a_value):
    out = []    # We do not want to mutate the list
    for item in lst:
        out.append(a_function(item, a_value))
    return out


def multiply(item, value):
    return item * value


def subtract(item, value):
    return item - value


def main():
    a = [1, 2, 3, 4, 5]
    b = apply_to_all(a, multiply, 5)
    c = apply_to_all(a, subtract, 1)
    print(a)
    print(b)
    print(c)


if __name__ == "__main__":
    main()