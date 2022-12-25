def fibo(maximum: int) -> str:
    n1, n2 = 0, 1
    sequence = ""
    while n1 < int(maximum):
        sequence += (", {}".format(n1) if n1 > 0 else "{}".format(n1))
        nth = n1 + n2
        n1 = n2
        n2 = nth
    return sequence


while not (amount := input("To what number would you like for us to print?")).isdigit():
    print("Please provide a NUMBER, thank you.")

print(fibo(int(amount)))
