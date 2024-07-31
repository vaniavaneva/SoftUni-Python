examHour = int(input("Enter exam hour: "))
examMinute = int(input("Enter exam minute: "))
arrivalHour = int(input("Enter arrival hour: "))
arrivalMinute = int(input("Enter arrival minute: "))
examTime = examHour * 60 + examMinute
arrivalTime = arrivalHour * 60 + arrivalMinute
timeDiff = arrivalTime - examTime
if timeDiff > 0:
    print("Late")
    if timeDiff < 60:
        print(f"{timeDiff} minutes after the start")
    else:
        hours = timeDiff // 60
        minutes = timeDiff % 60
        print(f"{hours}:{minutes:02d} hours after the start")
elif -30 <= timeDiff <= 0:
    print("On time")
    if timeDiff < 0:
        print(f"{abs(timeDiff)} minutes before the start")
else:
    print("Early")
    timeDiff = abs(timeDiff)
    if timeDiff < 60:
        print(f"{timeDiff} minutes before the start")
    else:
        hours = timeDiff // 60
        minutes = timeDiff % 60
        print(f"{hours}:{minutes:02d} hours before the start")