import random
kleuren = ["rood", "blauw", "groen", "geel","bruin"]

hoeveel = int(input("Hoeveel M&M's moeten er in het zakje?"))

zak = {}
teller = 1 

for x in range(hoeveel):
    keuzen = (random.choice(kleuren))
    if keuzen not in zak:
        zak.update({keuzen : teller})
    else:
        zak[keuzen] += 1

print(zak)