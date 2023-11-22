"""
    Garfield Maitland
    CS 5001
    11/21/2023
    Practice - a_function_as_an_object.py
"""


def binary_stack(digits):
    s = Stack()     # create the stack
    for each in digits:
        s.push(each)

    value = 0
    index = 0

    while not s.is_empty():
        value = value + int(s.pop()) * 2 ** index
        index += 1

    return value


def main():
    print("001", )


if __name__ == "__main__":
    main()