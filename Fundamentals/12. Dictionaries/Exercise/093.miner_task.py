collection = {}
while True:
    name = input()
    if name == "stop":
        break
    quantity = int(input())
    collection[name] = collection.get(name, 0) + quantity
for resource, quantity in collection.items():
    print(f"{resource} -> {quantity}")