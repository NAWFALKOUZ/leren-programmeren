game = 24.95
korting = 0.4
def bereking():
    aantal = int(input("hoeveel wil je inkopen: "))
    totaal_inkoop = game + aantal
    inkoopprijs = game * (1 - korting)
    verzendkosten = 1 + (aantal -1) * 0.25
    totaal_ = aantal * inkoopprijs
    alles_intotaal = verzendkosten + totaal_
    return alles_intotaal
print(bereking())




