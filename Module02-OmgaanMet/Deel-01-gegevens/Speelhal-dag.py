toegangsticket = 7.45
prijs_minuut = 0.37 / 5


aantal_personen =  int(input("hoeveel personen?"))
aantal_minuten =  int(input("Hoeveel minuten wil je?"))

totaal_toegangsprijs = aantal_personen * toegangsticket
totaal_vipprijs = aantal_minuten * prijs_minuut 
prijs = totaal_toegangsprijs + totaal_vipprijs * aantal_personen 

print(f'Dit geweldige dagje-uit met {aantal_personen} mensen in de Speelhal met {aantal_minuten} minuten VR kost je maar {prijs}')



















