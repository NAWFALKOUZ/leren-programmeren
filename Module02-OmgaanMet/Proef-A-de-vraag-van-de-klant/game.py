print('Jij bent een DSI-agent. jouw missie is je gaat een huis binnen stormen en de twee vijanden verslaan en de gijzelaar te redden')

point_if_entry = input('Ga jij de voor of achter deur doorbreken? de achterdeur lijkt niemand te zijn, optie 1 = voordeur, optie 2 = achterdeur').lower()
if point_if_entry == 'achterdeur' or point_if_entry == 'voordeur':
    print('Je breekt de deur open en door expolsie verlies je je wapen.')
wel_of_niet = input('A: Pak je wapen op of B: Pak je hem niet op.').lower()
if wel_of_niet == 'a':
    print('Je pakt je wapen op en gaat naar binnen. je loopt naar de gang')
elif wel_of_niet == 'b':
    print('Je ging zonder wapen naar binnen. Je bent dood')
    quit()

Kelder_woonkamer = input('Je ziet een kelder of ga je naar de woonkamer?').lower()
if Kelder_woonkamer == 'kelder':
    print('Je loopt naar beneden je raakt een draadje en blaast de hele huis op')
    quit()
elif Kelder_woonkamer == 'woonkamer':
    input('loopt naar de woonwkamer je ziet een van de gijzelaars en de gijzelaar. Hij schiet op jou, ga je A: Hem arresteren of B: schiet op hem ').lower()
if Kelder_woonkamer == 'a' or Kelder_woonkamer == 'A':
    print('Hij schiet nog een keer op je want schreeuwen helpt niet! (GAME OVER)')
    quit()
elif Kelder_woonkamer == 'b' or Kelder_woonkamer == 'B':
    print('Je raakt hem in zijn schouder hij ligt op de grond en je red de gijzelaar. Je loopt naar boven en gaat 1 kamer steeds doorzoeken')

slot = input('Je komt bij een deur met een code slot er op. Er staat en hint, wat is de gemiddelde lengte van een man in nederland ')
if slot >= '170':
    print('De deur gaat open en loopt naar binnen')
else:
    print('Je hebt de code verkeerd. je hebt 3 seconden om weg te komen. 3,2,1 BOOOOM. (je was te langzaam je bent dood)')
    quit()
sniper = input('Je ziet wat glinsteren in de kast je loopt er naar toe, het is een sniper. Pak je hem op JA of NEE').lower()
if sniper == 'ja':
    print('je hebt de sniper op gepakt en gaat terug naar de gang')
elif sniper == 'nee':
    print('je pakt hem niet op, je loopt terug naar de gang')
tweede_kamer = input('Je hoort geluid van de tweede kamer, je trapt de deur je ziet de gijzelaar hij sprint uit het raam. Spring je of niet?').lower()
if tweede_kamer == 'niet':
    print('omdat je niet sprong is hij er vandoor gegaan jij loser')
    quit()
elif tweede_kamer == 'spring':
    if sniper == 'ja':
        print('Je springt uit de raam en doet een 360 no scope across the map GG EZ (WIN)')
    elif sniper == 'nee':
        print('Je springt uit het raam maar je kan geen 360 no scope doen want je hebt geen sniper (fail)') 