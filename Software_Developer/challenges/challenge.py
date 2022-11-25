# Opg. 1
for x in range(1,13):
    print("Tafel van {}:".format(x))
    for y in range(1,11):
        print(f"{y} * {x} = {y*x}")

# Opg. 2
nummers = [5, 12, 19, 27, 3]

# Opg. 3
nummers.append(25)

# Opg. 4
print(len(nummers))

# Opg. 5
print(nummers)
nummers.remove(12)
print(nummers)

# Opg. 6
print(nummers)
nummers.remove(5)
print(nummers)

# Opg. 7
nummers = [36] + nummers
print(nummers)

# Opg. 8
addition = 0
for x in nummers:
    addition += x
print(addition)

# Opg. 9
nummers = []
print(nummers)

# Opg. 10
for x in range(1,4):
    nummers.append(x)

# Opg. 11
for x in range(4,51):
    nummers.append(x)
print(nummers)

# Opg. 12
indexed = nummers.index(25)

# Opg. 13
print(nummers)
nummers[0], nummers[49] = nummers[49], nummers[0]
print(nummers)

# Opg. 14
stuff = [1, "aap", 2, "apen", 3, "watermeloen", 15, 27, 15, "lekker bezig", "6"]

hoeveelheid = 0
for x in stuff:
    if str(type(x)) == "<class 'int'>":
        hoeveelheid += 1
print(hoeveelheid, "getallen")