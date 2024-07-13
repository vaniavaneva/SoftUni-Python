# budget = float(input())
# n = int(input())
# m = int(input())
# p = int(input())
# n *= 250
# m *= n * 0.35
# p *= n * 0.1
# finalSum = n + m + p
# if n > m:
#     finalSum *= 0.85
# if finalSum <= budget:
#     print(f'You have {budget - finalSum:.2f} leva left!')
# else:
#     print(f'Not enough money! You need {finalSum - budget:.2f} leva more!')

budget = float(input())
n = int(input())
m = int(input())
p = int(input())
nCost = n * 250
mCost = (nCost * 0.35) * m
pCost = (nCost * 0.1) * p
finalSum = nCost + mCost + pCost
if n > m:
    finalSum *= 0.85
if finalSum <= budget:
    print(f'You have {budget - finalSum:.2f} leva left!')
else:
    print(f'Not enough money! You need {finalSum - budget:.2f} leva more!')

