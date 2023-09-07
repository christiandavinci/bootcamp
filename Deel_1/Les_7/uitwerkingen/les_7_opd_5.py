beginsaldo = 10000  

rente_percentage = 2.8 / 100

jaren_5 = 5
jaren_15 = 15

eindbedrag_5 = beginsaldo * (1 + rente_percentage) ** jaren_5

eindbedrag_15 = beginsaldo * (1 + rente_percentage) ** jaren_15


print(f"Na {jaren_5} jaar heb je {eindbedrag_5:.2f} euro.")
print(f"Na {jaren_15} jaar heb je {eindbedrag_15:.2f} euro.")
