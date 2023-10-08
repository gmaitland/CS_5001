'''
   CS5001
   HW 1
   Fall 2023
   09/18/2023
   Garfield Maitland
'''

def main():

    # Record the constants

    square_feet_to_square_meter = 0.092903
    cost_per_square_meter = 21.10
    
    # Ask for and save user input variables

    length = float(input("Enter the length of the office (in feet): "))
    width = float(input("Enter the width of the office (in feet): "))
    
    # Calculate rate (arithmetic)

    area_of_office_feet = length * width
    area_of_office_meters = area_of_office_feet * square_feet_to_square_meter
    total_cost_eurodollar = area_of_office_meters * cost_per_square_meter
    
    # Print message to user

    print(f"The area of the office is {area_of_office_feet:.2f} square feet")
    print(f"...which is {area_of_office_meters:.2f} square meters")
    print(f"......and you will pay €{total_cost_eurodollar:.2f} per month")

if __name__ == "__main__":
    main()
