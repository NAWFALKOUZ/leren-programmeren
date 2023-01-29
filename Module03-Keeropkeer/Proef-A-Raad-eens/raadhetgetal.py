import random

rondes = 0
score = 0

while rondes < 20:
    te_raden_getal = random.randint(1,1000)

    print(te_raden_getal)
    teller = 0

    while teller < 10:
        geraden_getal = int(input('Raad een getal tussen 1 en 1000: '))

        if geraden_getal == te_raden_getal:
            print('geraden')
            score += 1
            rondes += 1
            teller = 10
            break

        verschil = abs(geraden_getal - te_raden_getal)

        if te_raden_getal >= geraden_getal:
            print('hoger')
        elif te_raden_getal <= geraden_getal:
            print('lager')
        if verschil >= 20: 
            print('je bent warm')
        elif verschil <=50:    
            print('je bent heel warm')
        teller += 1 

    if rondes < 20:
        verder = input('wil nog een getal raden? (ja/nee)').lower()
        if verder == "nee":
            print(f'je hebt {score} goed geraden')
            quit()

print(f"je hebt 20 rondes gedaan, je hebt {score} goed geraden ")
