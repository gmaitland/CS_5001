import acrostic_data

# 'Return' is a big red button that says 'abort'

x = acrostic_data.POEM.split("\n")

y = x[0][0]

z = []
for i in range(len(x)):
    if len(x[i]) > 0:
        print(x[i][0])
        z.append(x[i][0])

print(z)

a = " ".join(z)

a.
print(a)








