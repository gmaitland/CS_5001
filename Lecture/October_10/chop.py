list1 = [[1, 2, 3], [4, 5, 6]]

i = 0
while (i < len(list1)):
    print(f'{list1[i]}')

    j = 0
    while (j < len(list1[i])):
        print(f'{list1[i][j]}')
        j += 1
              
    i += 1
