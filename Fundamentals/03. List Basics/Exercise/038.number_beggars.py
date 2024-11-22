string = input()
beggars = int(input())
String = [int(x) for x in string.split(', ')]
Beggars = [0] * beggars
for _ in range(len(String)):
    Beggars_index = _ % beggars
    Beggars[Beggars_index] += String[_]
print(Beggars)