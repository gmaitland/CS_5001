"""
    Slice a list
"""

# How to get a sublist

# t[1:3] Start at 1 and End at 3 (not inclusive)

# t[:4] Not inclusive of 4

# t[3:] Goes to the end

# t[:] A copy of the whole list

# x[::-1] Return a list from front to back

# *IMPORTANT*
# x[::2] Skip 1 and skip 1.
# Example
# y = [1, 2, 3, 4, 5, 6]
# >>> y[::2] Return [1, 3, 5]

def main():

    
    for i in range(50, 700, 5):
        # 1st Value Start, 2nd Value End, 3rd value Increment
        print(i)

# Can have 3 parameters
 
if __name__ == "__main__":
    main()


