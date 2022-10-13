global lengte
global breedte
global hoogte

try:
    lengte = float(input("Wat is de lengte van het zwembad?").replace(",", "."))
    breedte = float(input("Wat is de breedte van het zwembad?").replace(",", "."))
    hoogte = float(input("Wat is de hoogte van het zwembad?").replace(",", "."))
except ValueError:
    print("Geef alstublieft een nummer door.")


diepte = lengte*breedte*hoogte
print(diepte)

uitgraven = diepte*25
afvoeren = diepte*32.50
voorrij = 250+(60*2.05) if  diepte > 20 else 100+(60*2.05)

m2 = lengte*breedte

print(f"""
Offerte voor een zwembad van 8 bij 3 bij 1,5 meter (inhoud {diepte:.2f} m2)
Uitgraven:            {uitgraven:.2f}
Afvoeren grond: {afvoeren:.2f}
Voorrijkosten:     {voorrij}
Totaal:                  {uitgraven+afvoeren+voorrij:.2f}

""")
