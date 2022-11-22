import random

kleuren = ("harten", "klaveren", "schoppen", "ruiten")
types = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas")
deckextra = ("joker", "joker")
deck = []

for y in range(4):
    typesrange = 0
    for x in range(13):
        deck.append(kleuren[y] + " " + types[x])
    deck.append("joker") if y < 2 else None
random.shuffle(deck)

for x in range(7):
    print(f"Kaart {x+1}: " + deck[y])
    deck.remove(deck[x])

print(f"\nDeck ({len(deck)} kaarten): {', '.join(deck)}")