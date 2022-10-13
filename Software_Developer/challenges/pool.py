diepte = 8*3*1.5
print(diepte)

uitgraven = diepte*25
afvoeren = diepte*32.50
voorrij = 250+(60*2.05)

print(f"""
Offerte voor een zwembad van 8 bij 3 bij 1,5 meter (inhoud {diepte:.2f} m2)
Uitgraven:            {uitgraven:.2f}
Afvoeren grond: {afvoeren:.2f}
Voorrijkosten:     {voorrij}
Totaal:                  {uitgraven+afvoeren+voorrij:.2f}

""")
