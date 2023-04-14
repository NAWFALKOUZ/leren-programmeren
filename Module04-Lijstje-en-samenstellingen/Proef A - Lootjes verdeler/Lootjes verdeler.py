# Vraagt namen aan deelnemers
# Zorg dat alle namen uniek zijn en minimaal 3 namen zijn opgegeven
#  als er 3 namen zijn vraagt hij steeds of je nog meer namen wilt invullen 
# trek random lootjes zonder dat iemand zichzelf heeft
# Print de lijst van namen en bijbehorende lootjes van de andere persoon

#je kan ook checken of de naam die het zelfde is. 

import random

namen = []

while True:
    vraag = input("Voer een naam in: ")
    if vraag in namen:
        print("je naam zit er al in")
    else: 
        namen.append(vraag)
    if len(namen) >= 3:
        verder = input("Wil je meer namen toevoegen ja/nee: ").lower()
        if verder == "nee":
            random.shuffle(namen)
            for x in range(len(namen)):
                print(f"{namen[x]} heeft het lootje van {namen[x-1]}")
            break