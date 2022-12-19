import random 

naam = input("wat is jouw naam?")
def main():    
    
    while True:
        try:
            tafel = int(input(f"Hallo {naam}, Welke tafel wil je oefenen?"))
            break
        except ValueError: 
            print("Het moet een cijfer zijn.")

    for x in range(6,16):
        antwoord = int(input(f"{x} x {tafel} ="))
        keer = x * tafel
        if antwoord == keer:
            print("goed")
        else:
            print(f"Fout, het goede antwoord is {keer}")


    oefenen = input("Zullen we nu de sommen door elkaar oefenen? ja of nee").lower()
    if oefenen == "ja":
        print("we gaan nu beginnen")
    elif oefenen == "nee":
        print("Jammer dat je weg gaat, tot de volgende keer")
        quit()
    



    hoeveel = int(input("Hoeveel vragen wil je?"))
    for x in range(hoeveel):
        cijfers = random.randint(6,16)
        De_tafel = tafel
        antwoord1 = cijfers * De_tafel
        print(f"Wat is {cijfers} x {tafel} ")
        antwoord2 = int(input())
        if antwoord2 == antwoord1:
            print("Correct!")
        else:
            print(f"fout, het goede antwoord is {antwoord1}")

    opnieuw = input("wil je verder oefenen? (ja of nee)").lower()
    if opnieuw == "ja":
        main()
    else:
        print("Jammer dat je weg gaat, tot de volgende keer")
        quit()
main()

# def = define main = function. def maakt een function die alleen werk als hij wordt geroepen
# variable is een doosje waar data wordt op geslagen
#str = text int = gehele getal float is een getal met een coma. een boolean of bool is true or false statements 5
#verandren naar 6 tot met 15 van plaats van 1 tot met 10
#als de antwoord fout is probeer opnieuw, met een loop terug naar het begin