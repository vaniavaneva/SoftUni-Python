rooms = int(input())
total = 0
need_chairs = False
for room in range(1, rooms + 1):
    string = input()
    parts = string.split()
    chairs = len(parts[0])
    visitors = int(parts[1])
    if visitors > chairs:
        needed = visitors - chairs
        print(f"{needed} more chairs needed in room {room}")
        need_chairs = True
    else:
        free = chairs - visitors
        total += free
if not need_chairs:
    print(f"Game On, {total} free chairs left")