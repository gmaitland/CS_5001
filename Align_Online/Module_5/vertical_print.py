"""
    CS 5001
    10/27/2023
    Align Online Module 5 - vertical_print.py
    Garfield Maitland
"""


def main():
    word = input("Enter word: ")
    index = 0
    while index < len(word):
        print(word[index])
        print(f" This is the word's {word[index]}")
        index += 1


main()
