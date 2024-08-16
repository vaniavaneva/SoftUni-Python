dayNum = int(input())


def switch_case(dayNum):
    if dayNum == 1:
        return "Monday"
    elif dayNum == 2:
        return "Tuesday"
    elif dayNum == 3:
        return "Wednesday"
    elif dayNum == 4:
        return "Thursday"
    elif dayNum == 5:
        return "Friday"
    elif dayNum == 6:
        return "Saturday"
    elif dayNum == 7:
        return "Sunday"
    else:
        return "Error"


result = switch_case(dayNum)
print(result)
