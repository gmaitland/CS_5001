'''
   CS5001
   HW 1
   Fall 2023
   09/18/2023
   Garfield Maitland
'''
'''
Test case #1:
Input: $1000
Output: 20 fifties, 0 twenties, 0 tens, 0 fives, 0 ones
Test case #2:
Input: $80
Output: 1 fifty, 1 twenty, 1 ten, 0 fives, 0 ones
Test case #3:
Input: $1
Output: 0 fifties, 0 twenties, 0 tens, 0 fives, 1 one
'''
FIFTY = 50
TWENTY = 20
TEN = 10
FIVE = 5
ONE = 1
def main():
    # Welcome statement / ask for and save user input variables
    withdraw_amount = int(input("Welcome to PDQ Bank! Amount to withdraw? $ "))
    print(f"Cha-ching! You asked for $ {withdraw_amount}")
    # Arithmetic
    fifties = withdraw_amount // FIFTY
    twenties = (withdraw_amount % FIFTY) // TWENTY
    tens = ((withdraw_amount % FIFTY) % TWENTY) // TEN
    fives = (((withdraw_amount % FIFTY) % TWENTY) % TEN) // FIVE
    ones = (((withdraw_amount % FIFTY) % TWENTY) % TEN) % FIVE
    # Print values
    print("That breaks down to:\n",
          fifties, "fifties\n",
          twenties, "twenties\n",
          tens, "tens\n",
          fives, "fives\n",
          ones, "ones\n")
if __name__ == '__main__':
    main()
