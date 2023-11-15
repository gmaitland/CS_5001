"""
    Garfield Maitland
    CS 5001
    11/14/2023
    Lecture - testCircle.py
"""

from Stack import Stack

def main():
    s = Stack()

    s.push(1)
    s.push(2)
    s.push("Hello World")
    s.push("CS5001 Rocks!")

    print(s.peek())

    while not s.is_empty():
        print(s.pop())

    print("Done")


if __name__ == "__main__":
    main()