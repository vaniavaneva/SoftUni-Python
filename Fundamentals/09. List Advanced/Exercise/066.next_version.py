string = input()
old = list(map(int, string.split('.')))
old[-1] += 1
if old[-1] > 9:
    old[-1] = 0
    old[-2] += 1
    if old[-2] > 9:
        old[-2] = 0
        old[-3] += 1
new = '.'.join(map(str, old))
print(new)