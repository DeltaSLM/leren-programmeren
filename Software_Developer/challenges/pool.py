diepte = 8*3*1.5
print(diepte)

uitgraven = diepte*25
afvoeren = diepte*32.50

print(f"""
Offerte voor een zwembad van 8 bij 3 bij 1,5 meter (inhoud {diepte:.2f} m2)
Uitgraven:             {uitgraven:.2f}
Afvoeren grond: {afvoeren:.2f}
Totaal:                    {uitgraven+afvoeren:.2f}

""")