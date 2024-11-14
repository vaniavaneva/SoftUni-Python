path = input()
extension = path.split("\\")[-1]
name, extension = extension.split(".")
print(f"File name: {name}")
print(f"File extension: {extension}")