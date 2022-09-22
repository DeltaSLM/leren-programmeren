iPhone = float(input("Hoeveel kost de Iphone 13?"))
Samsung = float(input("Hoeveel kost de Samsung Galaxy S22?"))
zenFone = float(input("Hoeveel kost de Asus Zenfone 9?"))

# Kijk of de iPhone en Samsung beide 900 of over zijn, en sluit het programma af met het advies niet een telefoon te kopen.

if iPhone >= 900 and Samsung >= 900 and zenFone >= 900:
    if iPhone > Samsung:
        print(f"De Iphone is het duurst, de telefoon kost: {iPhone} Euro\nDe Samsung is het goedkoopst, de telefoon kost: {Samsung} Euro")
    else:
        print(f"De Samsung Galaxy S22 is het duurst, de telefoon kost {Samsung} Euro\nDe Iphone 13 is het goedkoopst, de telefoon kost {iPhone} Euro")
    print("Het advies is dus geen telefoon te kopen, ze zijn te duur.")
    exit()

zenMinSamsung = Samsung - zenFone
zenMinIphone = iPhone - zenFone

if zenMinSamsung >= 100 and zenMinIphone >= 100:
    if iPhone > Samsung:
        print(f"De iPhone 13 is het duurst, de telefoon kost: {iPhone} Euro\nDe ZenFone is het goedkoopst, de telefoon kost: {zenFone} euro\nDe Samsung Galaxy S22 zit er tussenin met: {Samsung} Euro")
    else:
        print(f"De Samsung Galaxy S22 is het duurst, de telefoon kost: {Samsung} Euro\nDe ZenFone is het goedkoopst, de telefoon kost: {zenFone} euro\nDe iPhone 13 zit er tussenin met: {iPhone} Euro")
    print(f"het advies is dus de Asus ZenFone 9 te kopen. Deze is namelijk {zenMinIphone} euro goedkoper dan de iPhone 13 en {zenMinSamsung} euro goedkoper dan de Samsung Galaxy S22")
    exit()

# Kijk of de iPhone duurder is dan de Samsung.
# Indien hij dat is, zal hij kijken of dat de iPhone 50 plus euro duurder is, in welk geval hij zal aanraden om de Samsung te kopen


if iPhone > Samsung:
    print(f"De iPhone 13 is het duurst, de telefoon kost: {iPhone} Euro\nDe Samsung Galaxy S22 is het goedkoopst, de telefoon kost: {Samsung} Euro")
    prijsverschil = iPhone - Samsung

    if prijsverschil > 50:
        print(f"Het advies is dus de Samsung Galaxy S22 te kopen. Deze is namelijk {prijsverschil} euro goedkoper dan de Iphone 13")
    else:
        print(f"Het advies is dus de Iphone 13 te kopen. Deze is namelijk {prijsverschil} euro duurder dan de Samsung Galaxy S22")

# Als de Samsung duurder is dan zal de Iphone als advies worden gegeven

elif iPhone < Samsung:
    print(f"De Samsung Galaxy S22 is het duurst, de telefoon kost {Samsung} euro\nDe iPhone is het goedkoopst, de telefoon kost: {iPhone} Euro")
    prijsverschil = Samsung - iPhone

    print(f"Het advies is dus de Iphone 13 te kopen. Deze is namelijk {prijsverschil} euro goedkoper dan de Samsung Galaxy S22")

# De iPhone wordt als advies gegeven omdat de prijzen hetzelfde zijn

else:
    print(f"De telefoons kosten allebei {iPhone} Euro")
    print(f"Het advies is dus de Iphone 13 te kopen. Deze is namelijk net zo duur als de Samsung Galaxy S22.")
