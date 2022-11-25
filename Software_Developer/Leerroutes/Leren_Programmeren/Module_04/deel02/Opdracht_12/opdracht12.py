from fruitmandNew import fruitmand

translated = ""
def translation(fruitColor: str) -> str:
    translated = {"yellow": "gele", "green": "groene", "orange": "oranje", "red": "rode", "brown": "bruine", "pink": "roze", "purple": "paarse", "black": "zwarte"}
    if fruitColor in translated:
        return translated[fruitColor]
    else:
        return fruitColor

length = []
lengthnr = []

for x in fruitmand:
    lengthnr.append(len(x['name']))

index = lengthnr.index(max(lengthnr))
longestFruit = fruitmand[index]

print(f"De {longestFruit['name']} ({len(longestFruit['name'])} letters) heeft een {translation(longestFruit['color'])} kleur en een gewicht van {longestFruit['weight'] / 1000}KG")