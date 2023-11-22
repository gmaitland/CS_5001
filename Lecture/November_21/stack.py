"""
    Garfield Maitland
    CS 5001
    11/14/2023
    Lecture - stack.py
"""


class Stack:
    """ Stack ADT """
    def __init__(self):
        self.items = []

    def push(self, element):
        self.items.append(element)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []


