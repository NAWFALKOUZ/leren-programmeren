def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    if number2 == 0:
        print("Kan niet delen door 0")
        return None
    return number1 / number2

choice = " "
aantal = None  

while choice not in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'):
    choice = input('Wat wilt u doen?\nA) Getallen optellen\nB) Getallen aftrekken\nC) Getallen vermenigvuldigen\nD) Getallen delen\nE) Getal ophogen\nF) Getal verlagen\nG) Getal verdubbelen\nH) Getal halveren\nKies: ').upper()
    
    
while True:
    if aantal is not None:
        number1 = aantal
    else:
        if choice in ('A', 'B', 'C', 'D'):
            while True:
                try:
                    number1 = float(input("Geef het eerste getal op: "))
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
        number2 = float(input("Geef het tweede getal op: "))
        aantal = addition(number1, number2)
    elif choice == "B":
        number2 = float(input("Geef het tweede getal op: "))
        aantal = subtraction(number1, number2)
    elif choice == "C":
        number2 = float(input("Geef het tweede getal op: "))
        aantal = multiplication(number1, number2)
    elif choice == "D":
        number2 = float(input("Geef het tweede getal op: "))
        result = division(number1, number2)
        if result is None:
            continue
        aantal = result
    elif choice == "E":
        aantal = addition(number1, 1)
    elif choice == "F":
        aantal = subtraction(number1, 1)
    elif choice == "G":
        aantal = multiplication(number1, 2)
    else:
        aantal = division(number1, 2)
        if aantal is None:
            continue

    print(aantal)
    print("--------------------")

    choice = input(f'Wil je iets met het uitkomst ({aantal})?\nA) Getallen optellen\nB) Getallen aftrekken\nC) Getallen vermenigvuldigen\nD) Getallen delen\nE) Getal ophogen\nF) Getal verlagen\nG) Getal verdubbelen\nH) Getal halveren\nI) niks\n Kies: ').upper()
    if choice == "I":
        print("einde berekening")
        exit()
