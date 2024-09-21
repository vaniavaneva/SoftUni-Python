n = int(input())
check = ''
pure = True
for _ in range(n):
    word = input()
    pure = True
    for i in range(len(word)):
        check = word[i]
        if check == ',' or check == '.' or check == '_':
            pure = False
            break
    if pure:
        print(f'{word} is pure.')
    else:
        print(f'{word} is not pure!')