string = input()
count = {}
for char in string:
    if char != " ":
        count[char] = count.get(char, 0) + 1
for char, count in count.items():
    print(f"{char} -> {count}")