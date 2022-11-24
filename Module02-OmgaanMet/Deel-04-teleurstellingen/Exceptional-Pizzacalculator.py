# nawfal kouzmane Pizza calculator

small_pizza_prijs = 9
medium_pizza_prijs = 11
large_pizza_prijs = 13

print(f'small pizza kost {small_pizza_prijs} euro')
print(f'medium pizza kost {medium_pizza_prijs}euro')
print(f'large pizza kost {large_pizza_prijs} euro')
 
while True:
    try:
        antwoord_pizzas_small = int(input("Hoeveel small pizzas wil u?"))
        break
    except ValueError: 
        print("Dat is geen geldig nummer, probeer het opnieuw")
while True:
    try:
        antwoord_pizzas_medium = int(input("Hoeveel medium pizzas wil u"))
        break
    except ValueError:
        print("Dat is geen geldig nummer, probeer het opnieuw")
while True:
    try:
        antwoord_pizzas_large = int(input("Hoeveel large pizza wil je"))
        break
    except ValueError:
        print("Dat is geen geldig nummer, probeer het opnieuw")

prijs_small_pizza = antwoord_pizzas_small * small_pizza_prijs 
prijs_medium_pizza = antwoord_pizzas_medium * medium_pizza_prijs 
prijs_large_pizza = antwoord_pizzas_large * large_pizza_prijs 
totaal_prijs = prijs_small_pizza + prijs_medium_pizza + prijs_large_pizza


print("--------------------------------------------------")
print(f' {antwoord_pizzas_small} small pizza: {prijs_small_pizza} euro')
print(f' {hoeveel_pizza_medium} medium pizza: {prijs_medium_pizza} euro')
print(f' {hoeveel_pizza_large} large pizza: {prijs_large_pizza} euro')
print(f'{ totaal_prijs } euro, dit is je totale prijs ' ) 
print("--------------------------------------------------")