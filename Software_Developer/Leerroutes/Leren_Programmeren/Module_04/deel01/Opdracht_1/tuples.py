days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

def day(typedays, ranges, reverse):
    if reverse == False:
        iteration = 0
    else:
        iteration = 6
    sentence = "All {} days in a week are: ".format(typedays)
    for  x in range(ranges):
        sentence += days[iteration] + (", " if iteration != (ranges-1 if  reverse=="False" else ranges+1) else "")
        if reverse == False:
            iteration += 1
        else:
            iteration -= 1

    return sentence

print(day("", 7,False))
print(day("work", 5,False))
print("All weekend days in a week are: ", days[5] + ", " + days[6])
print(day("", 7,True))
print(day("work", 7,True).replace("Sunday, Saturday, ", ""))
print(day("weekend",2,True))