n = int(input())
while n > 0:
    message = int(input())
    if message == 88:
        print('Hello')
    elif message == 86:
        print('How are you?')
    elif message < 88 and message != 86:
        print('GREAT!')
    elif message > 88:
        print('Bye.')
    n -= 1