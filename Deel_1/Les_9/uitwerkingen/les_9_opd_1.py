
a=5
b=3
c=2
if (a==6 and b==4 or c==2):
   print("De conditie is waar")
else: 
   print("De conditie is niet waar")	

# En: 
a=5
b=3
c=2
if (a==6 and (b==4 or c==2)):
   print("De conditie is waar")
else:
   print("De conditie is niet waar")

# (geef met commentaar aan in de code wat het verschil is)
# Het verschil is dat bij het tweede blok code a==6 moet zijn voor dat deze naar de volgende conditie gaat.