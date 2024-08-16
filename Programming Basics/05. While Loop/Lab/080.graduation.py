name = input()
grade = 1
fail_count = 0
total_grades = 0

while grade <= 12:
    current_grade = float(input())

    if current_grade < 4.00:
        fail_count += 1
        if fail_count > 1:
            print(f"{name} has been excluded at {grade} grade")
            break
    else:
        total_grades += current_grade
        grade += 1

if grade > 12:
    average_grade = total_grades / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")