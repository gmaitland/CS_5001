ENGLISH = ['hello', 'friend', 'hey', 'awful', 'wow','reward', 'song', 'money',
           'board', 'cocktail', 'bathroom', 'friends', 'cheat', 'flag','boy',
           'girl', 'my', 'take', 'sink', 'telescope', 'clean', 'you']
PIRATE = ['ahoy', 'matey', 'avast', 'bilge-sucking', 'blimey', 'booty', 'chanty',
          'dubloon', 'plank', 'grogg', 'head', 'hearties', 'hornswaggle',
          'jack', 'lad', 'lass', 'me', 'plunder', 'scuttle', 'spyglass', 'swob',
          'ye']

STOPWORD = 'arr'

def convert_to_dictionary(lst1, lst2):
    ''' Function convert_to_dictionary
        Params: list of words (unique), list of translated words
        Returns: a dictionary where element from lst1 is key and lst2 is value
    '''
    dictionary = {}
    for i in range(len(ENGLISH)):
        dictionary[ENGLISH[i]] = PIRATE[i]
    return dictionary

def translate(english_word, dictionary):
    ''' Function translate
        Param: english word (a string)
        Returns: pirate equivalent, also a string
    '''
    english_word = english_word.lower()
    if english_word in dictionary:
        return dictionary[english_word]
    return english_word


def main():
    translator = convert_to_dictionary(ENGLISH, PIRATE)

    print("Arrrrr welcome to me pirate dictionary!")
    while True:
        english = input("Type some stuff, then hit enter with yer sword.\n"
                    "Or just say 'arr' to be done, ya scalliwag.\n")

        if english == STOPWORD:
            break

        english_lst = english.split()
        pirate = ""
        for word in english_lst:
            pirate += translate(word, translator)
            pirate += " "

        print(pirate, "\n")

main()
    
          


