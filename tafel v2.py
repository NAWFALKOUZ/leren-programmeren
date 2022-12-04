import random 



naam = input("wat is jouw naam?")
def main():    
    
    while True:
        try:
            tafel = int(input(f"Hallo {naam}, Welke tafel wil je oefenen?"))
            break
        except ValueError: 
            print("Het moet een cijfer zijn.")



    for x in range(1, 11):
        print(x, "x", tafel, "=", end=" ")
        keer = x * tafel
        antwoord = int(input())
        if antwoord == x * tafel:
            print("goed")
        else:
            print("Fout, het goede antwoord is " + str(keer))


    oefenen = input("Zullen we nu de sommen door elkaar oefenen? ja of nee").lower()
    if oefenen == "ja":
        print("we gaan nu beginnen")
    elif oefenen == "nee":
        print("Jammer dat je weg gaat, tot de volgende keer")
        quit()
    
    hoeveel = int(input("Hoeveel vragen wil je?"))
    for x in range(hoeveel):
        cijfers = random.randint(1,10)
        De_tafel = tafel
        antwoord1 = cijfers * De_tafel
        print("Wat is " + str(cijfers) + "x" + str(De_tafel))
        antwoord2 = int(input())
        if antwoord2 == antwoord1:
            print("Correct!")
        else:
            print("fout, het goede antwoord is " + str(antwoord1))

    opnieuw = input("wil je verder oefenen? (ja of nee)").lower()
    if opnieuw == "ja":
        main()
    else:
        print("Jammer dat je weg gaat, tot de volgende keer")
        quit()
main()