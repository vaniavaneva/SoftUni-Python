registered = {}
command_count = int(input())
for _ in range(command_count):
    command = input().split()
    action = command[0]
    username = command[1]
    if action == "register":
        plate_number = command[2]
        if username in registered:
            print(f"ERROR: already registered with plate number {registered[username]}")
        else:
            registered[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
    elif action == "unregister":
        if username not in registered:
            print(f"ERROR: user {username} not found")
        else:
            del registered[username]
            print(f"{username} unregistered successfully")
for user, plate in registered.items():
    print(f"{user} => {plate}")