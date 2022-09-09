toegangsticket = 7.45
mensen = 4
GameSeat = 0.37
minuten = 5
minuten_totaal = 45


entree = mensen*toegangsticket
vr = minuten_totaal/minuten * GameSeat
vrtotaal = mensen*vr

totaalprijs = entree+vrtotaal

print(f"Dit geweldige dagje-uit met {mensen} mensen in de Speelhal met {minuten_totaal} minuten VR kost je maar {totaalprijs:.2f} euro")