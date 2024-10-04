def sum_eo(num, odd, even):
    for _ in (num):
        _ = int(_)
        if _ % 2 == 0:
            even += _
        else:
            odd += _
    return f'Odd sum = {odd}, Even sum = {even}'


num = input()
odd = 0
even = 0
print(sum_eo(num, odd, even))