def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


while not (nterms := input("Please provide the term to which to print.")).isdigit() >= 0:
    print("We need a NUMBER.")
else:
    print(f"Fibonacci sequence:{' This may take a while' if int(nterms) > 50 else ''}")
    for i in range(int(nterms)):
        print(recur_fibo(i))