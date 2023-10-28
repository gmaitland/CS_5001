'''
    Lab 6: Disney Facebook
    Fall 2022
    CS 5001
    Goal: File manipulation in Python
'''

def initialize_FB():
    ''' Function: initialize_FB
        Input: None.
        Returns: a list filled with the dwarves and their friends, read
                 from a file.
                 First name in the list is the "account holder".
                 The rest of the list are their "friends"
    '''

    # haven't covered exception handling here. Assume file exists and can be
    # found. In the future, put a try: block here

    try:
        with open('facebook.txt', 'r') as infile:
            dwarves = []
            for lines in infile:
                lines = lines.split() # make a list out of the blank separated string
                dwarves.append(lines) # create list of lists from data file
            return dwarves
    except FileNotFoundError:
        print("Error: Could not locate the facebook data")
    except:
        print("An unknown error occurred")
    # implicit return None here. We'll use that as O (in I-P-O) in the caller

def menu(message, options='PUFQ'):
    ''' Function: menu
        Input:  message - user prompt message, options - valid options.
        Returns: 2-Tuple - user selection and boolean indicating if
                 the choice was in the valid option lis
        Description: Our friendly menu from Lecture 3 appears once again!
                     Functions and reuse at their best, y'all! :-)
    '''
    answer = input(message)
    answer = answer.upper() # convert to uppercase for comparison
    if(answer[0] in options.upper()): #compare first letter if they enter more
        return answer, True
    return answer, False

def get_known_dwarves(dwarves):
    ''' Function: get_known_dwarves
        Input: dwarves - list of lists holding dwarf FB information
        Returns: list that matches the names of the dwarves

        Note: We could have "hard coded" the names of the dwarves, but
        what if in the future, we want to consider different dwarves? Or,
        what if one of the dwarves gets a "solo contract" and we need to make
        this a 6-dwarve deal with Disney? Assuming the data file holds the
        "ground truth" of the FB users, we can read that file for the current
        roster and insulate ourselves from future changes.
    '''
    known_dwarves = []
    try:
        for each in dwarves:
            known_dwarves.append(each[0].lower())
    except:
        print("A little bit of an index error occurred. Data is unusable")
    finally:
        return known_dwarves
        
def find_me(me, dwarves):
    ''' Function: find_me
        Input: me - string representing current user dwarf
               dwarves - list of lists holding dwarf FB information
        Returns: list that matches the found dwarf (me)
    '''

    for each in dwarves:
        if each[0].lower() == me.lower():
            return each
        
def print_friends(me, dwarves):
    ''' Function: print_friends
        Input: me - string representing current user dwarf
               dwarves - list of lists holding dwarf FB information
        Returns: None
        Do: print the friends associated with the current user
    '''

    target = find_me(me, dwarves)
    if target is None:
        print("Warning: Data file is damaged. Cannot process request")
        return

    if len(target) == 1:
        print('You have no friends. Boo hoo.')
        return
    friends = target[1:] # slice to get our sublist of friends
    print(f"{target[0]}'s friends -> ", end = " ")
    for each in friends:
        print(each.capitalize(), end = " ")
    print("\n-------\n")

def unfriend(me, dwarves):
    ''' Function: unfriend
        Input: me - string representing current user dwarf
               dwarves - list of lists holding dwarf FB information
        Returns: None
        Do: remove the user specified dwarf from his friends list
            If the selection is not a friend, print msg and return
    '''

    target = find_me(me, dwarves)
    if target is None:
        print("Warning: Data file is damaged. Cannot process request")
        return
    
    if len(target) == 1: # remember, the current dwarf is at index 0
        print('No one to unfriend')
        return
    
    print('Here is your current friend list')
    print_friends(me, dwarves)
    
    undwarf = input('Who do you want to unfriend? ')
    undwarf = undwarf.lower().capitalize() # I'm storing names in capitalized form
    if (undwarf == target[0]) or (undwarf not in target):
        print('That person isn\'t your friend. No changes made')
        return
    target.remove(undwarf)
    print('Here is your updated friend list')
    print_friends(me, dwarves)
        
def add_friend(me, dwarves):
    ''' Function: add_friend
        Input: me - string representing current user dwarf
               dwarves - dictionary holding dwarf FB information
        Returns: None
        Do: add a dwarf to the current user's friend list. This is
            a closed community, so if the prospect is not a 7-dwarf
            do not add them to the list
    '''
    known_dwarves = get_known_dwarves(dwarves)
    target = find_me(me, dwarves)
    if target is None:
        print("Warning: Data file is damaged. Cannot process request")
        return
    
    print('*** Here is the current friend list ***')
    print_friends(me, dwarves)
    dwarf = input('Who do you want to add to your friend list? ')
    dwarf = dwarf.lower()
    if (dwarf == me.lower()) or (dwarf in target):
        print('Silly silly! You cannot friend yourself' +
              ' or an existing friend. No changes made')
        return
    if dwarf not in known_dwarves:
        print('That person is not a 7-dwarf! No changes made')
        return
    target.append(dwarf)
    print('*** Here is the updated friend list ***')
    print_friends(me, dwarves)

def quitting(dwarves): 
    ''' Function: quitting
        Input: dwarves.
        Returns: None
        Do: Save the FB data to our file prior to exiting the program
    '''

    # haven't covered exception handling here.
    # In the future, put a try: block here in case writing goes haywire

    with open('facebook.txt', 'w') as outfile:
        for dwarf in dwarves:
            for each in dwarf:
                outfile.write(each.capitalize() + ' ')
            outfile.write('\n') # remember to write the newline 1 per "row"!


def main():
    '''
        main driver. Use our menu to get user input and then
        call the appropriate functions based on user requests
    '''

    dwarves = initialize_FB()
    known_dwarves = get_known_dwarves(dwarves)

    me = input('Which of the 7 is logging in? ')
    if me.lower() not in known_dwarves:
        print('Unknown user. Goodbye')
    else:
        while True:
            answer, status = menu(  # not using status for this lab
                'Choose from one of the options below: \n' +
                'P: Print friends list\n' +
                'U: Unfriend someone\n' +
                'F: Add a new friend\n' +
                'Q: Quit\n Enter your choice now: ' )
            if answer == 'P':
                print_friends(me, dwarves)
            elif answer == 'U':
                unfriend(me, dwarves)
            elif answer == 'F':
                add_friend(me, dwarves)
            elif answer == 'Q':
                quitting(dwarves)
                break
    print('Thanks for using Facebooking!')

if __name__ == "__main__":
    main()
            
                
                
