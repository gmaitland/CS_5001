"""
    Garfield Maitland
    CS 5001
    10/17/2023
    Lecture - exception_example.py
"""
'''
def try_it(value, value2):
    try:
        x = int(value)
        y = int(value2)
        return x/y

        
    except (ValueError, ZeroDivisionError):
        print("Could not convert value to integer")




def main():
    try_it("K", "Z")
    print(try_it("1", "2"))
    print(try_it("1", "0"))
    
if __name__ == "__main__":
    main()
    
'''

import time

print("Starting...")
for i in range(50):
    print(i**5**5
          , end='', flush=False)
    dtime.sleep(1)
print("\nDone!")


