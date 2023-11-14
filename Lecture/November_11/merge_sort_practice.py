"""
    Garfield Maitland
    CS 5001
    11/14/2023
    Lecture - merge_sort_practice.py
"""

"Merge sort has a time complexity of 2log(n)"


def merge(L1: list, L2: list) -> list:
    """
    Merge sorted lists L1 and L2 into a new list and return that new list.
    >>> merge([1, 3, 4, 6], [1, 2, 5, 7])
    [1, 1, 2, 3, 4, 5, 6, 7]
    """

    newL = []
    i1 = 0
    i2 = 0

    # For each pair of items L1[i1] and L2[i2], copy the smaller into newL.
    while i1 != len(L1) and i2 != len(L2):
        if L1[i1] <= L2[i2]:
            newL.append(L1[i1])
            i1 += 1
        else:
            newL.append(L2[i2])
            i2 += 1

    # Gather any leftover items from the two sections.
    # Note that one of them will be empty because of the loop condition.
    newL.extend(L1[i1:])
    newL.extend(L2[i2:])
    print(newL)
    return newL

""" """


def main():
    list1 = [1, 3, 5, 9, 93, 93]
    list2 = [0, 343, 99, 343, 343243]
    list3 = merge(list1, list2)
    print(list3)
    list4 = mergesort(list3)
    print(list4)


if __name__ == "__main__":
    main()
