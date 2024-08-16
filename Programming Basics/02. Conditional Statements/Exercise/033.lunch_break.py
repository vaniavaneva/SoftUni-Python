import math
series = input()
episode = int(input())
breakTime = int(input())
lunch = breakTime / 8
rest = breakTime / 4
timeLeft = breakTime - lunch - rest
if timeLeft >= episode:
    print(f'You have enough time to watch {series}'
          f' and left with {math.ceil(timeLeft - episode)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series},"
          f" you need {math.ceil(episode - timeLeft)} more minutes.")