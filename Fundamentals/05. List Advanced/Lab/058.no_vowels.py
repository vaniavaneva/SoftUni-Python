string = input()
vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']
List = ''.join([x for x in string if x not in vowels])
print(List)
