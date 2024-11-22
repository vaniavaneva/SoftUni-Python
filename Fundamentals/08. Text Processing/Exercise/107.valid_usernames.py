usernames = input().split(", ")
for username in usernames:
    if 3 <= len(username) <= 16:
        if all(char.isalnum() or char in "-_" for char in username):
            print(username)