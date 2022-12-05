import random 

naam = input("wat is jouw naam?")
def main():

    while True:
        try:
            tafel = int(input(f"Hallo {naam}, Welke tafel wil je oefenen?"))
            break
        except ValueError: 
            print("Het moet een cijfer zijn.")


    for x in range(1,11):
        antwoord = int(input(f"{x} x {tafel} ="))
        keer = x * tafel
        if antwoord == keer:
            print("goed")
        else:
            print(f"Fout, het goede antwoord is {keer}")

    for x in range(1,11):
        
        while True:
            try:
                antwoord = int(input(f"{x} x {tafel} ="))
                break
            except ValueError:
                print("het moet een cijfer zijn")
            keer = x * tafel
        


    oefenen = input("Zullen we nu de sommen door elkaar oefenen? ja of nee").lower()
    if oefenen != "nee":
        print("we gaan nu beginnen")
    else:
        print("Jammer dat je weg gaat, tot de volgende keer")
        quit()

    hoeveel = int(input("Hoeveel vragen wil je?"))
    for x in range(hoeveel):
        cijfers = random.randint(1, 11)
        antwoord1 = cijfers * tafel
        print(f" wat is {cijfers} x {tafel} = ")
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
#str = text int = gehele getal float is een getal met een coma. een boolean of bool is true or false statements 

