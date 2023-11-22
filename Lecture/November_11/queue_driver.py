"""
    Garfield Maitland
    CS 5001
    11/21/2023
    Lecture - queue_driver.py
"""

from queue import Queue


def main():
    q = Queue()
    """
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(5)
    """
    # q.enqueue("Hello World")

    print(q.back())
    print(q.front())
    print("--------\n")

    while not q.is_empty():
        print(q.dequeue())

    print("Done")


if __name__ == "__main__":
    main()