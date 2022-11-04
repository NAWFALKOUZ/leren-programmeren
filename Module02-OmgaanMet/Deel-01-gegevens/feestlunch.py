croissantje = 0.39
stokbrood = 2.78
kortingsbon = 0.50

aantal_croissantjes = int(input('hoeveel croissantje wil je?'))
aantal_stokbrood = int(input("hoeveel stokbroden wil je?"))
aantal_kortingbon = int(input("hoeveel kortingsbonnen heb je?"))




totaal_prijs_croissant = aantal_croissantjes * croissantje 
totaal_prijs_stokbrood = aantal_stokbrood * stokbrood
totaal_prijs_kortingbon = aantal_kortingbon * kortingsbon
totaal_van_alles = totaal_prijs_croissant  + totaal_prijs_stokbrood - totaal_prijs_kortingbon


print(f'De feestlunch kost je bij de bakker {totaal_van_alles}voor de {aantal_croissantjes} croissantjes en de {aantal_stokbrood} stokbroden als de {aantal_kortingbon} kortingsbonnen nog geldig zijn!')
