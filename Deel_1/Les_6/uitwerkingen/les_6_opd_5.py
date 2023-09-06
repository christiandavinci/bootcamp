a = int(input("Voer de waarde voor a in: "))
b = int(input("Voer de waarde voor b in: "))
c = int(input("Voer de waarde voor c in: "))

if a > b:
    hoogste_ab = a
else:
    hoogste_ab = b

if hoogste_ab > c:
    print(f"Variabele a en b hebben de hoogste waarde ({hoogste_ab}), want deze is groter dan c ({c}).")
elif hoogste_ab < c:
    print(f"Variabele c heeft de hoogste waarde ({c}), want deze is groter dan a en b ({hoogste_ab}).")
else:
    print("Variabele a, b en c hebben allemaal dezelfde waarde.")