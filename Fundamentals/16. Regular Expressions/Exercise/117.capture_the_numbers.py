import re
all_numbers = []
while True:
    line = input().strip()
    if not line:
        break
    found_numbers = re.findall(r'\d+', line)
    all_numbers.extend(found_numbers)
print(" ".join(all_numbers))