n = int(input())
maxNum = float('-inf')
minNum = float('inf')
for _ in range(n):
    number = int(input())
    if number > maxNum:
        maxNum = number
    if number < minNum:
        minNum = number
print(f"Max number: {maxNum}")
print(f"Min number: {minNum}")