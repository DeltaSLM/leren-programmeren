import random

emenems = ('orange', 'blue', 'green', 'brown')
amount = ""

while not (amount := input("How many m&m's do you want in the bag?")).isdigit():
    print("Please provide numbers only.")

bag = []

for x in range(int(amount)):
    newemenem = random.choice(emenems)
    bag.append(newemenem)

print(f"You have {amount} m&m's in the bag: {bag}")
