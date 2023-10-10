
def main():
    list1 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

    i = 0
    while (i < len(list1)):
        print(f'{list1}')
        print(f'{list1[i]}')

        j = 0
        while (j < len(list1[i])):
            print(f'{list1[i]}')
            print(f'{list1[i][j]}')

            k = 0
            while (k < len(list1[i][j])):

                print(f'{list1[i][j]}')
                print(f'{list1[i][j][k]}')
                k += 1
            j += 1
        i += 1
main ()
