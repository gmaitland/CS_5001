"""
    CS 5001
    10/28/2023
    Align Online Module 6 - file_copy_version1.py
    Garfield Maitland
"""

"""
Module: Handing Exceptions

This file implements copying the poems file
"""


def main():
    input = open("poems.txt")
    content = input.read()
    input.close()



    input_2 = open("written.txt")
    content_2 = input_2.read()
    input_2.close()

    print(content_2)




    input = open("poems.txt")
    content = input.read()
    input.close()

    print(content)

    output = open("poems-copy.txt", "w")
    output.write(content)
    output.close()


main()
