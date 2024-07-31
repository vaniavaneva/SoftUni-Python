n1 = int(input())
n2 = int(input())
op = input()
result = 0
if op == '+':
    result = n1 + n2
    if result % 2 == 0:
        print(f'{n1} {op} {n2} = {result} - even')
    else:
        print(f'{n1} {op} {n2} = {result} - odd')
elif op == '-':
    result = n1 - n2
    if result % 2 == 0:
        print(f'{n1} {op} {n2} = {result} - even')
    else:
        print(f'{n1} {op} {n2} = {result} - odd')
elif op == '*':
    result = n1 * n2
    if result % 2 == 0:
        print(f'{n1} {op} {n2} = {result} - even')
    else:
        print(f'{n1} {op} {n2} = {result} - odd')
elif op == '/':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 / n2
        print(f'{n1} {op} {n2} = {result:.2f}')
elif op == '%':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 % n2
        print(f'{n1} {op} {n2} = {result}')