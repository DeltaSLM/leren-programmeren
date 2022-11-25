from fruitmand import fruitmand

colors = []

for fruit in fruitmand:
    if fruit['name'] == 'druif':
        fruitmand.remove(fruit)

for x in fruitmand:
    if x['color'] not in colors:
        colors.append(x['color'])

print(", ".join(colors))