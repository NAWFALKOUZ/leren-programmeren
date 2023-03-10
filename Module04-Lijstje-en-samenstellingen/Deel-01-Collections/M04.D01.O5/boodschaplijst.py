boodschappenlist = {}

while True:
    try:
        item_vraag = input("Voeg een item toe: ").capitalize()
        aantal = int(input("Hoeveel wil je van dit item? "))
    except ValueError:
        print("Dat is geen geldig nummer, probeer het opnieuw")
        continue
    
    if item_vraag in boodschappenlist:
        boodschappenlist[item_vraag] += aantal
    else:
        boodschappenlist.update({item_vraag : aantal})
    
    tweede_item_vraag = input("Wil je meer items toevoegen (ja of nee)? ")
    if tweede_item_vraag != "ja":
        break
    
print("-[BOODSCHAPPENLIJST]-")
for key,value in boodschappenlist.items():
    print(f"{value}x {key}")
print("----------------------") 
