"""
    CS 5001
    10/23/2023
    Align Online Module 4 - nana.py
    Garfield Maitland
"""

"""
    We are printing a for loop that will range
    over all the iterations of the function.
    After looking at the function in more detail,
    it appears that it may not run. Wow, it ran,
    this will require further investigation, and
    exploration
"""

def main():
    for i in range(8):
        print("na", end=" ")
        print(i)
    print("hey hey hey goodbye")
    print(i)
# The for loop seems like it is easier to implement


    i = 0 # initialization
    while i < 8: # loop condition
        print("na", end = " ")
        i += 1 # loop update statement
    print("hey hey hey goodbye")

# However the while loop appears to be more clean.
# Personally, I prefer the while loop
main()
