_ = input()
toDoList = [0] * 10
x = 0
while _ != 'End':
    command = _.split('-')
    importance = int(command[0]) - 1
    action = command[1]
    toDoList.pop(importance)
    toDoList.insert(importance, action)
    _ = input()
result = [element for element in toDoList if element != 0]
print(result)