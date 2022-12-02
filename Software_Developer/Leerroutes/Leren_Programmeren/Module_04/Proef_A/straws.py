import random

giveNames = True
booleaned = ""
original = []
straws = {}
gifted = []

while giveNames == True:
    while not (inputName := input("Please provide a name to add to the.")).isalpha():
        print("Letters only, no spaces.")

    if inputName not in original:
        original.append(inputName)
    else:
        pass

    if len(original) >= 3:
        while not (booleaned == "y" or booleaned == "n"):
            booleaned = input("Do you want to give up more names? Y/N")

        if booleaned == "n":
            giveNames = False
        else:
            booleaned = ""


for name in original:
    assignee = random.choice(original)

    while (assignee == name) or (name in straws) or (assignee in gifted):
        assignee = random.choice(original)

    straws[name] = assignee
    gifted.append(assignee)

print(original)

print(straws)

for (gifter, gifted) in straws.items():
    print(f"{gifter} has pulled {gifted}'s straw.")