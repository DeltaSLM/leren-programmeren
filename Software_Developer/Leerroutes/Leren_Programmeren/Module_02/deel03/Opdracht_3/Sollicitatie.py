# Stel eerst alle vragen en ga daarna pas beoordelen aan de hand van de gegeven antwoorden of de kandidaat mag solliciteren.
#
# De kandidaat moet wel voldoen aan de volgende criteria:
#
#     Meer dan 4 jaar praktijkervaring met dieren-dressuur OF meer dan 5 jaar ervaring met jongleren OF meer dan 3 jaar praktijkervaring met acrobatiek
#     In bezit van een Diploma MBO-4 ondernemen
#     In bezit van een geldig Vrachtwagen rijbewijs
#     In bezit van een hoge hoed
#     Is man EN heeft Snor breder dan 10 cm OF is vrouw EN draagt rood krulhaar langer dan 20 cm.
#     Let op: Je hoeft alleen een man naar zijn snorlengte te vragen en alleen een vrouw naar haar krulhaarlengte.
#     Is langer dan 150 cm
#     Is zwaarder dan 90 kg
#     Heeft Certificaat “Overleven met gevaarlijk personeel”
#
# De vragen met getallen mogen de kritieke grens (zoals 4 jaar, of 150 cm) van een criterium niet verklappen.  Dus je vraagt bijvoorbeeld:
#
#     'Wat is uw lichaamsgewicht?’ in plaats van 'Weegt  u zwaarder dan 90kg? J/N’
#     ‘Hoeveel jaar praktijkervaring heeft u met dieren-dressuur?’ in plaats van 'Heeft u meer dan 4 jaar praktijkerbaring dieren-dressuur? J/N’
#
# Om de kandidaat te verwarren voeg je ook 4 vragen toe die er niet toe doen. Ga verder spelen met maffe criteria.

input("""
######################################################################################################################################
#                        Welkom bij de sollicitatieronde circusdirecteur voor circus HotelDeBotel.                                   #
#                   In deze ronde gaan we u een paar vragen stellen, of u door kan krijgt u erna te horen.                           #
#                       Beantwoord alle vragen eerlijk en druk op <ENTER> als u er klaar voor bent.                                  #
######################################################################################################################################
""")

def fail(failvar):
    if failvar == "ja" or failvar == "nee":
        pass
    else:
        print("Graag antwoorden met ja of nee.")
        exit()

try:
    dierenervaring = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? Voer 0 in als u er geen hebt."))
    jongleerervaring = int(input("Hoeveel jaar praktijkervaring heeft u met jongleren? Voer 0 in als u er geen hebt."))
    acrobatiekervaring = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? voer 0 in als u er geen hebt."))
    diploma = str(input("Bent u in bezit van een MBO 4 Diploma onderneming?"))
    fail(diploma)
    rijbewijs = str(input("Bent u in bezit van een C (Vrachtwagen) rijbewijs?"))
    fail(rijbewijs)
    hoed = str(input("Bent u in bezit van een hoge hoed?"))
    fail(hoed)
    gender = str(input("Bent u een man of een vrouw?")).lower()
    if gender == "man":
        snor = float(input("Hoe breed is uw gehele snor in centimeters?"))
        pass
    elif gender == "vrouw":
        haar = float(input("Wat is uw krulhaarlengte in centimeters?"))
        pass
    else:
        print("U kunt niet iets anders dan man of vrouw zijn.")
        exit()
    lengte = float(input("Wat is uw lengte?"))
    gewicht = float(input("Wat is uw gewicht?"))
    certificaat = str(input("Hebt u het certificaat Overleven met gevaarlijk personeel?"))
    fail(certificaat)
    ### De opvolgende vragen hebben niks ermee te doen, maar zijn om de sollicitant te verwarren
    leven = str(input("Wat is leven voor jou?"))
    tuin = str(input("Heb jij liever een tuin of een balkon?"))
    feestdag = str(input("Wat is jou favoriete feestdag?"))
    chocolade = str(input("Hou jij van chocolade?"))
    fail(chocolade)

except Exception as e:
    if TypeError:
        print("TypeError")

if dierenervaring > 4 or jongleerervaring > 5 or acrobatiekervaring > 3 and diploma == "ja" and rijbewijs == "ja" and "hoed" == "ja" and snor > 10 or haar > 20 and lengte > 150 and gewicht > 90 and certificaat == "ja":
    print("gefeliciteerd! U hebt de sollicitatie gehaald. Wij zouden graag met u nog een diepgaander interview doen. Laat alstublieft even weten via eenemail@bedrijf.nl wanneer u beschrikbaar bent.")
else:
    print("Ons excuses, maar u hebt de sollicitatie niet gehaald.")

