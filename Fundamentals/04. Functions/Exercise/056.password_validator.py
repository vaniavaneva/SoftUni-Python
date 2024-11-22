def validate(password):
    error = []
    if not (6 <= len(password) <= 10):
        error.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        error.append("Password must consist only of letters and digits")
    count = sum(char.isdigit() for char in password)
    if count < 2:
        error.append("Password must have at least 2 digits")
    if error:
        print("\n".join(error))
    else:
        print("Password is valid")


user_input = input()
validate(user_input)