string = input()
pos = [num for num in string.split(', ') if int(num) >= 0]
neg = [num for num in string.split(', ') if int(num) < 0]
even = [num for num in string.split(', ') if int(num) % 2 == 0]
odd = [num for num in string.split(', ') if int(num) % 2 == 1]
print("Positive:", ', '.join(pos))
print("Negative:", ', '.join(neg))
print("Even:", ', '.join(even))
print("Odd:", ', '.join(odd))