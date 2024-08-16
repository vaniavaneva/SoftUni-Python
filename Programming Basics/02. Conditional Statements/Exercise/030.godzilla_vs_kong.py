budget = float(input())
extras = int(input())
costumeCost = float(input())
decor = budget * 0.1
if extras > 150:
    costumeCost *= 0.9
costumes = costumeCost * extras
if decor + costumes > budget:
    print('Not enough money!')
    print(f'Wingard needs {(decor + costumes) - budget:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {budget - (decor + costumes):.2f} leva left.')