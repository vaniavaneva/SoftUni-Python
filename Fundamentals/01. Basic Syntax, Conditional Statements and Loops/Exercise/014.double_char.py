while True:
    word = input()
    if word == "End":
        break
    if word == "SoftUni":
        continue
    doubled_word = ""
    for i in range(len(word)):
        check = word[i]
        doubled_word += check * 2
    print(doubled_word)