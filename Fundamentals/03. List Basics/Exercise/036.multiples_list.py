factor = int(input())
count = int(input())
List = []
number = 0
for _ in range(count):
    number += factor
    List.append(number)
print(List)