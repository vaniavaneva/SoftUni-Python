course = {}
while True:
    line = input()
    if line == "end":
        break
    name, student = line.split(" : ")
    if name not in course:
        course[name] = []
    course[name].append(student)
for course, students in course.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")