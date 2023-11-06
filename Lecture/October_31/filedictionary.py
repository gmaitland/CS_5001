"""
    Garfield Maitland
    CS 5001
    10/31/2023
    Lecture - filedictionary.py
"""

# Can do localization of code, it is a common thing to do

dict_1 = {"a": "letter", "1": "number", "'": "punctuation"}
'''
for stuff in dict:
    print(stuff)
'''
dict_1_for_while_loop = list(dict_1.items())

i = 0
while i < len(dict_1_for_while_loop):
    print(dict_1_for_while_loop[i])
    i += 1

new_list = ["I work hard", "I do my best", "This is what we do"]
"""
for phrases in new_list:
    print(new_list[phrases])
 """
phrases = 0
while phrases < len(new_list):
    print(new_list[phrases])
    phrases += 2
    # phrases = 1

for items in range(2, 100, 5):
    print(items)

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
