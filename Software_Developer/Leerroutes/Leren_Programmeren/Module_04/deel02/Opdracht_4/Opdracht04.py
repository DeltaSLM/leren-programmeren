import random

from fruitmand import fruitmand

while not (amount := input("How much fruit would you like?")).isdigit():
    print("NUMBER!!!!!")

amount = int(amount)

for x in range(amount):
    print(fruitmand[random.randint(0,len(fruitmand)-1)]['name'])