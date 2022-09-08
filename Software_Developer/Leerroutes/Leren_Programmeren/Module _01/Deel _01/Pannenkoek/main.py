import math

print("hoeveel pannenkoeken wilt u maken?")

bloem = 500 / 20 # gram
melk = 800 / 20 # ml
ei = 3 / 20 # hoeveelheid
zout = 1 / 20# teelepels
boter = 30 / 20 # gram

try:
    x = int(input())

    bloem = x * bloem
    melk = x * melk
    ei = x * ei
    zout = x * zout
    boter = x * boter
    print(
        f'Voor {x} pannenkoeken heb je nodig:\n{math.ceil(bloem):.07,7f} gram meel/bloem\n{math.ceil(melk):.0f} ml melk\n{math.ceil(ei):.0f} eieren\n{math.ceil(zout):.0f} theelepels zout\n{math.ceil(boter):.0f} gram boter')
except:
    if ValueError:
        print('Please use integers. OBVIOUSLY you cant bloody use text for pancake amounts')