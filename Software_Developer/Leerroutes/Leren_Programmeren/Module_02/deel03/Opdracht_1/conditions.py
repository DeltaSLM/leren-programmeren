

try:
    a = int(input("Dit programma laat zien welk cijfer van twee groter is.\nGeef alstublieft cijfer A hier door."))
    b = int(input("Geef alstublieft cijfer B hier door."))
except:
    if ValueError:
        print("Geef alstublieft een nummer door. Letters kunnen niet worden gebruikt.")

if a > b:
    max = a
    min = b
    print(f"A is het grootste getal: {max}")
    print(f"Het minimum is: {min}")
    print(f"Het maximum is {max}")

elif a < b:
    min = a
    max = b
    print(f"A is het kleinste getal: {min}")
    print(f"Het minimum is: {min}")
    print(f"Het maximum is {max}")

else:
    print("A en B zijn even groot")