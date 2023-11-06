"""
    CS 5001
    11/06/2023
    Homework 6 - emojini.py
    Garfield Maitland
"""


def read_emoji_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    metadata = lines[0].strip().split()
    emoji_dict = {metadata[i]: {} for i in range(1, len(metadata))}
    for line in lines[1:]:
        parts = line.strip().split()
        for i in range(1, len(metadata)):
            emoji_dict[metadata[i]][parts[0]] = parts[i]
    return emoji_dict


def translate_line(line, word_dict):
    translated_line = ''
    word_start = 0

    for i, char in enumerate(line):
        if char in ' \n\t.,!?()"-':
            if word_start < i:
                word = line[word_start:i]
                translated_line += word_dict.get(word, word)
            translated_line += char
            word_start = i + 1

    # Add the last word if the line doesn't end with a punctuation mark
    if word_start < len(line):
        word = line[word_start:]
        translated_line += word_dict.get(word, word)

    return translated_line


def batch_translate(emoji_file_name, directives_file_name):
    emoji_dict = read_emoji_file(emoji_file_name)

    try:
        with open(directives_file_name, 'r') as directives_file:
            for line in directives_file:
                source_lang, target_lang, source_file_name, target_file_name = line.strip().split()

                # Depending on the direction of translation, the word dictionary may differ
                if source_lang != 'english':
                    word_dict = {v: k for k, v in emoji_dict[source_lang].items()}
                else:
                    word_dict = emoji_dict[target_lang]

                try:
                    with open(source_file_name, 'r') as source_file, open(target_file_name, 'w') as target_file:
                        for line in source_file:
                            translated_line = translate_line(line, word_dict)
                            target_file.write(translated_line)
                except FileNotFoundError:
                    print(f"Error: The file {source_file_name} does not exist.")
                except Exception as e:
                    print(f"An error occurred while processing the file {source_file_name}: {e}")

                print(f"Processing {source_file_name}: {source_lang} -> {target_lang}")
    except FileNotFoundError:
        print(f"Error: The directives file {directives_file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the directives file: {e}")

    print("done")

# To use the function, simply call it with the names of your emoji and directives files:
# batch_translate('emojis.txt', 'emoji_directives.txt')
