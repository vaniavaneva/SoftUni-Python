n = int(input())

total_grades_sum = 0
total_grades_count = 0
total_presentations = 0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        break

    presentation_sum = 0

    for _ in range(n):
        grade = float(input())
        presentation_sum += grade
        total_grades_sum += grade
        total_grades_count += 1

    presentation_average = presentation_sum / n
    print(f"{presentation_name} - {presentation_average:.2f}.")

if total_grades_count > 0:
    final_average = total_grades_sum / total_grades_count
    print(f"Student's final assessment is {final_average:.2f}.")