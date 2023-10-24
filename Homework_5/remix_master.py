"""
    CS 5001
    10/24/2023
    Homework 5 - remix_master.py
    Garfield Maitland
"""


from music import PLAYLIST, SONGS


def substitute(song: list, old_word: str, new_word: str) -> bool:
    """
    Function: substitute()
        Replaces the old word with the neww word in the song. If the old word,
        is not in the song, then the function returns a boolean value false.
        Furthermore, the function strips the songs punctuation and updates
        the song list.

    Parameters:
        song (type: str)
        old_word (type: str)

    Returns:
        bool

    Defense:
        None
    """
    punctuation = ".?!:,"
    song_str = " ".join(song)

    if old_word not in song_str:
        return False

    song_str = song_str.replace(old_word, new_word)

    for char in punctuation:
        song_str = song_str.replace(char, "")

    song[:] = song_str.split()
    return True


def reverse_it(song: list) -> list:
    """
    Function: reverse_it()
        Converts the song list into a string and strips out the punctuation.
        Additionally, it reverses the words of the song and updates the
        song list accordingly.

    Parameters:
        song (type: list)

    Returns:
        list

    Defense:
        None
    """
    punctuation = ".?!:,"

    song_str = " ".join(song)
    for char in punctuation:
        song_str = song_str.replace(char, "")

    reversed_words = song_str.split()[::-1]
    song[:] = reversed_words
    return song


def load_song(selection: int) -> list:
    """
    Function: load_song()
        Converts the user selection to an index for list access and also
        checks if the user selection is a valid input.

    Parameters:
        load_song(type: int)

    Returns:
        list

    Defense:
        None
    """
    index = selection - 1

    if 0 <= index < len(PLAYLIST):
        return [SONGS[index], PLAYLIST[index]]
    else:
        return []


def main():
    current_song = []
    while True:
        print("ReMix-Master:")
        print("L: Load a different song")
        print("T: Title of current song")
        print("S: Substitute a word")
        print("P: Playback your song")
        print("R: Reverse it!")
        print("X: Reset to original song")
        print("Q: Quit?")
        choice = input("Your choice: ").upper()

        if choice == 'L':
            selection = int(input("Select a song by SONG #: "))
            loaded = load_song(selection)
            if loaded:
                current_song = loaded[0].copy()
                print(f"You are mixing the song: {loaded[1]}")
            else:
                print("Invalid selection!")

        elif choice == 'T':
            if current_song:
                print(f"The current song title is: {loaded[1]}")
            else:
                print("No song loaded!")

        elif choice == 'S':
            old_word = input("What word do you want to replace in the song? ")
            new_word = input("What new word do you want to use for the song? ")
            if not substitute(current_song, old_word, new_word):
                print(f"'The word {old_word}' is not found in the song!")

        elif choice == 'P':
            print(" ".join(current_song))

        elif choice == 'R':
            reverse_it(current_song)

        elif choice == 'X':
            current_song = loaded[0].copy()

        elif choice == 'Q':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
