num1 = float(input())
if num1 <= 10:
    print('slow')
elif 10 < num1 <= 50:
    print('average')
elif 50 < num1 <= 150:
    print('fast')
elif 150 < num1 <= 1000:
    print('ultra fast')
else:
    print('extremely fast')
