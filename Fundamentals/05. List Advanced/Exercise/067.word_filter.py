string = input()
even = [word for word in string.split() if len(word) % 2 == 0]
for word in even:
    print(word)