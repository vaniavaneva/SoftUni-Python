import re
furniture = []
total_cost = 0
while True:
    line = input()
    if line == "Purchase":
        break
    pattern = r">>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)"
    match = re.match(pattern, line)
    if match:
        name = match.group(1)
        price = float(match.group(2))
        quantity = int(match.group(4))
        furniture.append(name)
        total_cost += price * quantity
print("Bought furniture:")
for item in furniture:
    print(item)
print(f"Total money spend: {total_cost:.2f}")