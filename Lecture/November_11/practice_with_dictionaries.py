"""
    Garfield Maitland
    CS 5001
    11/19/2023
    Practice - practice_with_dictionaries.py
"""

"""
    Dictionaries are sometimes called associative memories or associative arrays. Unlike sequences,
    which are indexed by a range of numbers, dictionaries are indexed by keys. Keys can be any
    immutable type. Strings and numbers can always be keys. Tuples can be keys if they contain only
    stings, numbers or tuple. if a tuple contains a mutable object, directly or indirectly, it
    can not be used as a key. Lists can not be keys. This is because lists can be modified 
    using index assignments, slice assignments, or methods like append() and extend().
    
    It is ideal to think about dictionaries as key value pairs with the requirements that the keys are unique
    within on dictionary. A pair of braces creates an empty dictionary {}. : delineates the key: value pairs.
    Placing a comma separates the different key value pairs.
    
    The main use of a dictionary is to store a value with some key and extracting the value given the key.
    We can also delete a key: value pair with del. If you store using a key that is already in use, the
    old value associated with that key is forgotten. It is an error to extract a value using a
    non-existent key.
    
    The list(d) function returns a list of all the keys used in the dictionary, that were placed in insertion
    order. You can use sorted(d) to return a sorted list of all the dictionary keys. To check whether a single
    key is in the dictionary, use the in keyword. 
"""

tel = {'jack' : 4098, 'sape' : 4139}

tel['guido'] = 4127
print(tel)
tel['jack']

del tel['sape']
tel['irv'] = 4127
tel
list(tel)
print(tel)

sorted(tel)
print(tel)

print('guido' in tel)

print('jack' not in tel)


