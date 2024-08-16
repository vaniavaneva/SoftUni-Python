actor = input()
points = float(input())
raters = int(input())
for i in range(raters):
    if points >= 1250.5:
        break
    name = input()
    pointsRater = float(input())
    points += (len(name) * pointsRater) / 2
if points >= 1250.5:
    print(f'Congratulations, {actor} got a nominee for leading role with {points:.1f}!')
else:
    print(f'Sorry, {actor} you need {1250.5 - points:.1f} more!')