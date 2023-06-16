def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    if number2 == 0:
        raise ValueError("kan niet delen door 0")
    return number1 / number2

choice = " "
while not choice in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'):
    choice = input('Wat wilt u doen?\nA) Getallen optellen\nB) Getallen aftrekken\nC) Getallen vermenigvuldigen\nD) Getallen delen\nE) Getal ophogen\nF) Getal verlagen\nG) Getal verdubbelen\nH) Getal halveren\nKies: ').upper()

aantal = -1
while True:
    if aantal > -1 and choice in ('A', 'B', 'C', 'D'):
        number1 = aantal
        while True:
            try:
                number2 = float(input("Geef het tweede getal op: "))
                break
            except ValueError:
                print("Dit is geen geldig getal.")

    elif aantal > -1 and choice in ('E', 'F', 'G', 'H'):
        number1 = aantal

    elif choice in ('A', 'B', 'C', 'D'):
        while True:
            try:
                number1 = float(input("Geef een getal op: "))
                number2 = float(input("Geef nog een getal op: "))
                break
            except ValueError:
                print("Dit is geen geldig getal.")

    elif choice in ('E', 'F', 'G', 'H'):
        while True:
            try:
                number1 = float(input("Geef een getal op: "))
                break
            except ValueError:
                print("Dit is geen geldig getal.")

    else:
        exit()

    if choice == "A":
        aantal = addition(number1, number2)
    elif choice == "B":
        aantal = subtraction(number1, number2)
    elif choice == "C":
        aantal = multiplication(number1, number2)
    elif choice == "D":
        try:
            aantal = division(number1, number2)
        except ValueError:
            print("Kan niet delen door 0")
            continue
    elif choice == "E":
        number2 = 1
        aantal = addition(number1, number2)
    elif choice == "F":
        number2 = 1
        aantal = subtraction(number1, number2)
    elif choice == "G":
        number2 = 2
        aantal = multiplication(number1, number2)
    else:
        try:
            number2 = 2
            aantal = division(number1, number2)
        except ValueError:
            print("Kan niet delen door 0")
            continue

    print(aantal)
    print("--------------------")

    choice = input(f'Wil je iets met het uitkomst ({aantal})?\nA) Getallen optellen\nB) Getallen aftrekken\nC) Getallen vermenigvuldigen\nD) Getallen delen\nE) Getal ophogen\nF) Getal verlagen\nG) Getal verdubbelen\nH) Getal halveren\nI) niks\n Kies: ').upper()
    if choice == "I":
        print("einde berekening")
        exit()