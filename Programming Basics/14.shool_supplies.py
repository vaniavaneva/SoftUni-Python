pens = int(input())
markers = int(input())
detergent = int(input())
discount = int(input())
Sum = pens * 5.8 + markers * 7.2 + detergent * 1.2
print(Sum - (Sum * discount / 100))