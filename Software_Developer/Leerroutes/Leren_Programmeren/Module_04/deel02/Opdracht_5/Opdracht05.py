from fruitmand import fruitmand

fruitmand = reversed(fruitmand)
#for x in fruitmand:
    #print(x['name'])

# Andere mogelijkheid
for x in range(len(fruitmand)-1,-1,-1):
    # range: start, eind, hoeveelheid
    print(fruitmand[x]['name'])