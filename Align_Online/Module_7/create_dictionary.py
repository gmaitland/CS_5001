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
