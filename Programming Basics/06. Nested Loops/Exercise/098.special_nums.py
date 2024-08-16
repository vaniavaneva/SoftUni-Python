N = int(input())

first_output = True

for number in range(1111, 10000):
    num_str = str(number)

    is_special = True

    for char in num_str:
        digit = int(char)

        if digit == 0:
            is_special = False
            break

        if N % digit != 0:
            is_special = False
            break

    if is_special:
        if first_output:
            print(number, end="")
            first_output = False
        else:
            print(" ", end="")
            print(number, end="")

print()