from fruitmand import fruitmand

def weight(e):
  return e['weight']

fruitmand.sort(key=weight, reverse=True)
for x in fruitmand:
    print("Het gewicht van een {} is {:.2f}kg".format(x['name'], x['weight']/1000))