croissantjes = 17
stokbrood = 2
korting = 3

croissant_total = croissantjes*0.39
stokbrood_total = stokbrood*2.78
korting_total = korting*0.50

bruto = croissant_total + stokbrood_total

netto = bruto - korting_total

# Old print from Version 1.0.0
# print(f"""
# --------------------------------------------
# croissant {croissantjes}x {croissant_total}
# stokbrood {stokbrood}x {stokbrood_total}
# --------------------------------------------
# Beginprijs: {bruto}
# Korting -{korting_total:.2f}
# --------------------------------------------
# Eindprijs: {netto}
# """)

print(f"De feestlunch kost je bij de bakker {netto} euro voor de {croissantjes} croissantjes en de {stokbrood} stokbroden als de {korting} kortingsbonnen nog geldig zijn!")