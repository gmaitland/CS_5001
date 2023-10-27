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


word = "fri-yay"
for letter in word:
    print(letter)

lst = [4, 5, 6]
for num in lst:
    print(num)
"""
days = (mon, tue, wed, thurs, fri, sat, sun)
for day in days:
    print(day)
"""

lst = [3, 4, 5, 6, 7, 8, 9]
for num in lst:
    num = num + 10
    print(num)
# The lst is not mutated


# s = "abcde"
t = 0
while t < len(s):
    print(s[t])
    t += 1

main()
