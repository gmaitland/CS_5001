
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
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
