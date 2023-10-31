"""
    Garfield Maitland
    CS 5001
    10/31/2023
    Lecture - filedictionary.py
"""

def load_dictionary(file_name):
    with open(file_name, mode="r") as in_file:
        logos = {}

        for each in_file:
            each = each.strip("\n")
            english, french, spanish = each.split(",")
            logos[english] = [french, spanish]

        return logos
