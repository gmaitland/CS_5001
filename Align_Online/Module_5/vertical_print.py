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
s = input("Please enter a word:")
t = 0
while t < len(s):
    print(s[t])
    t += 1

# Reviewed while and for loops from yesterday

pets = ["bird", "cat", "dog", "fish"]
i = 0
while i < len(pets):
    print(pets[i])

    j = 0
    while j < len(pets[i]):
        print(pets[i][j])
        j += 1
    i += 1


a = "Road"
for letter in a:
    print(letter)

"""
    While loops typically have 5 lines of code. The sequence/list/array/string
    to be iterated/looped over, the variable index value that will be updated,
    the conditional statement that is designed to be false and using methods
    like .len(), the print() statement to print a value to the console, and
    finally the update statement to increment the index variable value, so that
    we can iterate to the next element within the list.
"""

main()
