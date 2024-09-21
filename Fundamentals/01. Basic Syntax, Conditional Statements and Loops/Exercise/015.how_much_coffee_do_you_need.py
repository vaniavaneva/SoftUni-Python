coffee = 0
while True:
    command = input()
    if command == "END":
        break
    if command == "coding":
        coffee += 1
    elif command == "dog" or command == "cat":
        coffee += 1
    elif command == "movie":
        coffee += 1
    elif command.upper() == "CODING":
        coffee += 2
    elif command.upper() == "DOG" or command.upper() == "CAT":
        coffee += 2
    elif command.upper() == "MOVIE":
        coffee += 2
if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)