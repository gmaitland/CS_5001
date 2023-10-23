def count_iterations(val):
    count=0
    while val > 1:
        val = val - 2
        count = count + 1
    print(count)
    
print(5 + count_iterations(10))
