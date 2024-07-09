nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())
sumNylon = (nylon + 2) * 1.5
sumPaint = (paint + (paint * 0.1)) * 14.5
sumThinner = thinner * 5
sumHours = ((sumNylon + sumPaint + sumThinner + 0.40) * 0.3) * hours
print((sumNylon + sumPaint + sumThinner + 0.40) + sumHours)