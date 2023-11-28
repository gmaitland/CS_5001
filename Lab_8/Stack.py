'''
    CS5001
    Fall 2020
    Our user-defined data structure: the Stack
    Has basic operations push, pop, is_empty, top
    Each runs in constant time, faster than some list operations.
'''

class Stack:
    def __init__(self):
        self.mystack = []

    def push(self, element):
        self.mystack.append(element)

    def pop(self):
        return self.mystack.pop()

    def is_empty(self):
        return not self.mystack

    def peek(self): # aka top()
        if self.mystack:
            return self.mystack[-1] 
        return None

