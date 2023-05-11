name_age_list = []

def name_age():
    name_age_dict = {}
    naam = input("Wat is je naam? ")
    leeftijd = int(input("Hoe oud ben je? "))
    name_age_dict['name'] = naam
    name_age_dict['age'] = leeftijd
    return name_age_dict

while True:
    name_age_list.append(name_age())
    if input("wil nog een naam toevoegen (ja/nee): ") == "nee":
        break

for x in name_age_list:
    print(f"{x['name']} is {x['age']} jaar")
