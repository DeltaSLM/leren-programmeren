iPhone = float(input("Hoeveel kost de Iphone 13?"))
Samsung = float(input("Hoeveel kost de Samsung Galaxy S22?"))

if iPhone > Samsung:
    print(f"De iPhone 13 is het duurst, de telefoon kost: {iPhone} Euro\nDe Samsung Galaxy S22 is het goedkoopst, de telefoon kost: {Samsung} Euro")
    prijsverschil = iPhone - Samsung

    if prijsverschil > 50:
        print(f"Het advies is dus de Samsung Galaxy S22 te kopen. Deze is namelijk {prijsverschil} euro goedkoper dan de Iphone 13")
    else:
        print(f"Het advies is dus de Iphone 13 te kopen. Deze is namelijk {prijsverschil} euro duurder dan de Samsung Galaxy S22")

elif iPhone < Samsung:
    print(f"De Samsung Galaxy S22 is het duurst, de telefoon kost {Samsung} euro\nDe iPhone is het goedkoopst, de telefoon kost: {iPhone} Euro")
    prijsverschil = Samsung - iPhone

    print(f"Het advies is dus de Iphone 13 te kopen. Deze is namelijk {prijsverschil} euro goedkoper dan de Samsung Galaxy S22")
else:
    print(f"De telefoons kosten allebij {iPhone} Euro")
    print(f"Het advies is dus de Iphone 13 te kopen. Deze is namelijk net zo duur als de Samsung Galaxy S22.")
