import re

naam = input("Wat is jou naam?")
address = input("Geregistreerd. Wat is jou adres?")
postcode = input("Geregistreerd. Wat is jou postcode?").upper()

postcode = re.search("^\d{4}\s?[A-Z]{2}$", postcode)

if postcode == None:
    print("Geef een viernummerig, twee letter postcode, zoals 0000BS.")
    exit()
else:
    postcode = postcode

woon = input("Geregistreerd. Wat is jou woonplaats?")

print(f"""
 ----------------------------------------------------
|  Naam      : {naam}
|  Adres     : {address}
|  Postcode  : {postcode[0]}
|  Woonplaats: {woon}
 ----------------------------------------------------
""")