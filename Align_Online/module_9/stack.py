"""
    Garfield Maitland
    CS 5001
    11/21/2023
    Practice - stack.py
"""

"""
    This user-defined data structure is called the stack.
    It has basic operations push, pop, is_empty, top
    It also runs in constant time, which is faster than
    some list operations.
"""


class Stack:
    def __init__(self):
        self.mystack = []

    def push(self, element):
        self.mystack.append(element)

    def pop(self):
        return self.mystack.pop()

    def is_empty(self):
        return not self.mystack

    def peek(self):  # aka top()
        if self.mystack:
            return self.mystack[-1]
        return None


def main():
    # mystack =
    print("Need to check the implementation later")


if __name__ == "__main__":
    main()
