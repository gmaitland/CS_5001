'''
   CS5001
   Lab 1 - Car Expense
   Fall 2023
   Garfield Maitland
'''

def main():

    # Write the constants for the program
    
    INSURANCE_COST = 1600 # Annualy
    
    # Write the variables here

    miles_driven = int(input("How many miles do you drive per month? "))
    fuel_efficiency = int(input("What is your car's fuel efficiency? "))
    gallon_of_gas_cost = float(input("What is the average price of a gallon of gas? "))
    
    MAINTENANCE_COST = miles_driven * 0.005
    FUEL_COST = (miles_driven / fuel_efficiency) * gallon_of_gas_cost
    
    # Write the total here

    total_cost = (INSURANCE_COST / 12) + MAINTENANCE_COST + FUEL_COST # Monthly

    # Write the print statements here

    print(f"Your total expense per month is ${total_cost:.2f}")


    
    '''
    my_number = int(input("Enter a number: "))
    print("The next number is", my_number + 1)
    '''
    
if __name__ == "__main__":
    main()
