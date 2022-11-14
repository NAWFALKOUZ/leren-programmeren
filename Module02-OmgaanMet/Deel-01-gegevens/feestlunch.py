# croissantje = 0.39
# stokbrood = 2.78
# kortingsbon = 0.5

vraag_croissantje = float(input("hoeveel kost een croissantje")) 
vraag_stokbrood = float(input("hoeveel kost een stokbrood"))
vraag_kortingsbon = float(input("Hoeveel is de kortingsbon"))


# print(f' 1 croissantje kost {croissantje} euro cent ')
# print(f' 1 stokbrood kost {stokbrood} euro ')
# print(f' 1 kortingsbon is {kortingsbon} euro cent ')

aantal_croissantjes = float(input('hoeveel croissantje wil je?'))
aantal_stokbrood = float(input("hoeveel stokbroden wil je?"))
aantal_kortingbon = float(input("hoeveel kortingsbonnen heb je?"))


totaal_prijs_croissant = aantal_croissantjes * vraag_croissantje 
totaal_prijs_stokbrood = aantal_stokbrood * vraag_stokbrood
totaal_prijs_kortingbon = aantal_kortingbon * vraag_kortingsbon
totaal_van_alles = totaal_prijs_croissant  + totaal_prijs_stokbrood - totaal_prijs_kortingbon

print(f'De feestlunch kost je bij de bakker {totaal_van_alles} voor de {aantal_croissantjes} croissantjes en de {aantal_stokbrood} stokbroden als de {aantal_kortingbon} kortingsbonnen nog geldig zijn!')