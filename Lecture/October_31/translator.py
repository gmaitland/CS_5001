"""
    Garfield Maitland
    CS 5001
    10/31/2023
    Lecture - translator.py
"""

# The english values are going to the key values for the french words
# hello ; bonjour

def build_dictionary(words, translation):
    logos = {}
    for index, value in enumerate(words):
        logos[value] = translation[index]
    return logos

def test_dictionary():
    english = ["hello", "goodbye", "thank you"]
    french = ["bonjour", "au revoir", "merci"]
    spanish = ["hola", "adios", "gracias"]

    translate = build_dictionary(english, spanish)
    word = input("Enter a word: ")
    word = word.lower()
    if word in translate: # is word a key in our dictionary?
        print(f"Translated word is {translate[word]}")
    else:
        print(f"Cannot translate {word}")



def main():
    """
    english = ["hello", "goodbye", "thank you"]
    french = ["bonjour", "au revoir", "merci"]
    spanish = ["hola", "adios", "gracias"]

    translator = [english, french, spanish]

    word = input("Enter a word in English: ")
    word = word.lower()

    if word in translator[0]:
        index = translator[0].index(word)
        print(f"Translated word is {translator[1][index]} in French")
        print(f"Translated word is {translator[2][index]} in Spanish")
    else:
        print(f"Cannot translate {word}")

    print("Done")
    """
    test_dictionary()
    print("Done")
if __name__ == "__main__":
    main()


