phonebook = {}
while True:
    num = input()
    if num.isdigit():
        count = int(num)
        break
    name, number = num.split('-')
    phonebook[name] = number
for _ in range(count):
    search = input()
    if search in phonebook:
        print(f"{search} -> {phonebook[search]}")
    else:
        print(f"Contact {search} does not exist.")