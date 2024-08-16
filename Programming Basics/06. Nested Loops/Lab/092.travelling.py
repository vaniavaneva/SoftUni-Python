destination = input()
saved = 0
while destination != 'End':
    budget = float(input())
    money = float(input())
    saved += money
    while saved < budget:
        money = float(input())
        saved += money
    print(f'Going to {destination}!')
    destination = input()
    saved = 0

