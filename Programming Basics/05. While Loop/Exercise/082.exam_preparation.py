threshold = int(input())
failedTimes = 0
solved = 0
grades = 0
last = ''
failed = True
while failedTimes < threshold:
    problem = input()
    if problem == 'Enough':
        failed = False
        break
    grade = int(input())
    if grade <= 4:
        failedTimes += 1
    grades += grade
    solved += 1
    last = problem
if failed:
    print(f'You need a break, {threshold} poor grades.')
else:
    print(f'Average score: {grades / solved:.2f}')
    print(f'Number of problems: {solved}')
    print(f'Last problem: {last}')
