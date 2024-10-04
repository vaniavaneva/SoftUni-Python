a = input()
b = input()


def range_ascii(a, b):
    start = ord(a)
    end = ord(b)
    if start > end:
        start, end = end, start
    result = [chr(i) for i in range(start + 1, end)]
    return ' '.join(result)


print(range_ascii(a, b))