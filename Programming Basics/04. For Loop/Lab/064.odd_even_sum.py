n = int(input())
Sum1 = 0
Sum2 = 0
for _ in range(n):
    number = int(input())
    if _ % 2 == 0:
        Sum1 += number
    else:
        Sum2 += number
if Sum1 == Sum2:
    print('Yes')
    print(f'Sum = {Sum1}')
else:
    print('No')
    print(f'Diff = {abs(Sum1 - Sum2)}')