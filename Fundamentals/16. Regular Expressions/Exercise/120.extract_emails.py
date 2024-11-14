import re


def extract_emails(text):
    email_pattern = r'\b[a-zA-Z0-9]+([._-]?[a-zA-Z0-9]+)*@[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+\b'
    matches = re.finditer(email_pattern, text)
    for match in matches:
        print(match[0])


text_input = input()
extract_emails(text_input)