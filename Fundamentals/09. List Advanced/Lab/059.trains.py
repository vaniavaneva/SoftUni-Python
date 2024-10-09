wagons = int(input())
train = [0] * wagons
_ = input()
while _ != 'End':
    word = _.split(' ')
    key_word = word[0]
    people = word[1]
    people = int(people)
    if key_word == 'add':
        train[-1] += people
    elif key_word == 'insert':
        index = int(word[1])
        people = int(word[2])
        train[index] += people
    elif key_word == 'leave':
        index = int(word[1])
        people = int(word[2])
        train[index] -= people
    _ = input()
print(train)