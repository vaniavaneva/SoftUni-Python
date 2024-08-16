tournaments = int(input())
starterPoints = int(input())
points = 0
won = 0
for i in range(tournaments):
    placement = input()
    if placement == 'W':
        points += 2000
        won += 1
    if placement == 'F':
        points += 1200
    if placement == 'SF':
        points += 720
averagePoints = points // tournaments
print(f'Final points: {points + starterPoints}')
print(f'Average points: {averagePoints:.0f}')
print(f'{won / tournaments * 100:.2f}%')