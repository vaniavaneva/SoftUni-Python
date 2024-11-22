string = input()
List = [int(x) for x in string.split()]
print(f'The minimum number is {min(List)}')
print(f'The maximum number is {max(List)}')
print(f'The sum number is: {sum(List)}')