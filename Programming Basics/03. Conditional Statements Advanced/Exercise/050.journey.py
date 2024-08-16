budget = float(input())
season = input()
cost = 0
place = ''
typeVacation = 'Hotel'
if budget <= 100:
    place = 'Bulgaria'
    if season == 'summer':
        cost = budget * 0.3
        typeVacation = 'Camp'
    elif season == 'winter':
        cost = budget * 0.7
elif 100 < budget <= 1000:
    place = 'Balkans'
    if season == 'summer':
        cost = budget * 0.4
        typeVacation = 'Camp'
    elif season == 'winter':
        cost = budget * 0.8
elif budget > 1000:
    place = 'Europe'
    cost = budget * 0.9
print(f'Somewhere in {place}')
print(f'{typeVacation} - {cost:.2f}')