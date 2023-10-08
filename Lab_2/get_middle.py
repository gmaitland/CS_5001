"""
   2023_Fall_CS5003_Lab_2
   09/21/2023_(09/22/2023)
   Garfield Maitland
   get_middle.py
"""


def get_middle(one, two, three):
    minimum = int(min(one, two, three))
    maximum = int(max(one, two, three))

    total = int(one) + int(two) + int(three)
    middle = total - (minimum + maximum)

    return middle
    # 002842027


def main():
    one = input("1st number is ")
    two = input("2nd number is ")
    three = input("3rd number is ")

    middle = get_middle(one, two, three)
    print("The middle number is ", middle)


if __name__ == "__main__":
    main()
