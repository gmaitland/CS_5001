"""
    Garfield Maitland
    CS 5001
    11/21/2023
    Lecture - Queue.py
"""

# Manually creating queue functions
# They have constant time access
# Decks have constant time access

# For some reason, these have to have a capital 1st letter file name


class Queue:
    """
        Queue class First In First Out (FIFO)
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, element):     # append the end of the list
        return self.items.append(element)

    def dequeue(self):
        return self.items.pop(0)

    def front(self):
        return self.items[0]

    def back(self):
        return self.items[-1]

