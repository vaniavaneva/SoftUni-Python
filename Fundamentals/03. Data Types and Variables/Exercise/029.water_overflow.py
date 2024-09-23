lines = int(input())
capacity = 255
tank = 0
while lines > 0:
    liters = int(input())
    if tank + liters > capacity:
        print('Insufficient capacity!')
    else:
        tank += liters
    lines -= 1
print(tank)