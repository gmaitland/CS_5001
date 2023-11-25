"""
    Garfield Maitland
    CS 5001
    11/23/2023
    Practice - recursion_practice.py
"""

"""
    The else codeblock conditional statement calls itself recursively
    until it reaches the the base case which in this instances is the
    if codeblock conditional statement
"""


def mystery(n):
    if n < 0:
        return 2 * n
    else:
        return mystery(n - 1) + n


def main():
    """
    print(mystery(-1))
    print(mystery(0))
    print(mystery(1))
    print(mystery(2))
    print(mystery(3))
    """
    print(mystery(4))
    print(mystery(77))
    print(mystery(100))
    print(mystery(7))
    print(mystery(12))


if __name__ == "__main__":
    main()
