vacation = float(input())
puzzle = int(input())
doll = int(input())
teddy = int(input())
minion = int(input())
truck = int(input())
toys = puzzle + doll + teddy + minion + truck
puzzle *= 2.6
doll *= 3
teddy *= 4.1
minion *= 8.2
truck *= 2
sumLv = puzzle + doll + teddy + minion + truck
if toys >= 50:
    sumLv *= 0.75
rent = sumLv * 0.1
finalSum = sumLv - rent
if finalSum >= vacation:
    print(f'Yes! {finalSum - vacation:.2f} lv left.')
else:
    print(f'Not enough money! {vacation - finalSum:.2f} lv needed.')