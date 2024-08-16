n = int(input())
a = b = c = d = e = 0
for i in range(0, n):
    num = int(input())
    if num < 200:
        a += 1
    elif 200 <= num <= 399:
        b += 1
    elif 400 <= num <= 599:
        c += 1
    elif 600 <= num <= 799:
        d += 1
    elif num >= 800:
        e += 1

print(f'{a / n * 100:.2f}%')
print(f'{b / n * 100:.2f}%')
print(f'{c / n * 100:.2f}%')
print(f'{d / n * 100:.2f}%')
print(f'{e / n * 100:.2f}%')
