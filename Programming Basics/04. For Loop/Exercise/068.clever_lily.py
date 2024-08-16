years = int(input())
machineCost = float(input())
toyCost = int(input())
money = 10
saved = 0
toys = 0
brotherTax = 0
for i in range(1, years + 1):
    if i % 2 == 0:
        saved += money
        money += 10
        brotherTax += 1
    else:
        toys += 1
toysCost = toys * toyCost
budget = saved + toysCost - brotherTax
if machineCost <= budget:
    print(f'Yes! {budget - machineCost:.2f}')
else:
    print(f'No! {machineCost - budget:.2f}')
