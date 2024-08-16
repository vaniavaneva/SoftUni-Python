money = 0
while True:
    line = (input())
    if line == 'NoMoreMoney':
        break
    line = float(line)
    if line <= 0:
        print('Invalid operation!')
        break
    print(f'Increase: {line:.2f}')
    money += line
print(f'Total: {money:.2f}')