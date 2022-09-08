#######################################################
# Dit is commentaar, veel te basic voor mij
#######################################################
def uwu():
    aantal = 6
    product = 'Patatje oorlog'
    stuksprijs = 1.90
    gram = '200g'

    regelprijs = aantal * stuksprijs

    print(f'{gram} {product} {aantal}x ${regelprijs:.2f}')

uwu()

### Cast types
int()
str()
float()

###############
# Input() Voorbeeld
###############
print("hoeveel pannenkoeken wilt u maken?")

bloem = 500 / 20 # gram
melk = 800 / 20 # ml
ei = 3 / 20 # hoeveelheid
zout = 1 / 20# teelepels
boter = 30 / 20 # gram

x = input()

print(type(x))

if str.isnumeric(x):
    bloem = int(x) * float(bloem)
    melk = int(x) * float(melk)
    ei = int(x) * float(ei)
    zout = int(x) * float(zout)
    boter = int(x) * float(boter)
    print(f'Voor {x} pannenkoeken heb je nodig:\n{bloem:.2f} gram meel/bloem\n{melk:.2f} ml melk\n{ei:.2f} eieren\n{zout:.2f} theelepels zout\n{boter:.2f} gram boter')
else:
    print('Please provide a positive integer.')
