"""
    Garfield Maitland
    CS 5001
    11/19/2023
    Practice - practice_with_dictionaries.py
"""
import math

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

# We can create dictionaries with the dict() constructor from
# sequences of key value pairs

z = dict([('adam', 100), ('bob', 200), ('charlie', 300)])
print(z)

# We can also use dictionary comprehension to create key value:value pairs

y = {x: x**2 for x in (2, 4, 6)}
print(y)

x = dict(david=1, eric=2, fred=3)
print(x)

"""
    In summary. We created a dictionary in three different ways. We used the
    We used {}, the dict() function on a list, and the dict(key=value) specification.
"""


# Using set on a sequence eliminates duplicates

# We are about to cover Looping Techniques

knights = {'gallahad': 'the pure', 'robin': 'the brave', 'garfield': 'the focused'}
for k, v in knights.items():
    print(k, v)

# So that is how we do it. We create two temp variables to loop the dict()

# We can also retrieve the position index and corresponding value pair
# with the enumerate() function

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# I think this current one is a bit advanced. Let's begin
# We can loop over two or more sequences at the same time

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
responses = ['nice to meet you', 'good luck', 'great']
for q, a, r in zip(questions, answers, responses):
    print('What is your {0}?, It is {1}. Ok, {2}.'.format(q, a, r))

# We can also loop over a sequence in reverse
# All we have to do is specify the sequence in the forward direction
# and then call the reversed() function

for i in reversed(range(1, 10, 2)):
    print(i)

# Ok we just incremented by 2. Let's increment by 3.

for j in reversed(range(1, 20, 3)):
    print(j)

# It is possible to loop over a sorted order with the sorted() function.
# This leaves the source unaltered

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

# Using the set() function on a sequence eliminates duplicate elements.
# You can also combine with the sorted function to synergized the operation
# in an idiomatic way

for f in sorted(set(basket)):
    print(f)

# It is better to create a new list when looping over it

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)