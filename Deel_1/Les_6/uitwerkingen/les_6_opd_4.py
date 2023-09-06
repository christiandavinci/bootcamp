a = int(input("Voer de waarde voor a in: "))
b = int(input("Voer de waarde voor b in: "))
c = int(input("Voer de waarde voor c in: "))

if a > b and a > c:
    print(f"Variabele a is het grootst want {a} is groter dan b en c.")
elif b > a and b > c:
    print(f"Variabele b is het grootst want {b} is groter dan a en c.")
elif c > a and c > b:
    print(f"Variabele c is het grootst want {c} is groter dan a en b.")
else:
    print("Er zijn minstens twee variabelen met dezelfde hoogste waarde.")