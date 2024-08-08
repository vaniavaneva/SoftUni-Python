groups = int(input())
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0
everyone = 0
for i in range(groups):
    people = int(input())
    if people <= 5:
        musala += people
    if 6 <= people <= 12:
        monblan += people
    if 13 <= people <= 25:
        kilimanjaro += people
    if 26 <= people <= 40:
        k2 += people
    if people >= 41:
        everest += people
    everyone += people
print(f'{musala/everyone * 100:.2f}%')
print(f'{monblan/everyone * 100:.2f}%')
print(f'{kilimanjaro/everyone * 100:.2f}%')
print(f'{k2/everyone * 100:.2f}%')
print(f'{everest/everyone * 100:.2f}%')