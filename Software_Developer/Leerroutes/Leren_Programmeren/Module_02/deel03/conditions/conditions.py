a = int()
b = int()

try:
    a = int(input("Dit programma laat zien welk cijfer van twee groter is.\nGeef alstublieft cijfer A hier door."))
    b = int(input("Geef alstublieft cijfer B hier door."))
except:
    if ValueError:
        print("Geef alstublieft een nummer door. Letters kunnen niet worden gebruikt.")

if a > b:
    max = a
    print(f"A is het grootste getal: {max}")