budget = int(input())
season = input()
fishers = int(input())
cost = 0
if season == 'Spring':
    cost = 3000
elif season == 'Summer' or season == 'Autumn':
    cost = 4200
elif season == 'Winter':
    cost = 2600
if fishers <= 6:
    cost *= 0.9
elif 7 <= fishers <= 11:
    cost *= 0.85
elif fishers >= 12:
    cost *= 0.75
if season != 'Autumn' and fishers % 2 == 0:
    cost *= 0.95
if cost <= budget:
    print(f'Yes! You have {budget - cost:.2f} leva left.')
else:
    print(f'Not enough money! You need {cost - budget:.2f} leva.')