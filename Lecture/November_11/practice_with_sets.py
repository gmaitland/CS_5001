"""
    Garfield Maitland
    CS 5001
    11/19/2023
    Practice - practice_with_sets.py
"""

"""
    Data compiled from the python docs page:
    
    A set is an unordered collection with no duplicate elements
    Basic uses include membership test and eliminating duplicate
    entries. Set objects also support mathematical operations like
    union, intersection, difference, and symmetric difference.
    
    Curly braces, or the set() built in function can used to create sets.
    To create an empty set, you have to use set(). This is because 
    {} creates an empty dictionary, not an empty set.
    
    Let's get started
"""

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket, "This is the set")    # show that duplicates have been removed

print('orange' in basket)   # fast membership testing

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')

print(a)    # prints unique letters in a
print(a - b)    # prints unique letters in a but not in b
print(a | b)    # prints set union
print(a & b)    # prints set conjunction
# print(a ^ b)    # exclusive or

