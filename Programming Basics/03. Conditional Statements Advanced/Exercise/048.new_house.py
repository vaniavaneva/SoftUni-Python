flowers = input()
numFlowers = int(input())
budget = int(input())
cost = 0
if flowers == 'Roses':
    cost = numFlowers * 5
    if numFlowers > 80:
        cost *= 0.9
elif flowers == 'Dahlias':
    cost = numFlowers * 3.8
    if numFlowers > 90:
        cost *= 0.85
elif flowers == 'Tulips':
    cost = numFlowers * 2.8
    if numFlowers > 80:
        cost *= 0.85
elif flowers == 'Narcissus':
    cost = numFlowers * 3
    if numFlowers < 120:
        cost = cost + (cost * 0.15)
elif flowers == 'Gladiolus':
    cost = numFlowers * 2.5
    if numFlowers < 80:
        cost = cost + (cost * 0.2)
if cost <= budget:
    print(f'Hey, you have a great garden with {numFlowers} '
          f'{flowers} and {budget - cost:.2f} leva left.')
else:
    print(f'Not enough money, you need {cost - budget:.2f} leva more.')