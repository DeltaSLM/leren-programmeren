input("""
######################################################################################################################################
#                                                                                        Welkom bij de sollicitatieronde circusdirecteur voor circus HotelDeBotel.                                                                                                                             #
#                                                                                  In deze ronde gaan we u een paar vragen stellen, of u door kan krijgt u erna te horen.                                                                                                             #
#                                                                                       Beantwoord alle vragen eerlijk en druk op <ENTER> als u er klaar voor bent.                                                                                                                       #
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

    if dierenervaring > 100 or jongleerervaring > 100 or acrobatiekervaring > 100:
        raise BaseException('Het is onmogelijk om meer dan 100 jaar ervaring te hebben in dieren-dressuur, jongleren en/of acrobatiek.')
except Exception as e:
    if ValueError:
        print("Voer een getal onder de 100 in")
        exit()
    elif BaseException:
        print(e)

diploma = input("Bent u in bezit van een MBO 4 Diploma onderneming?").lower()
fail(diploma)
rijbewijs = input("Bent u in bezit van een C (Vrachtwagen) rijbewijs?").lower()
fail(rijbewijs)
hoed = input("Bent u in bezit van een hoge hoed?").lower()
fail(hoed)
gender = input("Bent u een man of een vrouw?").lower()
if gender == "man":
    heeftsnor = input("Hebt u een snor?").lower()
    if heeftsnor == "ja":
        snor = float(input("Hoe breed is uw gehele snor in centimeters?"))
        pass
    else:
        pass
elif gender == "vrouw":
    heefthaar = input("Hebt u rood krulhaar?")
    if heefthaar == "ja":
        haar = float(input("Wat is uw krulhaarlengte in centimeters?"))
        pass
else:
    print("U kunt niet iets anders dan man of vrouw zijn.")
    exit()

try:
    lengte = float(input("Wat is uw lengte?"))
    if lengte < 170:
        raise BaseException("U bent nog kleiner dan een kabouter!")
        exit()
    gewicht = float(input("Wat is uw gewicht?"))
except Exception as e:
    if valueError:
       print( "Je moet in centimeters antwoorden.")
       exit()
    if BaseException:
        print(e)
        exit()

certificaat = input("Hebt u het certificaat Overleven met gevaarlijk personeel?").lower()
fail(certificaat)
### De opvolgende vragen hebben niks ermee te doen, maar zijn om de sollicitant te verwarren
leven = input("Wat is leven voor jou?")
tuin = input("Heb jij liever een tuin of een balkon?")
feestdag = input("Wat is jou favoriete feestdag?").lower()
if feestdag == "halloween":
    raise NameError('Halloween? In nederland? Dat vieren wij niet!!!')

chocolade = input("Hou jij van chocolade?").lower()
if chocolade == "nee":
    raise TypeError("Nee. Dat moest een typefout zijn. Chocolade is de holy grail.")
fail(chocolade)

if dierenervaring > 4 or jongleerervaring > 5 or acrobatiekervaring > 3 and diploma == "ja" and rijbewijs == "ja" and "hoed" == "ja" and snor > 10 or haar > 20 and lengte > 150 and gewicht > 90 and certificaat == "ja":
    print("gefeliciteerd! U hebt de sollicitatie gehaald. Wij zouden graag met u nog een diepgaander interview doen. Laat alstublieft even weten via eenemail@bedrijf.nl wanneer u beschrikbaar bent.")
else:
    print("Ons excuses, maar u hebt de sollicitatie niet gehaald.")