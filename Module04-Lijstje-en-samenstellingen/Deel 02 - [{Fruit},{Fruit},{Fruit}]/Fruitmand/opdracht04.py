from fruitmand import fruitmand
import random

hoeveel = input("type een nummer")

for x in (hoeveel):
    keuzen = random.randint(0,(len(fruitmand)))
    print(fruitmand[keuzen]['name'])