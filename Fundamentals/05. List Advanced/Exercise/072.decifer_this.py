def decipher(secret):
    words = secret.split()
    decoded = []
    for word in words:
        first_part = ''
        i = 0
        while i < len(word) and word[i].isdigit():
            first_part += word[i]
            i += 1
        first_letter = chr(int(first_part))
        if len(word) > len(first_part):
            rest_of_word = word[len(first_part):]
            if len(rest_of_word) > 1:
                second_letter = rest_of_word[0]
                last_letter = rest_of_word[-1]
                middle_part = rest_of_word[1:-1]
                new_word = first_letter + last_letter + middle_part + second_letter
            else:
                new_word = first_letter + rest_of_word
        else:
            new_word = first_letter
        decoded.append(new_word)
    return ' '.join(decoded)


secret_input = input()
decoded_output = decipher(secret_input)
print(decoded_output)