"""
    CS 5001
    10/23/2023
    Align Online Module 4 - matrix_print.py
    Garfield Maitland
"""

"""
    A matrix is a 2 dimensional array. This can be very useful
    for certain applications. A matrix is also known as a list
    of lists. 
"""

def main():
    grades = [
        [98, 88, 89, 97, 78],
        [99, 85, 92, 74, 96],
        [77, 81, 69, 82, 84],
        [95, 79, 69, 76, 87]]
    print(grades)

    print("The grades are:")
    row = 0 # 1st counter initialization
    while row < len(grades): # unknown list value, and conditional
        col = 0 # 2nd counter initialization
        while col < len(grades[row]): # conditional of the unknown list value
            print(grades[row][col], end="\t")
            col += 1 # update statement
        print("Almost done!")
        row += 1 # update statement
    print("Done!")


main()