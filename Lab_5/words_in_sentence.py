def frequency(words):
    word_count = []
    for each in words:
        if each in word_count:
            index = word_count.index(each)
            word_count[index + 1] = word_count[index + 1] + 1
        else:
            word_count = word_count + [each, 1]
    return word_count

def main():
    punctuation = '.?!;:,'
    sentence = input("Enter a sentence ")
    sentence = sentence.lower()
    words = sentence.split()
    print("You typed {} words in that sentence.".format(len(words)))
    print("Here are the individual words:")
    for i in range(len(words)):
        words[i] = words[i].strip(punctuation)
        print("{}.  {}".format(i, words[i]))
    print("The frequency of each word is: ")
    word_frequency = frequency(words)
    for i in range(0, len(word_frequency), 2):
        print("{} : {}".format(word_frequency[i], word_frequency[i+1]))

main()
