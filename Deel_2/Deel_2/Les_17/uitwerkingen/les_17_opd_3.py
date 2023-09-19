import random

aantal_rondjes = 3

for _ in range(aantal_rondjes):
    juiste_getal = random.randint(1, 5)
    pogingen = 0

    while True:
        getal = int(input('Raad het nummer tussen 1 - 5: '))
        pogingen += 1

        if getal == juiste_getal:
            print(f"\033[92mJe hebt het juiste getal {juiste_getal} geraden in {pogingen} pogingen!\033[0m")
            break
        elif getal >= 1 and getal <= 5:
            print("\033[91mJe hebt het nummer niet goed geraden. Probeer opnieuw!\033[0m")
        else:
            print("Ongeldige invoer. Voer een nummer tussen 1 en 5 in.")
