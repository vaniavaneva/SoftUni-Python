tabs = int(input())
salary = int(input())

for i in range(tabs):
    if salary <= 0:
        break
    tab = input()
    if tab == 'Facebook':
        salary -= 150
    elif tab == 'Instagram':
        salary -= 100
    elif tab == 'Reddit':
        salary -= 50

if salary <= 0:
    print('You have lost your salary.')
else:
    print(f'{salary}')
