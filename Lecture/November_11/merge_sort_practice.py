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
    # print(newL)
    return newL


    """ 
        About to create a mergesort algorithm. Merge sort, use merge to do the
        bulk of the work. It does this by making a list of one-item lists.
        As long as there are two lists to merge, they are merged
    """


def mergesort(L: list) -> None:
    """
    Reorder the items in L from smallest to largest.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> mergesort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """

    # Make a list of 1-item lists so that we can start merging.
    workspace = []
    for i in range(len(L)):
        workspace.append([L[i]])

    # The next two lists to merge are workspace[i] and workspace[i + 1].
    i = 0
    # As long as there are at least two more lists to merge, merge them.
    while i < len(workspace) - 1:
        L1 = workspace[i]
        L2 = workspace[i + 1]
        newL = merge(L1, L2)
        workspace.append(newL)
        i += 2

    # Copy the result back into L.
    if len(workspace) != 0:
        L[:] = workspace[-1][:]


def main():
    list1 = [1, 3, 5, 9, 93, 93]
    list2 = [0, 343, 99, 343, 343243]
    list3 = merge(list1, list2)
    print(list3)
    mergesort(list3)


if __name__ == "__main__":
    main()

# Try to create bubble_sort(L)
def bubble_sort(L: list) -> None:
    workspace = []
    i1 = 0
    i2 = 1

