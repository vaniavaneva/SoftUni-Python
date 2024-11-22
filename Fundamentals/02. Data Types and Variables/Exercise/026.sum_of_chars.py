n = int(input())
total_sum = 0
while n > 0:
    letter = input()
    total_sum += (ord(letter))
    n -= 1
print(f'The sum equals: {total_sum}')