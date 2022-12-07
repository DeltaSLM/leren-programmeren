import random

moreNames = True
giveNames = ""

gelijk = True
names = []
lijst = []
check = 0
straws = {}

while moreNames:
    while not (inputName := input("Please provide a name to add to the.")).isalpha():
        print("Letters only, no spaces.")

    if inputName not in names:
        names.append(inputName)
        lijst.append(inputName)

    if len(names) >= 3:
        while not (giveNames == "y" or giveNames == "n"):
            giveNames = input("Do you want to give up more names? Y/N").lower()

        if giveNames == "n":
            moreNames = False
        else:
            giveNames = ""

while check != len(names):
    check = 0
    for x in range(0, len(names)):
        if names[x] == lijst[x]:
            random.shuffle(lijst)
            print("shuffled")
        else:
            check += 1

print(names)
print(lijst)

for x in range(0, len(names)):
  print(f"{names[x]} heeft {lijst[x]}")