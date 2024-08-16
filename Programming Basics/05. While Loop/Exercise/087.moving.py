weight = int(input())
length = int(input())
height = int(input())
volume = weight * length * height
while volume > 0:
    boxes = input()
    if boxes == 'Done':
        print(f'{volume} Cubic meters left.')
        break
    boxes = int(boxes)
    volume -= boxes
if volume <= 0:
    print(f'No more free space! You need '
          f'{abs(volume)} Cubic meters more.')