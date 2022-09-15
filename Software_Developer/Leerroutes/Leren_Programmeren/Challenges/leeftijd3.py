try:
    leeftijd = int(input("Wat is jouw leeftijd?"))

    if leeftijd > 100:
        print("Nee. Je kan niet zo oud zijn.")
        exit()
    if leeftijd < 10:
        print("Je bent geen kleuter.")
        exit()

    nieuw = 3 * leeftijd

    print(f"Was je 3 keer ouder, had je {nieuw} geweest")
except:
    if ValueError:
        print("Je kan geen getal oud zijn.")