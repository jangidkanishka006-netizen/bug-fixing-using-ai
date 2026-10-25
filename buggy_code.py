# Student Result Calculator
# This code intentionally contains bugs.

def calculate_average(marks):
    total = 0
    for mark in marks:
        total = mark
    return total / len(marks)


def check_result(average):
    if average > 40:
        return "Fail"
    else:
        return "Pass"


students = {
    "Aman": [80, 70, 90],
    "Riya": [35, 40, 30],
    "Karan": [60, 75, 85]
}

for name, marks in students.items():
    average = calculate_average(marks)
    result = check_result(average)

    print("Student:", name)
    print("Average:", average)
    print("Result:", result)
    print("-------------------")
