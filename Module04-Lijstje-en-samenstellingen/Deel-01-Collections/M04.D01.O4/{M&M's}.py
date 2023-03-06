import random

kleuren = ["rood", "blauw", "groen", "geel","bruin"]

# Vraagt  hoeveel M&M's er in het zakje moeten
hoeveel = int(input("Hoeveel M&M's moeten er in het zakje?"))

# Maak een lege dictionary om de kleuren en de aantallen in op te slaan
zak = {}
teller = 1 

# Kies voor elke M&M willekeurig een kleur en tel het aantal voorkomens van elke kleur
for x in range(hoeveel):
    keuzen = (random.choice(kleuren))
    if keuzen not in zak:
        zak.update({keuzen : teller})
    else:
        zak[keuzen] += 1

print(zak)
