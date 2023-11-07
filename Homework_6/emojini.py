def read_emoji_file(file_name: str):
    emoji_dict = {'english_to_western': {},
                  'english_to_kaomoji': {},
                  'kaomoji_to_english': {},
                  'kaomoji_to_western': {},
                  'western_to_english': {},
                  'western_to_kaomoji': {},
                  }
    with open(file_name, 'r', encoding='utf-8') as file:
        next(file)  # Skip the metadata header
        for line in file:
            parts = line.strip().split()
            if len(parts) == 4:
                emoji_dict['english_to_western'][parts[1].lower()] = parts[2]
                emoji_dict['english_to_kaomoji'][parts[1].lower()] = parts[3]
                emoji_dict['kaomoji_to_english'][parts[3]] = parts[1]
                emoji_dict['western_to_english'][parts[2]] = parts[1]
    return emoji_dict

def parse_directives_file(file_name: str):
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
    words = source_text.split()
    translated_words = []

    for word in words:
        word_cleaned, prefix, suffix = strip_punctuation(word)
        if word_cleaned.lower() in emoji_dict[mode]:
            translated_word = prefix + emoji_dict[mode][word_cleaned.lower()] + suffix
        else:
            translated_word = word
        translated_words.append(translated_word)

    return ' '.join(translated_words)

def strip_punctuation(word: str):
    prefix, suffix = '', ''
    while word and not word[0].isalnum():
        prefix += word[0]
        word = word[1:]
    while word and not word[-1].isalnum():
        suffix = word[-1] + suffix
        word = word[:-1]
    return word, prefix, suffix

def write_to_file(translated_text: str, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(translated_text)

def batch_translate(emoji_file_name: str, directives_file_name: str):
    emoji_dict = read_emoji_file(emoji_file_name)
    translation_instructions = parse_directives_file(directives_file_name)

    for instruction in translation_instructions:
        with open(instruction['source_file'], 'r', encoding='utf-8') as file:
            source_text = file.read()

        translated_text = translate_text(source_text, emoji_dict, instruction['mode'])
        write_to_file(translated_text, instruction['output_file'])
        print(f"Processed {instruction['source_file']}: {instruction['mode'].replace(' ', ' -> ')}")

    print("All files processed.")

if __name__ == "__main__":
    batch_translate("emojis.txt", "emoji_directives.txt")
