"""
    CS 5001
    10/28/2023
    Align Online Module 7 - create_dictionary.py
    Garfield Maitland
"""

''' 
    Didn't cover the implementation of sets in the modules. But there was a video on them
    Three examples for creating the same do_re_mi dictionaries in PythonDo-Re-Mi example of using Dictionaries in Python
'''

"""
    Recall that the way a python program executes is from the bottom up.
    That mean's it starts with the line 'main()' and thus calls the
    def main(): function. After that, it executes what is in the main
    function line by line. It also jumps to other modules and helper
    functions when appropriate. 
    
    Separately, the way we iterate over content is with the for loop
    and the while loop. The for loop typically requires about 3 lines of
    code. They are the list of items, the conditional statement, and the
    print statement.
    
    The while loop typically requires about 5 lines of code. The list 
    of items, the update variable, the conditional statement, the
    print statement, and the variable update statement. Let's 
    demonstrate.
"""

# Demonstrate for loop
letters = "abcde"
for letter in letters:
    print(letter)
    print(f"This is the letter: {letter}")

# Demonstrate while loop
letters = "abcde"
i = 0
while i < len(letters):
    print(letters[i])
    i += 1

# Demonstrate nested while loop
important = ["sleep", "diet", "exercise"]
i = 0
while i < len(important):
    print(important[i])
    j = 0
    while j < len(important[i]):
        print(important[i][j])
        j += 1
    i += 1


empty_dictionary = {}

# dictionary uses the {} curly brackets, likely my favorite 1

do_re_mi_0 = {"do": "doe, a deer, a female deer",
              "re": "a drop of golden sun",
              "mi": "a name I call myself",
              "fa": "a long, long way to run"
              }

# Example uses the {} to delimit a list of key:value pairs
do_re_mi_1 = {"do": "doe, a deer, a female deer",
              "re": "a drop of golden sun",
              "mi": "a name I call myself",
              "fa": "a long, long way to run"
              }


# Example uses the dict() function with a list of named parameters
do_re_mi_2 = dict(do="doe, a deer, a female deer", re="a drop of golden sun",
                  mi="a name I call myself", fa="a long, long way to run")

# Example uses the dict() with a list of 2-value lists as the parameter
do_re_mi_3 = dict([["do", "doe, a deer, a female deer"],
                   ["re", "a drop of golden sun"],
                   ["mi", "a name I call myself"],
                   ["fa", "a long, long way to run"]])

# dictionary.items() variable name of the dictionary and then the .items() method

letters = "abcde"
i = 0
while i < len(letters):
    print(letters[i])
    i += 1