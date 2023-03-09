import random


kleuren = ('harten', 'klaveren', 'schoppen', 'ruiten')
kaarten = ('boer','vrouw','heer','aas')
jokers = ('Joker 1','joker 2')


lijst = []


for x in kleuren:
    for y in kaarten:
        lijst.append(f"{x} {y}")

    for z in range(2,11):
        lijst.append(f"{x} {z}")

for a in jokers:
    lijst.append(a)


random.shuffle(lijst)


for b in range(1,8):
    kaart = random.choice(lijst)
    print(f'kaart {b}: {kaart}')
    lijst.remove(kaart)


print(f'de rest van de kaarten is {len(lijst)}:{lijst}')
