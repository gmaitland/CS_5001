import acrostic_data

column = acrostic_data.POEM.split("\n")

i = 0
while i < len(column):
    column = column[i]
    if len(column) > 0:
        print(" ")
    else:
        print(column)
    i += 1
