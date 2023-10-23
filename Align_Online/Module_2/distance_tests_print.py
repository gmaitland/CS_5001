"""
    CS 5001
    10/22/2023
    Align Online Module 2 - distance_tests_print.py
    Garfield Maitland
"""

"""
    We are going to call the euclidian function from the
    distance.py file. Then we are going to implement some tests,
    approximately 4 of them. But prior to implementing the
    tests function calls in the main, we need to first create a
    test_euclidean function that serves as the constructor
    and that allows us to set up tests arguments.
"""

from distance import euclidean

def test_euclidean(x1, y1, x2, y2, expected):
    """
        Function test_euclidean
        Params: two points (floats)
        Return: nothing, just print actual vs expected
    """
    print("Testing points", x1, y1, x2, y2)
    actual = euclidean(x1, y1, x2, y2)
    print("\tExpected......", expected)
    print("\tActual........", actual)

def main():
    # test 1
    test_euclidean(0, 0, 0, 0, 0.0)

    # test 2
    test_euclidean(2, -1, -2, 2, 5.0)

    # test 3
    test_euclidean(0, 0, 1, 1, 1.414)

    # test 4
    test_euclidean(-5.2, 3.8, -13.4, 0.2, 8.955)

main()


"""
    Moving forward, a way to improve would be to use a
    conditional boolean statement to determine whether
    or file and it's test cases pass
"""






