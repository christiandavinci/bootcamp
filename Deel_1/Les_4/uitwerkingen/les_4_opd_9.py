aantal_studenten = 21 # ongeveer onze klas
collegegeld_per_student = 13,734 # onze klas college geld bij elkaar getld
btw_tarief_fruit = 0,09 # huidge btw kan 0 worden in 2024 wordt nog gekeken door de regering 
totaal_collegegeld = aantal_studenten * collegegeld_per_student
print("totaal collegegeld betaald"), totaal_collegegeld, "euro"


prijs_appels = 3.40
prijs_druiven = 2.45
prijs_bananen = 1.95

totaal_bedrag_fruit = prijs_appels + prijs_druiven + prijs_bananen
Btw_fruit = totaal_bedrag_fruit * btw_tarief_fruit
print("totaalbedrag fruit zonder btw:", totaal_bedrag_fruit, "euro")
print("btw op fruit:", Btw_fruit, "euro")