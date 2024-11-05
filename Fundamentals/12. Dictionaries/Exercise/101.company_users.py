employees = {}
while True:
    entry = input()
    if entry == "End":
        break
    name, id = entry.split(" -> ")
    if name not in employees:
        employees[name] = set()
    employees[name].add(id)
for company, ids in employees.items():
    print(company)
    for emp_id in ids:
        print(f"-- {emp_id}")