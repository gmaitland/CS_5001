'''
   CS5001
   HW 1
   Fall 2023
   09/18/2023
   Garfield Maitland
'''
def main():
    # Ask for and save user input variables
    supplier_fee = float(input("What is the supplier fee per kwh? "))
    power_fee = float(input("What is the power fee per kWh? "))
    kwh_used = float(input("How many kWh were used this month? "))
    # Calculate rate
    total_electric_bill = (supplier_fee + power_fee) * kwh_used
    # Print message to user
    print(f"Your electric bill this month is ${total_electric_bill:.2f}")
if __name__ == "__main__":
    main()
