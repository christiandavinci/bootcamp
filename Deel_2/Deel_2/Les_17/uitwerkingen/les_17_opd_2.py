import random

juiste_getal = 1

while True:
    getal = int(input('raad het nummer:'))
    
    if getal == juiste_getal:
        print("\033[92mje heb juiste getal geraden!\33]0m")
        break
    else:
     print("\033[91mje heb het nummer niet goed geraden! probeer opnieuw\33]0m")