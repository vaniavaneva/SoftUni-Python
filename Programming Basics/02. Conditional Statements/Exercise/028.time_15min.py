hours = int(input())
minutes = int(input())
minutes += 15
if minutes >= 60:
    hours += 1
    minutes -= 60
if hours >= 24:
    hours -= 24
formatted_minutes = f'{minutes:02}'
print(f'{hours}:{formatted_minutes}')