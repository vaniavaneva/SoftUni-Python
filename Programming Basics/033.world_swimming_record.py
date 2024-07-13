recordSec = float(input())
meters = float(input())
metSec = float(input())
extraSec = (meters // 15) * 12.5
sumSec = (meters * metSec) + extraSec
if sumSec < recordSec:
    print(f'Yes, he succeeded! The new world record is {sumSec:.2f} seconds.')
else:
    print(f'No, he failed! He was {sumSec - recordSec:.2f} seconds slower.')