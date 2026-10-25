
# Student Marks Calculator - Fixed Version

def calculate_average(marks):
    if not marks:
        return 0

    total = sum(marks)
    return total / len(marks)


def check_result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"


marks = [75, 80, 65]

average = calculate_average(marks)

print("Average Marks:", average)
print("Result:", check_result(average))
