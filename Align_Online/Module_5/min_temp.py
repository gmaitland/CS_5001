"""
    CS 5001
    10/27/2023
    Align Online Module 5 - min_temp.py
    Garfield Maitland
"""

HIGH_TEMPS = [92, 84, 98, 87, 94, 86, 75, 81, 91, 96, 75,
              74, 78, 78, 76, 79, 77, 91, 83, 77, 79, 74,
              78, 86, 88, 87, 84, 82, 82, 81, 83]


def main():

    """
    # min high temp in July
    min_temp = 100
    for temp in HIGH_TEMPS:
        if temp < min_temp:
            min_temp = temp
    print("Min temp in July was", min_temp, "degrees!")
    print(min_temp)
    """

max_temp = 80
for temp in HIGH_TEMPS:
    if temp > max_temp:
        max_temp = temp
        print(max_temp)

min_temp = 80
for temp in HIGH_TEMPS:
    if temp < min_temp:
        min_temp = temp
        print(min_temp)

average_temp = int(sum(HIGH_TEMPS)) / int(len(HIGH_TEMPS))
print(average_temp)

j = 0
for i in HIGH_TEMPS:
    j += i
print(f'The arithmetic total is {j}')
a = j / len(HIGH_TEMPS)
print(f'The average temperature is {int(a)}')

x = "Now is the summer of our joy".split() # When you use the .split() method
# Converts the string object into an array
for w in "Now is the winter of our discontent".split():
    print(x) # You can't use the .split() on an array



main()
