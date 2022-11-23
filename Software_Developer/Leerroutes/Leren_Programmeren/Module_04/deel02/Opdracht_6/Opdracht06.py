from fruitmand import fruitmand

for idx, dictionary in enumerate(fruitmand):
    if dictionary['name'] == "appel":
        print("The apple weighs " + str(dictionary['weight']) + "g")