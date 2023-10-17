"""
    CS 5001
    10/13/2023
    Lab 5
    Garfield Maitland
"""

import acrostic_data
# 'Return' is a big red button that says 'abort'
x = acrostic_data.POEM.split("\n")

y = x[0][0]

z = []
for i in range(len(x)): # Slightly pythonic | Similiar to for each
    if len(x[i]) < 1:
        print( end= " ")
    else:
        print(x[i][0])
        z.append(x[i][0])

print(z)

a = " ".join(z)

b = a.lower()

print(b)







