def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


prime_sum = 0
non_prime_sum = 0

while True:
    input_value = input()

    if input_value == "stop":
        break

    try:
        number = int(input_value)
    except ValueError:
        print("Invalid input. Please enter a number or 'stop' to end.")
        continue

    if number < 0:
        print("Number is negative.")
        continue

    if is_prime(number):
        prime_sum += number
    else:
        non_prime_sum += number

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")