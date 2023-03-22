from fruitmand import fruitmand

rond = 0
niet_rond = 0

x = False
while x == False:
    kleur = input('kies een kleur (in het engels): ')
    fruit_in_lijst = False 
    for fruit in fruitmand:
        if fruit['color'] == kleur:
            fruit_in_lijst = True  
            if fruit['round']:
                rond += 1
            else:
                niet_rond += 1

    if fruit_in_lijst: 
        if rond < niet_rond:
            print(f'Er zijn {niet_rond - rond} meer niet-ronde vruchten dan ronde vruchten in de kleur {kleur}')
        elif rond > niet_rond:
            print(f'Er zijn {rond - niet_rond} meer ronde vruchten dan niet-ronde vruchten in de kleur {kleur}')
        else:
            print(f"Er zijn {rond} ronde vruchten en {niet_rond} niet-ronde vruchten in de kleur {kleur}")
        quit()  
    else:
        print(f'{kleur} zit niet in de fruitmand')
