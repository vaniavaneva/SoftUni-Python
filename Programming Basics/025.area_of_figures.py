figure = input()
if figure == 'square':
    a = float(input())
    print(a * a)
elif figure == 'rectangle':
    a = float(input())
    b = float(input())
    print(a * b)
elif figure == 'circle':
    from math import pi
    a = float(input())
    print(pi * (a * a))
elif figure == 'triangle':
    a = float(input())
    b = float(input())
    print((a * b) / 2)
else:
    print('error')