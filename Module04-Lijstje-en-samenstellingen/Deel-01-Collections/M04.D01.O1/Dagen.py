Dagen = ("Maandag","Dinsdag","Woensdag","Donderdag","Vrijdag","Zaterdag","Zondag")

print(f"Alle dagen van de week zijn {Dagen}")

for y in range(5, 7): #range(start, stop, step) 
    print(f'de weekenddagen zijn: {Dagen[y]}')

for z in range(6, -1, -1):
    print(z)
    print(f'Alle dagen van de week in omgekeerde volgorde zijn: {Dagen[z]}')

for a in range(4,  -1, -1):
    print(f'De werkdagen in omgekeerde volgorde zijn: {Dagen[a]}')

for b in range(6,  4, -1):
    print(f'De weekenddagen in omgekeerde volgorde zijn: {Dagen[b]}')
