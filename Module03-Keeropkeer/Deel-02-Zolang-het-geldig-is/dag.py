dagen = ["maandag", "dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag"]



Dag = input("Welke dag is het? ")


nummer = 0
while True:
    print(dagen[nummer])
    if dagen[nummer] == Dag:
        break
    nummer += 1
print(f'nog {nummer + 1} dag(en)')






