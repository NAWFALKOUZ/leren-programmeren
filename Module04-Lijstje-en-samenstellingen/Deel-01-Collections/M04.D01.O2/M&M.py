import random
kleuren = ["oranje","blauw","groen","bruin"]

zakje = [] 


hoeveel = int(input("Hoeveel M&M's moeten er in het zakje?"))


for x in range(hoeveel):
    keuzen = (random.choice(kleuren))
    zakje.append(keuzen)
    
print(f"In het M&M zakje zitten er {hoeveel} en de kleuren {zakje}") 
