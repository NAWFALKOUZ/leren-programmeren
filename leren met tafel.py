import random 

naam = input("wat is jou naam?")
def main():    
    
    while True:
        try:
            tafel = int(input(f"Hallo {naam}, Welke tafel wil je oefenen?"))
            break
        except ValueError: 
            print("Het moet een cijfer zijn.")

    hoeveel = int(input("Hoeveel vragen wil je?"))
    
    
    for x in range(hoeveel):
        cijfers = random.randint(1,10)
        De_tafel = tafel
        antwoord1 = cijfers * De_tafel
        print("Wat is " + str(cijfers) + " x " + str(De_tafel) + "?")
        antwoord2 = int(input())
        if antwoord2 == antwoord1:
            print("Correct!")
        else:
            print("Sorry, het is " + str(antwoord1))

    opnieuw = input("wil je opnieuw spelen (ja of nee)").lower()
    if opnieuw == "ja":
        main()
    else:
        print("Dank je wel voor het leren van de tafel van",tafel)
        quit()
main()