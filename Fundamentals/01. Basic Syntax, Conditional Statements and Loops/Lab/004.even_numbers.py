n = int(input())
for i in range(n):
    num = int(input())
    if num % 2 == 1:
        print(f'{num} is odd!')
        break
else:
    print('All numbers are even.')