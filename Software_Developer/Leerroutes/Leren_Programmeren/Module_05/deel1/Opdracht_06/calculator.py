import functions

# variables
choice = ""
symbol = ""
execute = ""
noquit = True
n1 = float
n2 = float

while noquit:
    while not (choice == "a" or choice == "b" or choice == "c" or choice == "d" or choice == "e" or choice == "f" or choice == "g" or choice == "h"):
        if choice == "i":
            print("Stoppen...")
            noquit = False


        choice = input(f"""
{"wat wilt u doen" if not n1 else "Wat wilt u met de uitkomst doen?"}
A) getallen optellen
B) getallen aftrekken
C) getallen vermenigvuldigen
D) getallen delen
E) getal ophogen
F) getal verlagen
G) getal verdubbelen
H) getal halveren
{"I) niets" if n1 else ""}
Kies: """).lower()

    if not n1:
        try:
            n1 = float(input("Wat is het eerste getal?"))
        except ValueError:
            print("We hebben een getal (optioneel met decimalen) nodig.")

    if choice != "e" and choice != "f" and choice != "g" and choice != "h":
        try:
            n2 = float(input("Wat is het tweede getal?"))
        except ValueError:
            print("We hebben een getal (optioneel met decimalen) nodig.")

    elif choice == "e" or choice == "f":
        n2 = 1
    else:
        n2 = 2

    if choice == "a":
        execute = functions.addition(n1, n2)
        symbol = "+"
    elif choice == "b":
        execute = functions.subtraction(n1, n2)
        symbol = "-"
    elif choice == "c":
        execute = functions.multiplication(n1, n2)
        symbol = "*"
    elif choice == "d":
        execute = functions.division(n1, n2)
        symbol = "/"
    elif choice == "e":
        execute = functions.addition(n1, n2)
        symbol = "+"
    elif choice == "f":
        execute = functions.subtraction(n1, n2)
        symbol = "-"
    elif choice == "g":
        execute = functions.multiplication(n1, n2)
        symbol = "*"
    elif choice == "h":
        execute = functions.division(n1, n2)
        symbol = "/"

    answer = execute

    print(f"{n1} {symbol} {n2} = {answer}")
    n1 = answer
    choice = ""
