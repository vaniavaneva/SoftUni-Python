day = input()


def switch_case(day):
    if day == "Monday" or day == "Tuesday" or \
            day == "Wednesday" or day == "Thursday" or day == "Friday":
        return "Working day"
    elif day == "Saturday" or day == "Sunday":
        return "Weekend"
    else:
        return "Error"


result = switch_case(day)
print(result)