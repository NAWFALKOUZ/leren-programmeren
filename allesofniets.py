import random 

naam = input("wat is jou naam?")
def main():    
    
    while True:
        try:
            tafel = int(input(f"Hallo {naam}, Welke tafel wil je oefenen?"))
            break
        except ValueError: 
            print("Het moet een cijfer zijn.")
    
    print(f"dit is de tafel van {tafel}")
    for x in range(1,11):
        print(f"{x} x {tafel} =", x*tafel)

    





    while True:
        try:
            hoeveel = int(input("Hoeveel vragen wil je?"))
            break
        except ValueError:
            print("het moet cijfers zijn")

    hoeveel = int(input("Hoeveel vragen wil je?"))
    for x in range(hoeveel):
        cijfers = random.randint(1,10)
        De_tafel = tafel
        antwoord1 = cijfers * De_tafel
        print(f"Wat is {cijfers}  x {De_tafel} ?")
        antwoord2 = int(input())
        if antwoord2 == antwoord1:
            print("Correct!")
        else:
            print("Sorry, het is " + (antwoord1))

        opnieuw = input("wil je opnieuw oefenen (ja of nee)").lower()
        if opnieuw == "ja":
         main()
        else:
            print("Jammer dat je weg gaat, tot de volgende keer")
        quit()
main()