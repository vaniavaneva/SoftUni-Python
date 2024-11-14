text = input()
result = []
explosion = 0
for i in range(len(text)):
    if text[i] == '>':
        result.append(text[i])
        explosion += int(text[i + 1])
    elif explosion > 0:
        explosion -= 1
    else:
        result.append(text[i])
print(''.join(result))