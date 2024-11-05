count = int(input())
grades = {}
for _ in range(count):
    name = input()
    grade = float(input())
    if name not in grades:
        grades[name] = []
    grades[name].append(grade)
for name, grades in grades.items():
    average = sum(grades) / len(grades)
    if average >= 4.50:
        print(f"{name} -> {average:.2f}")