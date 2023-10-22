"""
    CS 5001
    10/22/2023
    Align Online Module 2 - myneu.py
    Garfield Maitland
"""

def view_calendar():
    ''' Function view_calendar
        Parameters: none
        Returns: nothing
    '''
    print("Calendar:\n"
          "Start date: Jan 7th\n"
          "End date: April 27th\n")

def view_class_schedule(my_class):
    ''' Function view_class_schedule
        Parameter: string
        Returns: nothing
    '''
    if my_class == "MATH1241":
        print("MWR 9:15-10:25am")
    elif my_class == "CS5001":
        print("T 6-9:00pm")
    elif my_class == "CS5002":
        print("W 6-9:00pm")
    else:
        print("Not valid input or you don't have class")

def calculate_tuition(total_tuition, scholarship_pct):
    ''' Function calculate_tuition
        Parameters: two floats
        Returns: float
    '''
    to_pay = total_tuition - total_tuition * scholarship_pct
    return to_pay

def main():
    """
    view_calendar()
    view_class_schedule("MATH1241")
    view_class_schedule("CS5001")
    view_class_schedule("CS5002")

    view_calendar()
    view_calendar()

    view_class_schedule("CS5001")
    print("...")
    view_class_schedule("CS5002")
    print("...")
    """
    my_class = input("What class are you taking?\n").upper()
    print("here's your schedule...\n")
    view_class_schedule(my_class)

    tuition = float(input("How much is total tuition?\n"))
    discount = float(input("How much scholarship pct did you get?\n"))
    left_to_pay = calculate_tuition(tuition, discount)
    
    print("You need to pay $", left_to_pay, sep = "")
    
main()

"""
    We created multiple functions that we then called
    from our main function. This allowed us to input
    different types of arguments into the parameter
    field, and observe the behavior and output. We did
    this by prompting the user for input and then
    we mapped the user input to the appropriate
    value in our defined function. Our defined function
    view_class_schedule was defined with conditional
    if, elif and else conditional statements.
"""