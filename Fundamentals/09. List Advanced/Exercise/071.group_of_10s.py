def group_of_tens(string):
    numbers = list(map(int, string.split(", ")))
    group_boundary = 10
    max_number = max(numbers)
    results = []
    while group_boundary <= max_number:
        current_group = [n for n in numbers if n <= group_boundary]
        results.append(f"Group of {group_boundary}'s: {current_group}")
        numbers = [n for n in numbers if
                   n > group_boundary]
        group_boundary += 10
    if numbers:
        results.append(f"Group of {group_boundary}'s: {numbers}")
    for result in results:
        print(result)


string = input()
group_of_tens(string)