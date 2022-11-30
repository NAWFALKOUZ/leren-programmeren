print('Jij bent een DSI-agent. jouw missie is je gaat een huis binnen stormen en de twee vijanden verslaan en de gijzelaar te redden')

print('Je trapt de deur in maar de deur is geboobytrapped')
optie = input('Je verliest je wapen door de expolsie. A: pak de wapen niet of B: pak je de wapen op')
if optie == 'a' or optie == 'A':
    print('Je bent dood omdat je zonder wapen het huis in ging. GAME OVER')
    exit()
elif optie == 'b' or optie == 'B':
    print('Je pakt je wapen op en rent het huis in')
boven_beneden = input('Je hoort voetstappen maar je weet niet of het boven of beneden is. A: ga je naar de kelder of B: naar boven')
if boven_beneden == 'a' or boven_beneden == 'A':
    print('Je ziet explosieven maar nog steeds loop je naar beneden je raakt een draadje en de huis blaast op. GAME OVER')
    quit()
elif boven_beneden == 'b' or boven_beneden == 'B':
    print('Je loopt naar boven je ziet iemand. Je schiet op hem. Jij rent naar een kamer jij loopt er naar toe.')
vraag = input('Je bent bij de deur is hoort gehuil wat doe je A: je blijft wachten of B: je schreeuwd doe je handen om hoog en gaat naar binnen')
if vraag == 'a' or vraag == 'A':
    print('Je hoort hem nog steeds huilen doordat kon je de ander gijzelaar niet horen.Je ziet hem in je oog hoek maar het is te laat. GAME OVER ')
    quit()
elif vraag == 'b' or vraag == 'B':
    print('Hij geeft zich over maar verteld niet waar zijn vriend is.')
geluid = input('Je hoort geluiden in de kamer er naast. Wat doe je A:Blaas je de muur op B:Je gaat de gang in je ziet hem door het raam heen springen ')
if geluid == 'a' or geluid == 'A':
    print('Je stond te dicht bij de explosief dus je vloog naar achter je verloor van bewustzijn en was de verdachten weg.')
elif geluid == 'b' or geluid == 'b':
    print('Jij spring er achter aan een je doet een 360 no scope across the map en je raakt hem GG EZ (WIN) ')