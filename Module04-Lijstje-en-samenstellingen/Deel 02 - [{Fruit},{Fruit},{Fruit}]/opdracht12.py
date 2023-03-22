from fruitmand import fruitmand

naam_fruit = ''
kleur_fruit = ''
gewicht_fruit = 0
letters = 0

for fruit in fruitmand:
    if letters < len(fruit['name']):
        naam_fruit = fruit['name']
        kleur_fruit = fruit['color']
        gewicht_fruit = fruit['weight']
        letters = len(fruit['name'])

kleuren = {
    "yellow" : "gele",
    "green" : "groene",
    "orange" : "oranje",
    "red" : "rode",
    "brown" : "bruin",
}

print(f'De "{naam_fruit}" ({letters} letters) heeft een {kleuren[kleur_fruit]} kleur en een gewicht van {gewicht_fruit / 1000} kg.')
