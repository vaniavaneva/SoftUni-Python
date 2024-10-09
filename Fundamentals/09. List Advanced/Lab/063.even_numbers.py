nums = list(map(int, input().split(', ')))
found = map(
    lambda x: x if nums[x] % 2 == 0 else 'no',
    range(len(nums))
)
even = list(filter(lambda a: a != 'no', found))
print(even)