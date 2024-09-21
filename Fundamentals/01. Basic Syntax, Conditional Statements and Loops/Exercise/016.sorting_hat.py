name = input()
while name != 'Welcome!' or name != 'Voldemort':
    char = 0
    if name == 'Welcome!':
        print('Welcome to Hogwarts.')
        break
    if name == 'Voldemort':
        print('You must not speak of that name!')
        break
    for _ in range(len(name)):
        char += 1
    if char < 5:
        print(f'{name} goes to Gryffindor.')
    elif char == 5:
        print(f'{name} goes to Slytherin.')
    elif char == 6:
        print(f'{name} goes to Ravenclaw.')
    elif char > 6:
        print(f'{name} goes to Hufflepuff.')
    name = input()