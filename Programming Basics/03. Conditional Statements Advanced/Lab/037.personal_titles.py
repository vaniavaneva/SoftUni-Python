years = float(input())
gender = input()
if gender == "m":
    if years >= 16:
        print("Mr.")
    else:
        print("Master")
else:
    if years >= 16:
        print("Ms.")
    else:
        print("Miss")