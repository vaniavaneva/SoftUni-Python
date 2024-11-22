n = int(input())
word = input()
strings = []
for _ in range(n):
    current_string = input()
    strings.append(current_string)
print(strings)
for x in range(len(strings) - 1, - 1, - 1):
    element = strings[x]
    if word not in element:
        strings.remove(element)
print(strings)