
from music import PLAYLIST, SONGS


def substitute(song: list, old_word: str, new_word: str) -> bool:
    punctuation = ".?!:,"
    song_str = " ".join(song)

    # If the word to be replaced is not in the song, return False
    if old_word not in song_str:
        return False

    # Replace the old word with the new word in the song
    song_str = song_str.replace(old_word, new_word)

    # Strip out the punctuation
    for char in punctuation:
        song_str = song_str.replace(char, "")

    # Update the song list
    song[:] = song_str.split()
    return True


def reverse_it(song: list) -> list:
    punctuation = ".?!:,"

    # Convert the song list to a string and strip out punctuation
    song_str = " ".join(song)
    for char in punctuation:
        song_str = song_str.replace(char, "")

    # Reverse the words and update the song list
    reversed_words = song_str.split()[::-1]
    song[:] = reversed_words
    return song


def load_song(selection: int) -> list:
    # Convert user selection to index for list access
    index = selection - 1

    # Check if the selection is valid
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
            selection = int(input("Select a song by number (1 for the first song, etc.): "))
            loaded = load_song(selection)
            if loaded:
                current_song = loaded[0].copy()
                print(f"You are mixing the song: {loaded[1]}")
            else:
                print("Invalid selection!")

        elif choice == 'T':
            if current_song:
                print(f"Current song title: {loaded[1]}")
            else:
                print("No song loaded!")

        elif choice == 'S':
            old_word = input("What word do you want to replace in the existing song? ")
            new_word = input("What new word do you want to use for the song? ")
            if not substitute(current_song, old_word, new_word):
                print(f"'{old_word}' not found in the song!")

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
