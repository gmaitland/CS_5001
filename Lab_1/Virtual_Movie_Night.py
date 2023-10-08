'''
   CS5001
   Lab 1 - Virtual Movie Night
   Fall 2023
   Garfield Maitland
'''

def main():

    # Write the constants for the program
    
    TICKET_COST = 7.95
    SNACK_COST = 8.95
    DRINK_COST = 4.25

    LOYALTY_DISCOUNT = 0.9

    # Ask for the user input
    
    tickets = int(input("How many tickets are you buying? "))
    snacks = int(input("How many snacks are you buying? "))
    drinks = int(input("How many drinks are you buying? "))
    
    # Compute the total cost

    total_cost = TICKET_COST + SNACK_COST + DRINK_COST

    #Print the value

    print(f"Total cost is ${total_cost}")
    print(f"Your price after the discount is: ${LOYALTY_DISCOUNT*total_cost:.2f}")
    
if __name__ == "__main__":
    main()










    
