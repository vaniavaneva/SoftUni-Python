needed = float(input())
owed = float(input())
days = 0
spending = 0
while owed < needed and spending < 5:
    command = input()
    money = float(input())
    days += 1
    if command == 'save':
        owed += money
        spending = 0
    elif command == 'spend':
        owed -= money
        spending += 1
        if owed < 0:
            owed = 0
if spending == 5:
    print('You can\'t save the money.')
    print(days)
if owed >= needed:
    print(f'You saved the money for {days} days.')