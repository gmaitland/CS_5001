'''
    CS5001 - Fall 2023
    Christian Rogerson & Garfield Maitland
    Simple Program with Games of Chance
'''
# import modules
import random

def toss_coin():
    '''
        Return the result of a coin toss
    '''
    return random.randint(0,1)

def print_outcomes(outcome):
    '''
        Print outcomes of random events
    '''
    print(f"The outcome is: {outcome}")

def main():
    # get random events
    coin_toss = random.randint(0,1)
    random_float = random.uniform(1, 10)
    print(random_float)

    # turn random events into words

    # print the outcomes
    # print(f"Coin toss resul: {coin_toss}")
    # print("Coin toss result: ", coin_toss)
    

if __name__ == "__main__":
    main()
