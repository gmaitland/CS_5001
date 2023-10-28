"""
    CS 5001
    10/28/2023
    Align Online Module 6 - file_copy_version2.py
    Garfield Maitland
"""

"""
Module: Handing Exceptions

This file implements copying the poems file and modifying the lines
"Roses are red" to all upper-case.
"""


def main():
    input = open("poems.txt", "r")
    output = open("poems-copy.txt", "w")

    for line in input:
        if line.strip() == "Roses are red":
            output.write(line.upper())
        else:
            output.write(line)
    input.close()
    output.close()

"""
    for line in input:
        if line.strip() == "Roses are red":
            output.write(line.upper())
        else:
            output.write(line)
"""

"""
    I was able to read and write to a file. In other words I was able
    to manipulate data to complete a certain task outside of the
    pycharm application; this is really exciting times.
"""
main()
