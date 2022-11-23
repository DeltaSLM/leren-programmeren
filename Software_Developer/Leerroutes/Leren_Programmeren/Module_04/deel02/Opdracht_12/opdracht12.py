from fruitmand import fruitmand

translated = {"yellow": "gele", "green": "groene", "orange": "oranje", "red": "rode", "brown": "bruine", "pink": "roze", "purple": "paarse", "black": "zwarte"}
length = []
lengthnr = []

for x in fruitmand:
    lengthnr.append(len(x['name']))

index = lengthnr.index(max(lengthnr))
longestFruit = fruitmand[index]

print(f"De {longestFruit['name']} ({len(longestFruit['name'])} letters) heeft een {translated[longestFruit['color']]} kleur en een gewicht van {longestFruit['weight'] / 1000}KG")