from fruitmand import fruitmand

weight = 0

fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 2350,
    'color' : 'green',
    'round' : False
}) # Please confirm i have no idea whether watermelons are considered round for this program's definition of round :panic:

for x in fruitmand:
    weight += x['weight']

print("The fruit basket weighs {}g, or {:.2f}kg".format(weight, weight/1000))
