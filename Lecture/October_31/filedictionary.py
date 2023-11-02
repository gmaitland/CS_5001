"""
    Garfield Maitland
    CS 5001
    10/31/2023
    Lecture - filedictionary.py
"""

# Can do localization of code, it is a common thing to do

'''
for stuff in dict:
    print(stuff)
'''

dict = {"a": "letter", "1": "number", "'": "punctuation"}
i = 2
while i < len(dict):
    print(dict[i])
    i += 1

def load_dictionary(file_name):
    with open(file_name, mode="r") as in_file:
        logos = {}

        for each in in_file:
            each = each.strip("\n")
            english, french, spanish = each.split(",")
            logos[english] = [french, spanish]

        return logos

def test_file_dictionary():
    translate = load_dictionary("words.txt")
    word = input("Enter a word: ")
    word = word.lower()
    if word in translate:
        print(f"Translated word is: {translate[word][0]} in French")
        print(f"Translated word is: {translate[word][1]} in Spanish")
    else:
        print(f"Cannot translate {word}")

def main():
    test_file_dictionary()


if __name__ == "__main__":
    main()