animal = input()


def switch(animal):
    if animal == "dog":
        return "mammal"
    elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
        return "reptile"
    else:
        return "unknown"


result = switch(animal)
print(result)