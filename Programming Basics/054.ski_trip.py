days = int(input())
typeRoom = input()
grade = input()
nights = days - 1
cost = 0
finalCost = 0
if typeRoom == 'room for one person':
    cost = 18
elif typeRoom == 'apartment':
    cost = 25
    if days < 10:
        cost *= 0.7
    elif 10 < days < 15:
        cost *= 0.65
    elif days > 15:
        cost *= 0.5
elif typeRoom == 'president apartment':
    cost = 35
    if days < 10:
        cost *= 0.9
    elif 10 < days < 15:
        cost *= 0.85
    elif days > 15:
        cost *= 0.8
if grade == 'positive':
    finalCost = nights * cost + (nights * cost) * 0.25
elif grade == 'negative':
    finalCost = nights * cost - (nights * cost) * 0.1
print(f'{finalCost:.2f}')