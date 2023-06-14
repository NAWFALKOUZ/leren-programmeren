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
while True:
    if aantal > -1 and choice in ('A', 'B', 'C', 'D'):
        number1 = aantal
        number2 = float(input("Geef het tweede getal op: "))

    elif aantal > -1 and choice in ('E', 'F', 'G', 'H'):
        number1 = aantal

    elif choice in ('A', 'B', 'C', 'D'):
        number1 = float(input("Geef een getal op: "))
        number2 = float(input("Geef nog een getal op: "))

    elif choice in ('E', 'F', 'G', 'H'):
        number1 = float(input("Geef een getal op: "))

    else:
        exit()

    if choice == "A":
        aantal = addition(number1, number2)
        print(aantal)
    elif choice == "B":
        aantal = subtraction(number1, number2)
        print(aantal)
    elif choice == "C":
        aantal = multiplication(number1, number2)
        print(aantal)
    elif choice == "D":
        aantal = division(number1, number2)
        print(aantal)
    elif choice == "E":
        number2 = 1
        aantal = addition(number1, number2)
        print(aantal)
    elif choice == "F":
        number2 = 1
        aantal = subtraction(number1, number2)
        print(aantal)
    elif choice == "G":
        number2 = 2
        aantal = multiplication(number1, number2)
        print(aantal)
    else:
        number2 = 2
        aantal = division(number1, number2)
        print(aantal)

    choice = input(f'Wil je iets met het uitkomst ({aantal})?\nA) Getallen optellen\nB) Getallen aftrekken\nC) Getallen vermenigvuldigen\nD) Getallen delen\nE) Getal ophogen\nF) Getal verlagen\nG) Getal verdubbelen\nH) Getal halveren\nKies: ').upper()
