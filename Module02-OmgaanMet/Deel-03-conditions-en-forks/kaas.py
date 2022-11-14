kleur_vraag = input("is de kaas geel?")
if kleur_vraag == "nee":
    vraag_schimmel = input('Heeft de kaas blauwe schimmel?')
    if vraag_schimmel == "nee":
        korst_vraag = input('Heeft de kaas een korst?')
        if korst_vraag == "nee":
            print('Jouw kaas is de Mozzarella')
        elif korst_vraag == "ja":
            print("Jouw kaas is de Camembert")
    elif vraag_schimmel == 'ja':
        vraag_korst_kaas = input('Heeft de kaaseen korst?')
        if vraag_korst_kaas == 'nee':
            print('Jouw kaas is de Foume d Amber')
        elif vraag_korst_kaas == 'ja':
            print('Jouw kaas is de Blue de Rochbaron')
elif kleur_vraag == 'ja':
    vraag_gaten = input('Zitten er gaten in?')
    if vraag_gaten == 'nee':
        vraag_hard = input('is de kaas  hard als steen?')
        if vraag_hard == 'nee':
            print('Jouw kaas is de Goudse Kaas')
        elif vraag_gaten == 'ja':
            print('Jouw kaas is de Parmigiano Reggiano')
    elif vraag_gaten == 'ja':
        vraag_duur = input('is de kaas belagelijk duur?')
        if vraag_duur == 'nee':
            print('Leerdammer')
        elif vraag_duur == 'ja':
            print('Emmenthaler')