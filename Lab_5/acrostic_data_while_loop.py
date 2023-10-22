import acrostic_data

column = acrostic_data.POEM.split("\n")
print(column)
# Column is a list of strings
# Explain the code at each line, and start thinking of each line
# When you read them, convert to common spoken vernacular
# Allows to speak through the code through a more productive way
j = []
i = 0
# While loop emuluate the function of a for loop
while i < len(column): # i is less than the number of strings in the variable
    line = column[i] # Denotes that is a line from acrostic.poem.py
    if len(line) > 0:
        print(line[0])
        # print(" ")
        j.append(line[0])
        # print(j)

    if len(line) == 0:
        j.append(" ")
#    else:
#        print(" ")

    # if len(line) == 0:
    i += 1

k = "".join(j)
print(k)

# String joining
print(j)

# "".join(["a", " ", "b"])