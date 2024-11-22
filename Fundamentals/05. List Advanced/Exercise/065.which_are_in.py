string1 = input()
string2 = input()


def substrings(string1, string2):
    list1 = string1.split(', ')
    list2 = string2.split(', ')
    result = []
    for substring in list1:
        if any(substring in List for List in list2):
            result.append(substring)
    return result


output = substrings(string1, string2)
print(output)