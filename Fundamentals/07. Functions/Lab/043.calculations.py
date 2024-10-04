operator = input()
x = int(input())
y = int(input())


def math(operator):
    if operator == 'multiply':
        return x * y
    elif operator == 'divide':
        return x // y
    elif operator == 'add':
        return x + y
    elif operator == 'subtract':
        return x - y


print(math(operator))