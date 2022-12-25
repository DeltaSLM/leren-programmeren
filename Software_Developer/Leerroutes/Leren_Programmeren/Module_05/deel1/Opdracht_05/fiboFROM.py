# alternatief hieronder

def fibo(minimum: int) -> str:
    n1, n2 = 0, 1
    count = 0
    sequence = ""
    while count < 100:
        if n1 > minimum:
            sequence += (str(n1) if sequence == "" else ", {}".format(n1))
            count += 1
        nth = n1 + n2
        n1 = n2
        n2 = nth
    return sequence


while not (amount := input("From what number would you like for us to print?")).isdigit():
    print("Please provide a NUMBER, thank you.")

print(fibo(int(amount)))
