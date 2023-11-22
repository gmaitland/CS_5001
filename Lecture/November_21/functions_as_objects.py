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


def apply_lambda(lst, a_function):
    out = []
    for item in lst:
        out.append(a_function(item))
    return out


def reduce_to_single_value(lst, a_function, initial_value=0):
    result = initial_value
    for item in lst:
        result = a_function(result, item)
    return result



def main():
    a = [1, 2, 3, 4, 5]
    b = apply_to_all(a, multiply, 5)
    c = apply_to_all(a, subtract, 2)
    print(a)
    print(b)
    print(c)

    print("------------\n")

    d = apply_lambda(a, lambda x: x * 10)   # This is the lambda expression
    print(d)

    print("-------> fold/reduce <--------")
    print(reduce_to_single_value(a, (lambda x,y: x + y), 0))
    print(reduce_to_single_value(b, (lambda x, y: x + y), 0))
    print(reduce_to_single_value(c, (lambda x, y: x + y), 0))
    print(reduce_to_single_value(["Hello ", "World", "!"], (lambda x, y: x + y), ""))


if __name__ == "__main__":
    main()