results = {}
inputloop = 0

while inputloop != 3:
    while not (countries := input("Input a country here: ")).isalpha():
        print("A country name in letters please, no spaces")

    if countries in results.keys():
        print("This country is already in the list, try again.")

    else:
        while not (score := input(f"What is the score of {countries}?")).isdigit():
            print("The score please, this is usually a single number.")

        results[countries] = score
        inputloop += 1


print(results)

print(max(results.values()))

dictKeys = list(results.keys())

print(f"""
Wedstrijd {dictKeys[0].upper()} - {dictKeys[1].upper()} eindigde in {results[dictKeys[0]]} - {results[dictKeys[1]]}
{dictKeys[0].upper()}: punten {results[dictKeys[0]]}; doelsaldo: {int(results[dictKeys[0]]) - int(results[dictKeys[1]])}
{dictKeys[1].upper()}: punten {results[dictKeys[1]]}; doelsaldo: {int(results[dictKeys[1]]) - int(results[dictKeys[0]])}
{dictKeys[2].upper()}: punten {results[dictKeys[2]]}; doelsaldo: {int(results[dictKeys[2]]) - int(results[dictKeys[2]])}
""")