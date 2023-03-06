import random
kleuren = ["oranje","blauw","groen","bruin"]

# Maak een lege lijst om de gekozen M&M's op te slaan
zakje = [] 

# Vraagt hoeveel M&M's er in het zakje moeten
hoeveel = int(input("Hoeveel M&M's moeten er in het zakje?"))

# maakt willekeurige kleuren voor elk van de M&M's en voeg deze toe aan de lijst
for x in range(hoeveel):
    keuzen = (random.choice(kleuren))
    zakje.append(keuzen)
    
print(f"In het M&M zakje zitten er {hoeveel} en de kleuren {zakje}") 
