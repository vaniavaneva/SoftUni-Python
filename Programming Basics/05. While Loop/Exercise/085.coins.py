change = float(input())
change = round(change * 100)
coins = 0
while change > 0:
    if change >= 200:
        change -= 200
        coins += 1
    elif change >= 100:
        change -= 100
        coins += 1
    elif change >= 50:
        change -= 50
        coins += 1
    elif change >= 20:
        change -= 20
        coins += 1
    elif change >= 10:
        change -= 10
        coins += 1
    elif change >= 5:
        change -= 5
        coins += 1
    elif change >= 2:
        change -= 2
        coins += 1
    elif change >= 1:
        change -= 1
        coins += 1

print(coins)