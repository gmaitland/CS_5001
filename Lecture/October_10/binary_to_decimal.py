"""
    Garfield Maitland
    CS 5001
    10/10/2023
    Binary to Decimal Converter
"""

# Used the for loop to help traverse the list

def binary(digits):
    digits = digits[::-1]

    value = 0
    for i in range(len(digits)):
        value = value + int(digits[i]) * 2**i
    return value

def main():
    print("001", binary("001")) # 1
    print("100", binary("100")) # 4
    print("101", binary("101")) # 5
    print("111", binary("111")) # 7

    print(["1", "1", "1"], binary(["1", "1", "1"]))
    

    
if __name__ == "__main__":
    main()
