"""
    Garfield Maitland
    CS 5001
    11/21/2023
    Lecture - protocol.py
"""

from square import Square
from circle import Circle
from queue import Queue


def main():
    q = Queue()
    q.enqueue(Square(1))
    q.enqueue(Square(2))
    q.enqueue(Cricle(1))
    q.enqueue(Square(5))

    print(q.front())
    print(q.back())

    print("------------\n")

    while not q.is_empty():
        print(q.front())
        print(q.dequeue().get.area())

    print("Done")


if __name__ == "__main__":
    main()