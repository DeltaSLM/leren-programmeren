def table(amount: int):
    for number in range(1, 11):
        print(f"{number} * {amount} = {number * amount}")

while not (answer := input("What number would you like to see the table of?")).isdigit():
    print("Please provide a number.")

table(int(answer))