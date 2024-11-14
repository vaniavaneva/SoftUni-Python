text = input()
while text != "end":
    reversed_text = ""
    for ch in reversed(text):
        reversed_text += ch
    print(text + " = " + reversed_text)
    text = input()