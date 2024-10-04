string = input()
numbers = string.split()
absolute = [abs(float(_)) for _ in numbers]
print(absolute)