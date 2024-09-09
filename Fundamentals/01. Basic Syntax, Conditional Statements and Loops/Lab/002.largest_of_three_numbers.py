import sys
first = int(input())
second = int(input())
third = int(input())
max_num = -sys.maxsize
if first > max_num:
    max_num = first
if second > max_num:
    max_num = second
if third > max_num:
    max_num = third
print(max_num)