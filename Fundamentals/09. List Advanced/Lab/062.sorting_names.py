names = input().split(', ')
sortedList = sorted(names, key=lambda x: (-len(x), x))
print(sortedList)