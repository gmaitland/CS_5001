"""
    CS 5001
    11/06/2023
    Homework 6 - emojini.py
    Garfield Maitland
"""

import re


def parse_emoji_file(emoji_file_name):
    with open(emoji_file_name, 'r', encoding='utf-8') as file:
        headers = file.readline().strip().split('\t')
        emoji_map = {header: {} for header in headers[1:]}  # skip METADATA

        for line in file:
            data = line.strip().split('\t')
            for i, header in enumerate(headers[1:], 1):  # skip METADATA
                emoji_map[header][data[0].lower()] = data[i]

    return emoji_map


def read_directive_file(directives_file_name):
    with open(directives_file_name, 'r', encoding='utf-8') as file:
        directives = [line.strip().split() for line in file]
    return directives


def transform_text(mapping, text, direction):
    words = text.split()
    transformed_words = []

    for word in words:
        # Retain punctuation
        base_word = re.sub(r'[\W_]', '', word)
        punctuation = re.sub(r'\w', '', word)
        key = base_word.lower()

        if direction == 'english':
            transformed_word = mapping.get(key, base_word)
        else:  # assume direction is either 'western' or 'kaomoji'
            reverse_map = {v: k for k, v in mapping.items()}
            transformed_word = reverse_map.get(key, base_word)

        transformed_words.append(transformed_word + punctuation)

    return ' '.join(transformed_words)


def write_output_file(output_file_name, transformed_text):
    with open(output_file_name, 'w', encoding='utf-8') as file:
        file.write(transformed_text)


def batch_translate(emoji_file_name, directives_file_name):
    try:
        emoji_map = parse_emoji_file(emoji_file_name)
        directives = read_directive_file(directives_file_name)

        for directive in directives:
            source_lang, target_lang, input_file, output_file = directive
            with open(input_file, 'r', encoding='utf-8') as file:
                text = file.read()

            mapping = emoji_map[target_lang.upper()] if target_lang != 'english' else emoji_map[source_lang.upper()]
            transformed_text = transform_text(mapping, text, source_lang)
            write_output_file(output_file, transformed_text)

        print('Processing completed.')
    except FileNotFoundError as e:
        print(f"Error: The file {e.filename} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    # Example of running batch_translate with the provided files.
    # In practice, you might want to accept these as command-line arguments or from user input.
    batch_translate('emojis.txt', 'emoji_directives.txt')


if __name__ == "__main__":
    main()
