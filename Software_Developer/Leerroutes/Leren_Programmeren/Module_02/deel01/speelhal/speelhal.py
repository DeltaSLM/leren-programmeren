# toegangsticket = 7.45
# mensen = 4
# GameSeat = 0.37
# minuten = 5
# minuten_totaal = 45


# entree = mensen*toegangsticket
# vr = minuten_totaal/minuten * GameSeat
# vrtotaal = mensen*vr

# totaalprijs = entree+vrtotaal


# Hoeveel mensen hebben tickets nodig * de ticket prijs


# print(f"Dit geweldige dagje-uit met {int(input('met hoeveel mensen ga je?'))} mensen in de Speelhal met {minuten_totaal} minuten VR kost je maar {totaalprijs:.2f} euro")

mensen = int()
vrmensen = int()
vrminuten = int()
ticket = float()
gameprijs = float()
gameminuten = int()

try:
     mensen = int(input("Met hoeveel mensen ga je?"))
     ticket = float(input("Hoeveel euro moeten de tickets zijn?").replace(",", "."))
     gameprijs = float(input("Hoeveel euro moet de gameseat zijn? De hoeveelheid minuten kan in de volgende vraag worden beantwoord.").replace(",", "."))
     gameminuten = int(input(f"Hoeveel minuten per {gameprijs} euro?"))
     vrmensen = int(input("Hoeveel van jullie gaan in de GameSeat?"))
     vrminuten = int(input("Hoeveel minuten gaat ieder persoon gemiddeld op de GameSeat?"))
except:
     if ValueError:
          print("Geef alstublieft antwoord in cijfers.")
          exit()

if vrmensen > mensen:
     print("Er kunnen niet meer mensen in de GameSeat dan dat je tickets hebt.")
     exit()



ticket = ticket / 100
gameprijs = gameprijs / 100
toegang = mensen * (ticket * 100)
VR = vrmensen * vrminuten / gameminuten * (gameprijs * 100)
totaal = toegang+VR
print(f"Dit dagje uit met {mensen} mensen en {vrminuten} vr minuten per persoon kost je maar {totaal} euro.")