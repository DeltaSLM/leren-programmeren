from fruitmand import fruitmand

colors = []
fruitmand.remove(fruitmand[4])

for x in fruitmand:
    if x['color'] not in colors:
        colors.append(x['color'])

print(", ".join(colors))