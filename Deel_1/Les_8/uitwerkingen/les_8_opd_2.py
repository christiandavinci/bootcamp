cijfer = int(input("wat is jou cijfer: "))
omschrijving = ''

if cijfer == 10:
    omschrijving ="Uitmuntend" 
    print(omschrijving)

elif cijfer == 9:
    omschrijving ="Zeer goed" 
    print(omschrijving)
elif cijfer == 8:
    omschrijving ="Goed" 
    print(omschrijving)
elif cijfer == 7:
    omschrijving ="Ruim voldoende" 
    print(omschrijving)
elif cijfer == 6:
    omschrijving ="Voldoende" 
    print(omschrijving)
elif cijfer == 5:
    omschrijving ="Bijna voldoende" 
    print(omschrijving)
elif cijfer == 4:
    omschrijving ="Onvoldoende" 
    print(omschrijving)
elif cijfer == 3:
    omschrijving ="Gering" 
    print(omschrijving)
elif cijfer == 2:
    omschrijving ="Slecht" 
    print(omschrijving)
elif cijfer == 1:
    omschrijving ="Zeer slecht" 
    print(omschrijving)
else:
    print("Dit kan ik niet omzetten!")


if cijfer >= 6:
    print (f'Gefeliciteerd, {omschrijving} je resultaat is een {cijfer}')
elif cijfer <=6: 
    print (f"Jammer, {omschrijving} je resultaat is een {cijfer}")
