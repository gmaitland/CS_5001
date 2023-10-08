import random

# Function to get the Pokémon name based on the numbering scheme
def get_player(num):
    pokemon_names = [
        "Bulbasaur", "Charmander", "Butterfree", "Rattata", "Weedle",
        "Pikachu", "Sandslash", "Jigglypuff", "Raichu", "Diglett"
    ]
    if 1 <= num <= len(pokemon_names):
        return pokemon_names[num - 1]
    else:
        return "Diglett"

# Function to determine the winner of an RPS battle
def check_battle(computer, player):
    if computer == player:
        return "DRAW!"
    elif (computer == 1 and player == 3) or (computer == 2 and player == 1) or (computer == 3 and player == 2):
        return "COMPUTER"
    else:
        return "PLAYER"

# Main game logic
def main():
    red_score = 0
    blue_score = 0

    print("What team do you want (red or blue)?")
    team = input().strip().lower()

    while True:
        red_pokemon = get_player(random.randint(1, 10))
        blue_pokemon = get_player(random.randint(1, 10))

        print(f"RED pokemon {red_pokemon} vs. BLUE pokemon {blue_pokemon}")
        print("Enter 1 for Rock, 2 for Paper, 3 for Scissors")
        player_choice = int(input().strip())

        computer_choice = random.randint(1, 3)

        print(f"{red_pokemon} played {['ROCK', 'PAPER', 'SCISSORS'][player_choice - 1]}. {blue_pokemon} played {['ROCK', 'PAPER', 'SCISSORS'][computer_choice - 1]}")

        result = check_battle(computer_choice, player_choice)

        if result == "DRAW!":
            print("It's a draw! No winner")
        elif result == "COMPUTER":
            print(f"BLUE team wins with {blue_pokemon}!")
            blue_score += 1
        else:
            print(f"RED team wins with {red_pokemon}!")
            red_score += 1

        print("Play again (y/n)?")
        play_again = input().strip().lower()

        if play_again != 'y':
            break

    print("Tournament has ended!\n")
    print(f"RED team: {red_score}\nBLUE team: {blue_score}")

    if red_score > blue_score:
        print("RED team wins!")
    elif blue_score > red_score:
        print("BLUE team wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
def main():
  play() 

if __name__ == "__main__":
  main()    """
    Function: black_or_white()
        If both the column & row are even then we know the square is BLACK
        If both the column & row are odd then we know the square is BLACK
        If the column and row are not the same we know the square is WHITE

    Parameters:
        row int: Is an int that represents the selected hex value.
        column int: Is an int that represents the selected hex value.

    Preconditions:
        None

    Returns:
        BLACK if both column and row are even
        BLACK if both column and row are odd
        WHITE if one or the other is even and odd
    """    """
    Function: check_battle()
        Creates the logic for the win condition to determine if either the
        computer choice or the player choice wins the battle.

    Parameters:
        computer_choice int: A value between 1 and 3 inclusive that represents
        rock, paper, or scissors.
        player_choice int: A value between 1 and 3 inclusive that represents
        rock, paper, or scissors.

    Preconditions:
        None

    Returns:
        DRAW! or COMPUTER or PLAYER
    """https://piazza.com/class/lm0ya0hzoty3iy/post/64https://piazza.com/class/lm0ya0hzoty3iy/post/64https://piazza.com/class/lm0ya0hzoty3iy/post/64
