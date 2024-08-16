floors = int(input())
rooms = int(input())
lastFloor = floors
while floors != 0:
    if floors == lastFloor:
        number = floors * 10
        for i in range(rooms):
            print(f"L{number}", end=" ")
            number += 1
        print()
    elif floors % 2 == 0:
        number = floors * 10
        for i in range(rooms):
            print(f"O{number}", end=" ")
            number += 1
        print()
    elif floors % 2 != 0:
        number = floors * 10
        for i in range(rooms):
            print(f"A{number}", end=" ")
            number += 1
        print()
    floors -= 1