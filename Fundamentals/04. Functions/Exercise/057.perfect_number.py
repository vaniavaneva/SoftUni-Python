def perfect(n):
    sum_div = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum_div += i
    if sum_div == n:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
result = perfect(number)
print(result)