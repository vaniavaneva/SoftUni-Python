product = input()
amount = int(input())


def sum(product):
    if product == 'coffee':
        return amount * 1.5
    elif product == 'water':
        return amount * 1.0
    elif product == 'coke':
        return amount * 1.4
    elif product == 'snacks':
        return amount * 2.0


print(f'{sum(product):.2f}')