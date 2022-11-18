item = ""
quantity = ""
stop = False
dict = {}

while stop != True:
    stopArg = ""

    item= input("What would you like to add to your grocery list? Please only provide the item.").lower()

    while not (quantity := input("How much of {} would you like?".format(item))).isdigit():
        print("Please provide a number for the quantity you'd like of {}".format(item))

    if item in dict:
        dict.update({item: int(quantity)+int(dict[item])})
    else:
        dict[item] = quantity.lower()

    while not (stopArg == "y" or stopArg == "n"):
        stopArg = input("Would you like to continue? Y/N").lower()

    if stopArg == "n":
        stop = True

print("-[ BOODSCHAPPENLIJST ]-\n")
for x in dict.keys():
    print(f"    {str(dict[x])}x {x.capitalize()}")