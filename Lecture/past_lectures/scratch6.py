"""
    Evening coin toss game
"""

import random

# grandma = input("Are you heads or tails? ")
# heads = grandma

def flip_coin():
    """this function returns 'heads' or 'tails' from a random number"""
    # heads -> 0
    number = random.randint(0,1)
    if number == 0:
        return "HEADS! You win!"
    return "TAILS"

def print_report(heads, tails, visual):  
    print("Flip Coin Final Report")
    print(f"Flip History is: {visual}")
    print(f"Number of Heads = {heads} | Number of Tails = {tails}")

def game():
    heads = 0
    tails = 0
    visual = " "
    flag = True
    i = 0 # initial value of loop variable
    # while i < 20:
    while True:
        answer = flip_coin()
        if i == 10:
            i = i + 1
            flag = False
            continue
        visual = visual + answer + " "
        if answer == "HEADS":
            heads = heads + 1
        else:
            tails = tails + 1

        i += 1

    print_report(heads, tails, visual)

# if __name__ == "__main__":
def main():
    game()
