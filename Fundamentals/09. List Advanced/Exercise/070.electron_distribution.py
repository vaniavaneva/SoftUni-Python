electrons = int(input())
n = 1
shells = []
while electrons > 0:
    maxShell = 2 * (n ** 2)
    if electrons >= maxShell:
        shells.append(maxShell)
        electrons -= maxShell
    else:
        shells.append(electrons)
        electrons = 0
    n += 1
print(shells)