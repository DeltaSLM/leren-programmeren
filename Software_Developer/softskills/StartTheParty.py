gastheer = input("What's your name?").lower()
gasten = 13
drank = True
chips = True

if drank and gastheer != 'rudi' and (gastheer or gasten >= 5 and gasten+1 < 13):
    print('Start the party')
else:
    print('No party.')