"""
    Ice cream example
"""

"""
    Notes;
    if brocolli == "Y" or broccoli == "y":
    not equal. == is equivalence. Be very specific with your language
    if broccoli == ("Y" or "y"):
    will be evaluated to 'something' or 'True'. This takes on the form of
    the C language. Be careful when doing composites   
"""

def main():
    ice_cream = input("Do you like ice cream (y/n)? ")
    if ice_cream.lower() == "y":
        print("Yay! So do I!")
        
    broccoli = input("Do you like broccoli? y/n? ")
    if broccoli.lower() == "y":
        print("Yay! I like it with cheese. Cheddah!")
        
    if ice_cream.lower() == 'y' and broccoli.lower() == 'y':
        print("Yum! Broccoli Ice Cream Sundae coming your way now! Enjoy!")
    elif ice_cream.lower() == 'n' and broccoli.lower() == 'y':
        print("You are a healthy person.")
    elif ice_cream.lower() == 'y' and broccoli.lower() == 'n':
        print("But it is healthy for you.")
    elif ice_cream.lower() == 'n' and broccoli.lower() == 'n':
        print("Thanks for playing our game")

if __name__ == "__main__":
    main()
