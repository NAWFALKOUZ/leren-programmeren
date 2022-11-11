# nawfal kouzmane Pizza calculator

smallPizza_prijs = 9
mediumPizza_prijs = 11
largePizza_prijs = 13


hoeveel_pizzaSmall = int(input('hoeveel small pizzas wil je?'))
hoeveel_pizzaMedium = int(input('hoeveel medium pizzas wil je?'))
hoeveel_pizzaLarge =int (input('hoeveel large pizzas wil je?'))

prijs_smallPizza = hoeveel_pizzaSmall * smallPizza_prijs 
prijs_mediumPizza = hoeveel_pizzaMedium * mediumPizza_prijs 
prijs_largePizza = hoeveel_pizzaLarge * largePizza_prijs 
totaal_prijs = prijs_smallPizza + prijs_mediumPizza + prijs_largePizza


print("--------------------------------------------------")
print(f'small pizza: {prijs_smallPizza} euro')
print(f'Medium pizza: {prijs_mediumPizza} euro')
print(f'Large pizza: {prijs_largePizza} euro')
print(f'{ totaal_prijs } euro, dit is je totale prijs ' ) 
print("--------------------------------------------------")