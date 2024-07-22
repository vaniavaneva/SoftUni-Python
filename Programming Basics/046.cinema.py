typeProjection = input()
rows = int(input())
columns = int(input())
if typeProjection == 'Premiere':
    print(f'{(rows * columns) * 12:.2f} leva')
elif typeProjection == 'Normal':
    print(f'{(rows * columns) * 7.5:.2f} leva')
elif typeProjection == 'Discount':
    print(f'{(rows * columns) * 5:.2f} leva')