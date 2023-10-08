'''
   CS5001
   HW 1
   Fall 2023
   09/18/2023
   Garfield Maitland
'''
    # Record the constants
SQUARE_FEET_TO_SQUARE_METER = 0.092903
COST_PER_SQUARE_METER = 21.10
    
def main():
    
    # Ask for and save user input variables
    length_office_feet = float(input("Enter the length of the office (in feet): "))
    width_office_feet = float(input("Enter the width of the office (in feet): "))
    
    # Calculate rate (arithmetic)
    area_of_office_feet = length_office_feet * width_office_feet
    area_of_office_meters = area_of_office_feet * SQUARE_FEET_TO_SQUARE_METER
    total_cost_eurodollar = area_of_office_meters * COST_PER_SQUARE_METER
    
    # Print message to user
    print(f"The area of the office is {area_of_office_feet:.2f} square feet")
    print(f"...which is {area_of_office_meters:.2f} square meters")
    print(f"......and you will pay €{total_cost_eurodollar:.2f} per month")

if __name__ == "__main__":
    main()
