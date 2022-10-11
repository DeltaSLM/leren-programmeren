tijd = 1

while tijd != 25:
    if tijd > 12:
        format = "PM"
    else:
        format = "AM"

    print(tijd, format)
    tijd += 1