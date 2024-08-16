allSteps = 0
while allSteps <= 10000:
    steps = input()
    if steps == 'Going home':
        steps = int(input())
        allSteps += steps
        if allSteps < 10000:
            print(f'{10000 - allSteps} more steps to reach goal.')
        break
    steps = int(steps)
    allSteps += steps
if allSteps >= 10000:
    print(f'Goal reached! Good job!')
    print(f'{allSteps - 10000} steps over the goal!')
