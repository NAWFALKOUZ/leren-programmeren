def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

choice = " "
while not choice in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'):
    choice = input('Wat wilt u doen?\nA) Getallen optellen\nB) Getallen aftrekken\nC) Getallen vermenigvuldigen\nD) Getallen delen\nE) Getal ophogen\nF) Getal verlagen\nG) Getal verdubbelen\nH) Getal halveren\nKies: ').upper()
    if choice == "NIKS":
        exit()

aantal = -1
firstRound = True
while True:
    if not firstRound:
        n1 = aantal
        if choice in ('A', 'B', 'C', 'D'):
            while True:
                try:
                    n2 = float(input("Geef het tweede getal op: "))
                    break
                except ValueError:
                    print("Dit is geen geldig getal. Probeer opnieuw.")
        else:
            n2 = 1 if choice in ('E', 'F') else 2
    else:
        firstRound = False
        while True:
            try:
                n1 = float(input("Geef een getal op: "))
                n2 = float(input("Geef nog een getal op: ")) if choice in ('A', 'B', 'C', 'D') else 1 if choice in ('E', 'F') else 2
                break
            except ValueError:
                print("Dit is geen geldig getal. Probeer opnieuw.")

    if choice == "A":
        aantal = addition(n1, n2)
    elif choice == "B":
        aantal = subtraction(n1, n2)
    elif choice == "C":
        aantal = multiplication(n1, n2)
    elif choice == "D":
        if n2 == 0:
            print("Kan niet delen door 0")
            continue
        aantal = division(n1, n2)
    elif choice == "E":
        aantal = addition(n1, n2)
    elif choice == "F":
        aantal = subtraction(n1, n2)
    elif choice == "G":
        aantal = multiplication(n1, n2)
    else:
        if n2 == 0:
            print("Kan niet delen door 0")
            continue
        aantal = division(n1, n2)

    print(aantal)

    choice = input(f'Wil je iets met het uitkomst ({aantal}) doen?\nA) Getallen optellen\nB) Getallen aftrekken\nC) Getallen vermenigvuldigen\nD) Getallen delen\nE) Getal ophogen\nF) Getal verlagen\nG) Getal verdubbelen\nH) Getal halveren\nKies: ').upper()

