"""
    Garfield Maitland
    CS 5001
    10/10/2023
    Grades v2 - with semesters
"""

# try/except, preprocessing, regular expression, trace the code, doctest, unittest

def main():
    grades = [] # remember, grades is a nested list

    my_grade = float(input("Enter a grade, negative to stop: "))
    while my_grade >= 0:
        semester = input("Which semester (FA20, SP23, etc.) ")
        found = False # a flag will use to track the state of finding lists
        for each in grades:
            if semester.upper() in each: # list exists in our grades
                each.append(my_grade)
                found = True
                break
        if not found: # aka if found == False
            grades.append([semester.upper(), my_grade ])

        my_grade = float(input("Enter a grade, neg to stop: "))

    print(grades)
        


if __name__ == "__main__":
    main()
