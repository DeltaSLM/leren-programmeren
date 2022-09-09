toegangsticket = 7.45
mensen = 4
GameSeat = 0.37
minuten = 5
minuten_totaal = 45


entree = mensen*toegangsticket
vr = minuten_totaal/minuten * GameSeat
vrtotaal = mensen*vr

totaalprijs = entree+vrtotaal

print(f"U totaalprijs van vandaag komt op {totaalprijs:.2f} euro.")