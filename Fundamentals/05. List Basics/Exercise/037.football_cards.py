A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
terminated = False
cards = input().split()
for card in cards:
    team, player = card.split('-')
    player = int(player)
    if team == 'A' and player in A:
        A.remove(player)
    elif team == 'B' and player in B:
        B.remove(player)
    if len(A) < 7 or len(B) < 7:
        terminated = True
        break
print(f"Team A - {len(A)}; Team B - {len(B)}")
if terminated:
    print("Game was terminated")
