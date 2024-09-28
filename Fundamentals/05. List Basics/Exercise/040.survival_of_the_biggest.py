input_numbers = input()
n = int(input())
numbers = list(map(int, input_numbers.split()))
sorted_numbers = sorted(numbers)
numbers_to_remove = sorted_numbers[:n]
remaining_numbers = [num for num in numbers if num not in numbers_to_remove]
result = ", ".join(map(str, remaining_numbers))
print(result)