"""
    Piggly Wiggly
"""


# For collection of data use a while loop
# We haven't covered the for loop yet
# Will cover sets and dictionaries and maybe tuples
# The math is so important for internalizing the programming content
# And application


def main():
    food = ["grapes", "apples", "snickers"] # 1st list

    user_food = [] # 2nd list

    item = input("What food item do you want (stop to end)? ")
    while item.upper() != "STOP": # This is how we exit the loop
        user_food += [item]
        item = input("Next food item (stop to end)? ")

    print(user_food) # Asks to print the user food list

    i = 0 # This is our running variable
    while i < len(user_food): # Comparison portion of the function
        if user_food[i].lower() in food:
            print(f"I'm shopping for {user_food[i]} too!")
        i = i + 1
         
 
if __name__ == "__main__":
    main()
