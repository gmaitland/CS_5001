"""
    CS 5001
    11/06/2023
    Homework 6 - emojini.py
    Garfield Maitland
"""


def read_emoji_file(file_name: str):
    """
    Function: read_emoji_file()
        Reads the emoji file and creates the mappings

    Parameters:
        file_name (type: str)

    Returns:
        emoji_dict

    Defense:
        none
    """
    emoji_dict = {'english_to_western': {},
                  'english_to_kaomoji': {},
                  'kaomoji_to_english': {},
                  'kaomoji_to_western': {},
                  'western_to_english': {},
                  'western_to_kaomoji': {},
                  }
    with open(file_name, 'r', encoding='utf-8') as file:
        next(file)  # Skip the metadata header
        # Each line will have english, western, kaomoji
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                english, western, kaomoji = parts
                emoji_dict['english_to_western'][english.lower()] = western
                emoji_dict['english_to_kaomoji'][english.lower()] = kaomoji
                emoji_dict['kaomoji_to_english'][kaomoji.lower()] = english
                emoji_dict['kaomoji_to_western'][kaomoji.lower()] = western
                emoji_dict['western_to_english'][western.lower()] = english
                emoji_dict['western_to_kaomoji'][western.lower()] = kaomoji
    return emoji_dict


def parse_directives_file(file_name: str):
    """
    Function: parse_directives_file()
        Parses the directives file to see what to read/ write

    Parameters:
        file_name (type: str)

    Returns:
        instructions

    Defense:
        none
    """
    instructions = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 4:
                instruction = {
                    'mode': f"{parts[0]}_to_{parts[1]}",
                    'source_file': parts[2],
                    'output_file': parts[3]
                }
                instructions.append(instruction)
    return instructions


def translate_text(source_text: str, emoji_dict: dict, mode: str):
    """
    Function: translate_text()
        Translates the text into the appropriate language mapping

    Parameters:
        source_text (type: str)
        emoji_dict (type: dict)
        mode (type: str)

    Returns:
        ' '.join(translated_words)

    Defense:
        none
    """
    words = source_text.split()
    translated_words = []
    # print(emoji_dict)
    for word in words:
        word_cleaned, prefix, suffix = strip_punctuation(word)
        # print(word_cleaned)
        if word_cleaned.lower() in emoji_dict[mode]:
            translated_word = (prefix +
                               emoji_dict[mode][word_cleaned.lower()] + suffix)
        else:
            translated_word = word
        translated_words.append(translated_word)

    return ' '.join(translated_words)
    # Word may not be getting identified.


def strip_punctuation(word: str):
    """
    Function: strip_punctuation()
        Removes the appropriate punctuation

    Parameters:
        word (type: str)

    Returns:
        word, prefix, suffix

    Defense:
        none
    """
    prefix, suffix = '', ''
    while word and not word[0].isalnum():
        prefix += word[0]
        word = word[1:]
    while word and not word[-1].isalnum():
        suffix = word[-1] + suffix
        word = word[:-1]
    return word, prefix, suffix


def write_to_file(translated_text: str, file_name: str):
    """
    Function: write_to_file()
        Writes details to a file.

    Parameters:
        translated_text (type: str)
        file_name (type: str)

    Returns:
        none

    Defense:
        none
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(translated_text)


def batch_translate(emoji_file_name: str, directives_file_name: str):
    """
    Function: batch_translate()
        Translates multiple files from a single call

    Parameters:
        emoji_file (type: str)
        directives_file_name (type: str)

    Returns:
        none

    Defense:
        try / except blocks
    """
    try:
        emoji_dict = read_emoji_file(emoji_file_name)
        if not emoji_dict:
            print("Failed to load emoji mappings. Exiting.")
            return

        translation_instructions = parse_directives_file(directives_file_name)
        if not translation_instructions:
            print("Failed to load translation instructions. Exiting.")
            return

        for instruction in translation_instructions:
            try:
                with open(instruction['source_file'],
                          'r', encoding='utf-8') as file:
                    source_text = file.read()
                translated_text = translate_text(source_text,
                                                 emoji_dict,
                                                 instruction['mode'])
                write_to_file(translated_text, instruction['output_file'])
                print(f"Processed {instruction['source_file']}:"
                      f" {instruction['mode'].replace('_', ' -> ')}")
            except FileNotFoundError:
                print(f"The source file "
                      f"{instruction['source_file']} was not found.")
            except IOError as e:
                print(f"An I/O error occurred: {e}")
            except Exception as e:
                print(f"An error occurred during processing: {e}")

        print("All files processed.")
    except Exception as e:
        print(f"An unexpected error occurred during batch processing: {e}")

    print("All files processed.")


if __name__ == "__main__":
    batch_translate("emojis.txt", "emoji_directives.txt")
