n = int(input())
Sum1 = 0
Sum2 = 0
for _ in range(n):
    number = int(input())
    Sum1 += number
for _ in range(n):
    number = int(input())
    Sum2 += number
if Sum1 == Sum2:
    print(f'Yes, sum = {Sum1}')
else:
    print(f'No, diff = {abs(Sum1-Sum2)}')