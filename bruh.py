grootste = 0
kleinste = 1000
aantal_deelbaar_drie = 0


for x in range(10):
    getal = int(input("type je getallen"))
    if getal > grootste:
        grootste = getal

    if getal < kleinste:
        kleinste = getal

if getal % 3 == 0:
    aantal_deelbaar_drie = aantal_deelbaar_drie + 1


print(F"deel {aantal_deelbaar_drie}")
print(f"het grooste getal is:{grootste} je kleinste getal is:{kleinste}")