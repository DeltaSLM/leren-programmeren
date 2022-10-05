try:
    number = int(input("Provide me with a number."))
    if number == 0:
        raise ValueError
except ValueError:
    print("We need a number above 0.")
    exit()


for x in range(1, 11):
    print(f"{x}*{number}={x*number}")