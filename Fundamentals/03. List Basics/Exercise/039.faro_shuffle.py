string = input()
Cards = string.split()
shuffles = int(input())
for _ in range(shuffles):
    mid = len(Cards) // 2
    first = Cards[:mid]
    second = Cards[mid:]
    shuffledDeck = []
    for x in range(mid):
        shuffledDeck.append(first[x])
        shuffledDeck.append(second[x])
    Cards = shuffledDeck
print(Cards)