"""
    Garfield Maitland
    CS 5001
    10/10/2023
    Tutoring - nested_nested_while_loops.py
"""


def main():
    # print out every single element in the list
    list1 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

    i = 0  # reset i
    # iterate through the first level of multidimensional list
    while (i < len(list1)):
        print(f'\n\ntop level: {list1}')
        print('\nnext row')
        print(f'i: {i}')  # print out row index
        print(f'list[i] = {list1[i]}')

        j = 0  # rest j
        while (j < len(list1[i])):  # 2 not < 2
            print('inner loop')
            # print out "column" index (elements of a row)
            print(f'j: {j}'
            print(f'list[{i}][j] = {list1[i][j]}')

            k = 0  # reset k
            while (k < len(list1[i][j])):  # 2 not < 2
                print('inner inner loop')
                # print out "column", "column" index (elements of a row)
                print(f'k: {k}')
                print(f'list[{i}][{j}][k] = {list1[i][j][k]}')
                # print(f'{list1[i][j][k]}')
                k += 1
            j += 1
        i += 1


main()
