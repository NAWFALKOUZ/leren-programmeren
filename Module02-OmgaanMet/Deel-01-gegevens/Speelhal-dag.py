# toegangsticket = 7.45
# prijs_minuut = 0.37 / 5


vraag_toegangsticket = float(input("Hoeveel kost een toegangs ticket"))
vraag_prijs_per_minuut = float(input("Hoeveel prijs per minuut"))


# print(f'toegangsticket kost {toegangsticket} euro')
# print(f'prijs per minuut kost {prijs_minuut} euro')

aantal_personen =  float(input("hoeveel personen?"))
aantal_minuten =  float(input("Hoeveel minuten wil je?"))

totaal_toegangsprijs = aantal_personen * vraag_toegangsticket,
totaal_vipprijs = aantal_minuten * vraag_prijs_per_minuut
prijs = totaal_toegangsprijs + totaal_vipprijs * aantal_personen 

print(f'Dit geweldige dagje-uit met {aantal_personen} mensen in de Speelhal met {aantal_minuten} minuten VR kost je maar {prijs}')



















