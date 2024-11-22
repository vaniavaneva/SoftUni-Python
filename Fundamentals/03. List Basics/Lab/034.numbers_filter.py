n = int(input())
List = []
filteredList = []
for _ in range(n):
    integer = int(input())
    List.append(integer)
action = input()
if action == 'even':
    for integer in List:
        if integer % 2 == 0:
            filteredList.append(integer)
elif action == 'odd':
    for integer in List:
        if integer % 2 != 0:
            filteredList.append(integer)
elif action == 'negative':
    for integer in List:
        if integer < 0:
            filteredList.append(integer)
elif action == 'positive':
    for integer in List:
        if integer >= 0:
            filteredList.append(integer)
print(filteredList)