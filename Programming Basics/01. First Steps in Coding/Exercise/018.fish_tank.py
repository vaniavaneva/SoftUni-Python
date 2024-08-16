length = int(input())
width = int(input())
height = int(input())
percent = float(input())
volume = length * width * height
needLitres = volume / 1000
print(needLitres * (1 - percent / 100))