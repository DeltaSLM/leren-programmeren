from fruitmand import fruitmand

translated = {"yellow": "gele", "green": "groene", "orange": "oranje", "red": "rode", "brown": "bruine"}
length = []

for x in fruitmand:
    length.append(x['name'])

index = length.index(max(length))
longestFruit = fruitmand[index]

print(f"De {longestFruit['name']} ({len(longestFruit['name'])} letters) heeft een {translated[longestFruit['color']]} kleur en een gewicht van {longestFruit['weight'] / 1000}KG")
