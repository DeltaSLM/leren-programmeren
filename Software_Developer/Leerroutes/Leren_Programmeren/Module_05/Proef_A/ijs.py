bestelling = True

print("Welkom bij Papi Gelato, je mag alle smaken kiezen zolang het maar vanille ijs is")

while bestelling:
    waarin = ""
    opnieuw = ""

    while not (bolletjes := input("Hoeveel bolletjes wilt u?")):
        print("Sorry, dat snap ik niet")

    bolletjes = int(bolletjes)

    if bolletjes > 8 or bolletjes < 1:
        if bolletjes > 8:
            print("Onze bakjes zijn niet groot genoeg voor meer dan 8 bolletjes.")
        elif bolletjes < 1:
            print("Je kan alleen kiezen tussen 1 tot en met 8 bolletjes.")

    elif bolletjes <= 3:
        while not (waarin == "hoorntje" or waarin == "bakje"):
            if waarin != "":
                print("Sorry, dit snap ik niet.")
            waarin = input("Wilt u dit in een hoorntje of in een bakje?")

    elif bolletjes >= 4 and bolletjes <= 8:
        waarin = "bakje"
        print(f"Dan krijgt u van mij een bakje met {bolletjes} bolletjes!")

    if bolletjes <= 8 and bolletjes >= 1:
        print(f"Hier is uw {waarin} met {bolletjes} bolletjes.")

        while not (opnieuw == "j" or opnieuw == "n"):
            if opnieuw != "":
                print("Sorry, dat snap ik niet.")
            opnieuw = input("Wilt u nog meer bestellen? J/N").lower()

        if opnieuw == "j":
            waarin = ""
            opnieuw = ""
        elif opnieuw == "n":
            bestelling = False
            print("Bedankt en tot ziens!")