"""
    Grade Calc
"""

def grade():
    grades = []
    my_grade = float(input("Enter a grade, negative to stop: "))
    while my_grade >= 0:
        grades.append(my_grade)
        my_grade = float(input("Enter another grade, neg to stop: "))

    if len(grades) > 0:
        average = sum(grades) / len(grades)

    else:
        average = "Unknown - No greades available"

    print(f"Your average is {average}")
                         
if __name__ == "__main__":
    grade()
