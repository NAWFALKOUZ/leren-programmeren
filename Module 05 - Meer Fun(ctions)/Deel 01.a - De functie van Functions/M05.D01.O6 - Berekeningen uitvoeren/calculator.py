choice = input('wat wilt u doen?\nA) getallen optellen\nB) getallen aftrekken\nC) getallen vermenigvuldigen\nD) getallen delen\nE) getal ophogen\nF) getal verlagen\nG) getal verdubbelen\nH) getal halveren\nKies: ').upper()



def addition(nummer1,nummer2):
    return nummer1 + nummer2

def subtraction(nummer1,nummer2):
    return nummer1 - nummer2


def multiplication(nummer1,nummer2):
    return nummer1 * nummer2

def division(nummer1,nummer2):
    return nummer1 / nummer2


  if choice == 'A':
        result = addition(nummer1, nummer2)
        operation = "optellen"
    elif choice == 'B':
        result = subtraction(nummer1, nummer2)
        operation = "aftrekken"
    elif choice == 'C':
        result = multiplication(nummer1, nummer2)
    elif choice == 'D':
        result = division(nummer1, nummer2)
        operation = "delen"
    elif choice == 'E':s
        result = addition(nummer1, nummer2)
        operation = "ophogen"
    elif choice == 'F':
        result = subtraction(nummer1, nummer2)
        operation = "verlagen"
    elif choice == 'G':
        result = multiplication(nummer1, nummer2)
        operation = "verdubbelen"
    elif choice == 'H':
        result = division(nummer1, nummer2)
        operation = "halveren"