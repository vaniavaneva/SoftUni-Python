x = input()


def palindrome(num):
    return str(num) == str(num)[::-1]


def check(string):
    numbers = string.split(", ")
    results = [palindrome(num) for num in numbers]
    for result in results:
        print(result)


check(x)