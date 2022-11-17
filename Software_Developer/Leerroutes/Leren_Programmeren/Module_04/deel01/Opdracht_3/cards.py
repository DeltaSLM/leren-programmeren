import random

kleuren = ("harten", "klaveren", "schoppen", "ruiten")
types = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas")
deckextra = ("joker", "joker")
deck = []
kleurenrange = 0
cardsrange = 0

for y in range(4):
    typesrange = 0
    for x in range(13):
        deck.append(kleuren[kleurenrange] + " " + types[typesrange])
        typesrange += 1
    kleurenrange += 1
    deck.append("joker") if y < 2 else None
random.shuffle(deck)

for x in range(7):
    print(f"Kaart {cardsrange+1}: " + deck[kleurenrange])
    deck.remove(deck[cardsrange])
    cardsrange += 1

print(f"\nDeck ({len(deck)} kaarten): {', '.join(deck)}")