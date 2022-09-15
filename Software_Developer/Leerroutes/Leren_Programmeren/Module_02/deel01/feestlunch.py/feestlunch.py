croissantjes = int() #17
stokbrood = int() #2
bonnen = int() #3
croissant_prijs = float()
stokbrood_prijs = float()
korting = float()

try:
    croissantjes = int(input("Hoeveel croissantjes wil je?"))
    croissant_prijs = float(input("Hoeveel kosten de croissantjes per stuk?"))
    stokbrood = int(input("Hoeveel stokbroden wil je?"))
    stokbrood_prijs = float(input("Hoeveel kosten de stokbrood per stuk?"))
    bonnen = int(input("Hoeveel kortingsbonnen heb je?"))
    korting = float(input("Hoeveel korting staat er op elke kortingsbon?"))
except:
    print("Je kan alleen cijfers invoeren, decimalen kunnen ook alleen bij het invoeren van de prijzen en de korting.")

croissant_totaal = croissantjes*croissant_prijs
stokbrood_totaal = stokbrood*stokbrood_prijs
korting_totaal = bonnen*korting

bruto = croissant_totaal + stokbrood_totaal

netto = bruto - korting_totaal

print(f"De feestlunch kost je bij de bakker {netto} euro voor de {croissantjes} croissantjes en de {stokbrood} stokbroden als de {korting:.0f} kortingsbonnen nog geldig zijn!")