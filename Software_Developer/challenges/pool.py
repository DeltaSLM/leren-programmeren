global lengte
global breedte
global hoogte

try:
    lengte = float(input("Wat is de lengte van het zwembad?").replace(",", "."))
    breedte = float(input("Wat is de breedte van het zwembad?").replace(",", "."))
    hoogte = float(input("Wat is de diepte van het zwembad?").replace(",", "."))
except ValueError:
    print("Geef alstublieft een nummer door.")
    exit()

diepte = lengte*breedte*hoogte
print(diepte)

uitgraven = diepte*25
afvoeren = diepte*32.50
voorrij = 250+(60*2.05) if  diepte > 20 else 100+(60*2.05)

m2 = lengte*breedte
betontegel = m2*200+m2*20 if diepte >= 20 else m2*250+m2*25

print(f"""
Offerte voor een zwembad van {lengte} bij {breedte} bij {hoogte} meter (inhoud {diepte:.2f} m2)
Uitgraven:                     {uitgraven:.2f}
Afvoeren grond:          {afvoeren:.2f}
Voorrijkosten:              {voorrij}
Beton + tegel ({m2}): {betontegel}
Totaal:                           {uitgraven+afvoeren+voorrij+betontegel:.2f}

""")
