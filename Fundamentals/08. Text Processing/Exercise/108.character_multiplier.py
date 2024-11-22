str1, str2 = input().split()
total = 0
min_length = min(len(str1), len(str2))
for i in range(min_length):
    total += ord(str1[i]) * ord(str2[i])
for i in range(min_length, len(str1)):
    total += ord(str1[i])
for i in range(min_length, len(str2)):
    total += ord(str2[i])
print(total)