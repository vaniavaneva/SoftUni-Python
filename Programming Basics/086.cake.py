length = int(input())
width = int(input())
pieces = length * width
while pieces > 0:
    take = input()
    if take == 'STOP':
        print(f'{pieces} pieces are left.')
        break
    take = int(take)
    pieces -= take
if pieces <= 0:
    print(f'No more cake left! You need {abs(pieces)} pieces more.')