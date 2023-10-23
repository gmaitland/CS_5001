"""
    CS 5001
    10/23/2023
    Align Online Module 3 - pizza_starter.py
    Garfield Maitland
"""

"""
    Boolean Expressions, Conditional Expressions & Conditionals
    In this program we want to calculate the number of slices
    each person can eat when n pizzas are ordered
"""




def main():
    # get two integers from the user
    pizzas = int(input("How many pizzas did you order? "))
    people = int(input("How many people are there? "))
    if people != 0:
        # multiply by 8 slices per pie and divide
        slices = pizzas * 8 / people
        print(pizzas, "pizzas split between", people, "can have", slices, "slices")
    else:
        print("People can not be zero")

main()


"""
    Used if and else conditional statement to create a 
    boolean situation
"""