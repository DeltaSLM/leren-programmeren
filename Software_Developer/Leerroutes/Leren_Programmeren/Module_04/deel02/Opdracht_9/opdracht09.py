from fruitmand import fruitmand

colors = []

for idx, dictionary in enumerate(fruitmand):
    if dictionary['name'] == "druif":
        fruitmand.pop(idx)

for x in fruitmand:
    if x['color'] not in colors:
        colors.append(x['color'])

print(", ".join(colors))