from fruitmand import fruitmand

colors = []
roundfruit = {"round": 0, "notround": 0}
for x in fruitmand:
    if x['color'] not in colors:
        colors.append(x['color'])

while not (answer := input(f"Tell us a color from the following: {', '.join(colors)}")) in colors:
    print("De kleur {} zit niet in de fruitmand".format(answer))

for x in fruitmand:
    if x['color'] == answer:

        if x['round']:
            roundfruit['round'] += 1
        else:
            roundfruit['notround'] += 1

#print(roundfruit) # uncomment for debug
moreRound = roundfruit['round'] - roundfruit['notround']
lessRound = roundfruit['notround'] - roundfruit['round']

if roundfruit['round'] > roundfruit['notround']:
    print(f"Er {'is' if moreRound == 1 else 'zijn'} {moreRound} meer ronde {'vrucht' if moreRound == 1 else 'vruchten'} dan niet ronde vruchten in de kleur {answer}")
elif roundfruit['round'] < roundfruit['notround']:
    print(f"Er {'is' if lessRound == 1 else 'zijn'} {lessRound} minder ronde {'vrucht' if lessRound == 1 else 'vruchten'} dan niet ronde vruchten in de kleur {answer}")
elif roundfruit['round'] == roundfruit['notround']:
    print(f"Er {'is' if roundfruit['round'] == 1 else 'zijn'} {roundfruit['round']} ronde {'vrucht' if roundfruit['round'] == 1 else 'vruchten'} en {roundfruit['notround']} niet ronde {'vrucht' if roundfruit['notround'] == 1 else 'vruchten'} in de kleur {answer}")
else:
    print("Er is iets fout gegaan, probeer het opnieuw.\n\nDebug:\n{}".format(roundfruit))
