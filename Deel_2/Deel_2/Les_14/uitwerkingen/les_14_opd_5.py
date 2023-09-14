mijn_lijst = ['jona', 'bart', 'doris', 'boris', 'joris']

naam = input('voer een naam in')


if naam in mijn_lijst:
    mijn_lijst.remove(naam)
    print(mijn_lijst)
else:
    mijn_lijst.append(naam)
    print(mijn_lijst)



# Opdracht 5:
# Schrijf een programma dat een lijst van 5 namen maakt en vervolgens de gebruiker vraagt om een naam in te voeren. 
# Gebruik de remove functie om de opgegeven naam uit de lijst te verwijderen
# als deze voorkomt en print vervolgens de bijgewerkte lijst.
# Als de opgegeven naam niet in de lijst voorkomt, gebruik dan de append functie
# om deze aan de lijst toe te voegen en print vervolgens de bijgewerkte lijst.