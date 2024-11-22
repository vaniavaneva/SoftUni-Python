details = {}
while True:
    order_input = input()
    if order_input == "buy":
        break
    name, price, quantity = order_input.split()
    price = float(price)
    quantity = int(quantity)
    if name not in details:
        details[name] = {'price': price, 'quantity': 0}
    details[name]['quantity'] += quantity
    details[name]['price'] = price
for product, details in details.items():
    total_cost = details['price'] * details['quantity']
    print(f"{product} -> {total_cost:.2f}")