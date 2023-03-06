import random

# Definieer de verschillende kaartkleuren, soorten en jokers als tuple variabelen
kleuren = ('harten', 'klaveren', 'schoppen', 'ruiten')
kaarten = ('boer','vrouw','heer','aas')
jokers = ('Joker 1','joker 2')

# Maak een lege lijst aan om de kaarten in op te slaan
lijst = []

# Genereer kaarten voor elk type kleur en soort, voeg ze toe aan de lijst
for x in kleuren:
    for y in kaarten:
        lijst.append(f"{x} {y}")
    # Voeg de nummerkaarten toe voor elke kleur
    for z in range(2,11):
        lijst.append(f"{x} {z}")
# Voeg de jokers toe aan de lijst
for a in jokers:
    lijst.append(a)

# Schud de kaarten in de lijst willekeurig door elkaar
random.shuffle(lijst)

# Trek 7 kaarten van de lijst en print deze uit
for b in range(1,8):
    kaart = random.choice(lijst)
    print(f'kaart {b}: {kaart}')
    lijst.remove(kaart)

# Print de resterende kaarten in de lijst na het trekken van 7 kaarten
print(f'de rest van de kaarten is {len(lijst)}:{lijst}')
