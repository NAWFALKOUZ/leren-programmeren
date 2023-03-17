Dagen = ("Maandag","Dinsdag","Woensdag","Donderdag","Vrijdag","Zaterdag","Zondag")
#naast elkaar geprint worden

print(f"Alle dagen van de week zijn {Dagen}")

print(f'de weekenddagen zijn: ')
for y in range(5, 7): #range(start, stop, step) 
    print(Dagen[y], end=" ")
print("\n")

print(f'Alle dagen van de week in omgekeerde volgorde zijn:')
for z in range(6, -1, -1):
    print(Dagen[z], end =" ")
print("\n")

print(f'De werkdagen in omgekeerde volgorde zijn:')
for a in range(4,  -1, -1):
    print(Dagen[a], end=" ")
print("\n")

print('De weekenddagen in omgekeerde volgorde zijn:')
for b in range(6,  4, -1):
    print(Dagen[b], end=" ")
