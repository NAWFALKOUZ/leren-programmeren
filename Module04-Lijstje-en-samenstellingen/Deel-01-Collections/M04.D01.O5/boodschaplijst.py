boodschappenlist = {}

while True:
    item_vraag = input("Voeg een item toe: ").lower()
    aantal = int(input("Hoeveel wil je van dit item? "))
    
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
