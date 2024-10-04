def even(num):
    return num % 2 == 0


num = input().split()
even_nums = map(int, num)
nums = list(filter(even, even_nums))
print(nums)