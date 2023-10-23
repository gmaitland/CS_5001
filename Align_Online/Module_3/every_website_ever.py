"""
    CS 5001
    10/23/2023
    Align Online Module 3 - every_website_ever.py
    Garfield Maitland
"""

"""
    Created 2 functions, choose_menu() and main()
    main() includes the conditional, and
    the initialization statement, choose_menu()
    has the update statement 
"""


def choose_menu():
    ''' Function: choose_menu
        Parameters: none
        Returns: nothing
    '''
    print("L -- Login\n"
          "R -- Register\n"
          "Q -- Quit\n")
    choice = input("Enter your choice now\n")
    return choice.upper()


def main():
    while True:
        option = choose_menu()
        if option == "Q":
            break

    print("Thanks for using our website!\n")


main()
