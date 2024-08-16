text = input()
Sum = 0
for i in range(1, len(text)):
    if text[i] == "a":
        Sum += 1
    if text[i] == "e":
        Sum += 2
    if text[i] == "i":
        Sum += 3
    if text[i] == "o":
        Sum += 4
    if text[i] == "u":
        Sum += 5
print(Sum)