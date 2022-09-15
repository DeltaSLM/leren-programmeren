import datetime

today = datetime.date.today().strftime("%H:%M:%S")
timenow = datetime.datetime.now().strftime("%H:%M:%S")
print(f"{today}\n{timenow}")
deadline = "00:00:00"
current_time = str(today) + " " + str(timenow)
start = datetime.datetime.strptime(current_time,'%H:%M:%S')
ends = datetime.datetime.strptime(deadline, '%H:%M:%S')

print(start - ends)