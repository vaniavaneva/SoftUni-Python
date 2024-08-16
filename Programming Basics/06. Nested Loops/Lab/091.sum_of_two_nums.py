start = int(input())
end = int(input())
magic = int(input())
combinations = 0
x1, x2 = 0, 0
found = False
for x1 in range(start, end + 1):
    for x2 in range(start, end + 1):
        combinations += 1
        if x1 + x2 == magic:
            print(f'Combination N:{combinations} ({x1} + {x2} = {magic})')
            found = True
            break
    if found:
        break
if not found:
    print(f'{combinations} combinations - neither equals {magic}')