movie = input()
standard = 0
student = 0
kid = 0
all = 0
movieTickets = 0
while movie != 'Finish':
    space = int(input())
    spaceSave = space
    ticket = input()
    while ticket != 'End' or space == 0:
        if ticket == 'standard':
            standard += 1
        if ticket == 'student':
            student += 1
        if ticket == 'kid':
            kid += 1
        all += 1
        movieTickets += 1
        space -= 1
        if space == 0:
            break
        ticket = input()
    print(f'{movie} - {movieTickets / spaceSave * 100:.2f}% full.')
    movieTickets = 0
    movie = input()
    if movie == 'Finish':
        break
print(f'Total tickets: {all}')
print(f'{student / all * 100:.2f}% student tickets.')
print(f'{standard / all * 100:.2f}% standard tickets.')
print(f'{kid / all * 100:.2f}% kids tickets.')
