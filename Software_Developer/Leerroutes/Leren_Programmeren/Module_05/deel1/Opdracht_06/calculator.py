answer = ""

def addition(number1 : int, number2 : int) -> str:
    answer = f"{number1} + {number2} = {number1+number2}"
    return answer

def subtraction(number1 : int, number2 : int) -> str:
    return ""

def multiplication(number1 : int, number2 : int) -> str:
    return ""

def division(number1 : int, number2 : int) -> str:
    return ""

def increase(number1: int) -> str:
    return ""

def decrease(number1: int) -> str:
    return ""

def double(number1: int) -> str:
    return ""

def half(number1: int) -> str:
    return ""

choice = ""
n2 = int

while not (choice == "a" or choice == "b" or choice == "c" or choice == "d" or choice == "e" or choice == "f" or choice == "g" or choice == "h"):
    choice = input("""
Wat wilt u doen?
A) getallen optellen
B) getallen aftrekken
C) getallen vermenigvuldigen
D) getallen delen
E) getal ophogen
F) getal verlagen
G) getal verdubbelen
H) getal halveren
""").lower()

while not (n1 := input("Wat is het eerste nummer?")).isdigit():
    print("NUMMER alstublieft.")
n1 = int(n1)

if choice == "a" or choice == "b" or choice == "c" or choice == "d":
    while not (n2 := input("Wat is het tweede nummer?")).isdigit():
        print("NUMMER alstublieft.")
    n2 = int(n2)

def type():
    if choice == "a":
        addition(n1, n2)
    elif choice == "b":
        subtraction(n1, n2)
    elif choice == "c":
        multiplication(n1, n2)
    elif choice == "d":
        division(n1, n2)
    elif choice == "e":
        increase(n1)
    elif choice == "f":
        decrease(n1)
    elif choice == "g":
        double(n1)
    elif choice == "h":
        half(n1)

print(type())