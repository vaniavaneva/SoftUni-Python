book = input()
count = 0
found = False
current = input()
while current != 'No More Books':
    if current == book:
        found = True
        print(f'You checked {count} books and found it.')
        break
    count += 1
    current = input()
if not found:
    print('The book you search is not here!')
    print(f'You checked {count} books.')