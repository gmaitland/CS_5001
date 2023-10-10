def main():
    #print out every single element in the list
    list = [[1,2,3], [4,5,6]]
    
    i = 0 # reset i
    # iterate through the first level of multidimensional list
    while(i < len(list)):
        print("\nnext row")
        print(f"i: {i}") # print out row index
        print(f"list[i] = {list[i]}")

        j = 0 # reset j
        while(j < len(list[i])): # 3 < 3
            print("inner loop")
            # print out "column" index (elements of a row)
            print(f"j: {j}")
            print(f"list[{i}][j] = {list[i][j]}")
            j += 1
        i += 1

main()
