givenday = input("Please provide me with the full name of a day.").lower()

if givenday == "monday" or givenday == "tuesday" or givenday == "wednesday" or givenday == "thursday" or givenday == "friday" or givenday == "saturday" or givenday == "sunday":
    pass
else:
    print("Please provide a full day's name such as Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday.")
    exit()

weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

days = 0

while givenday != weekdays[days]:
    print(weekdays[days])
    days += 1

print(givenday)