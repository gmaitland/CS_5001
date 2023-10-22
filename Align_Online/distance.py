"""
    CS 5001
    10/22/2023
    Align Online Module 2 - distance.py
    Garfield Maitland
"""

def euclidean(x1, y1, x2, y2):
    """
        Function euclidean
        Parameters: four floats, representing two points
        Returns: a float, the distance between the two points
    """
    x_diff = (x2 - x1) ** 2
    y_diff = (y2 - y1) ** 2
    dist = (x_diff + y_diff) ** 0.5
    return dist


"""

def main():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    dist = euclidean(x1, y1, x2, y2)
    print(f'The euclidean distance is, {dist}')


main()

"""

"""
    We created 4 variables that prompt the user for 
    assignment and then we mapped the euclidean function
    return value to the dist variable. Then we print created
    a print line to display the values to the console
"""
