students = {}
while True:
    command = input()
    if ":" not in command:
        target_course = command.replace("_", " ")
        break
    name, student_id, course = command.split(":")
    course = course.strip()
    if course not in students:
        students[course] = []
    students[course].append((name, student_id))
if target_course in students:
    for name, student_id in students[target_course]:
        print(f"{name} - {student_id}")