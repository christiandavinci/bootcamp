import random

def is_geldig_gok(getal):
    return 1 <= getal <= 5  

aantal_rondjes = 0
aantal_fouten = 0

while True:
    juiste_getal = random.randint(1, 5)
    pogingen = 0

    while True:
        getal = int(input('Raad het nummer tussen 1 - 5: '))
        
        if not is_geldig_gok(getal):
            print("Ongeldige gok. Voer een nummer tussen 1 en 5 in.")
            continue

        pogingen += 1

        if getal == juiste_getal:
            print(f"\033[92mJe hebt het juiste getal {juiste_getal} geraden in {pogingen} pogingen!\033[0m")
            break
        else:
            print("\033[91mJe hebt het nummer niet goed geraden. Probeer opnieuw!\033[0m")
            aantal_fouten += 1

    aantal_rondjes += 1
    antwoord = input("Wil je nog een ronde spelen? (ja/nee): ")

    while antwoord.lower() not in ['ja', 'nee']:
        print("Ongeldige invoer. Voer 'ja' of 'nee' in.")
        antwoord = input("Wil je nog een ronde spelen? (ja/nee): ")

    if antwoord.lower() != 'ja':
        break

print(f"Je hebt in totaal {aantal_rondjes} rondes gespeeld.")
print(f"Je hebt {aantal_fouten} keer fout geraden.")
