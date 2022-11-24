vraag_man_vrouw = input('Bent u een man of een vrouw?')
if vraag_man_vrouw == 'man':
    snor = input('heeft u een snor?')
    if snor == 'ja':
        snor_breed = int(input('Hoe breed is uw snor (in cm)'))
else: 
    kleur = input('welk kleur haar heeft u?')
    if kleur == 'rood':
        lengte_haar = int(input('Hoe lang is uw haar?(in cm)'))
        
opleiding = input('heeft u een Diploma MBO-4 ondernemen?')
if opleiding == "nee":
    raise NameError('koop een online het is goedkoper dan als je school doet')
rijbewijs_vrachtwagen = input('heeft u een vrachtwagen rijbwijs?')
if rijbewijs_vrachtwagen == "nee":
    raise NameError('steel er een van je buurman!')
hoge_hoed = input('heeft u een hoge hoed?')
gewicht = int(input('Hoeveel kilo weegt u?'))
lengte = int(input('Hoelang bent u (in cm)?'))
if lengte < 150:
    raise NameError('ga is groeien dwerg')
certificaat = input('Heeft u een Certificaat "Overleven met gevaarlijk personeel"?')
dieren_dressuur = int(input('Hoeveel jaar heeft u praktijkervaring met dieren-dressuur?'))
jongleren = int(input('Hoeveel jaar heeft u praktijkervaring met jongleren?'))
acrobatiek = int(input('Hoeveel jaar heeft u praktijkervaring met acrobatiek?'))


if ((vraag_man_vrouw == 'man' and snor == 'ja' and snor_breed  >9) or (vraag_man_vrouw == 'vrouw' and kleur == 'rood' and lengte_haar >19)) and opleiding == 'ja' and rijbewijs_vrachtwagen == 'ja' and hoge_hoed == 'ja' and gewicht >90 and gewicht <120 and lengte >150 and lengte <220 and certificaat == 'ja' and dieren_dressuur > 3 and jongleren >4 and acrobatiek >3:
    print('je bent een kandidaat voor circusdirecteur ')
else:
    print('sorry, je bent niet geschikt voor circusdirecteur')