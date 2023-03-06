boodschappenlist = {}

while True:
    # Vraag de gebruiker om een item en het aantal
    item_vraag = input("Voeg een item toe: ").lower()
    aantal = int(input("Hoeveel wil je van dit item? "))
    
    # Voeg het item en het aantal toe aan de boodschappenlijst
    if item_vraag in boodschappenlist:
        boodschappenlist[item_vraag] += aantal
    else:
        boodschappenlist.update({item_vraag : aantal})
    
    # Vraagt of ze meer items willen toevoegen
    tweede_item_vraag = input("Wil je meer items toevoegen (ja of nee)? ")
    if tweede_item_vraag != "ja":
        break
    
print("-[BOODSCHAPPENLIJST]-")
for key,value in boodschappenlist.items():
    print(f"{value}x {key}")
print("----------------------") 
