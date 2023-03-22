from fruitmand import fruitmand

Zwaar_licht = sorted(fruitmand, key=lambda x: x['weight'], reverse=True)

for x in Zwaar_licht:
    print(x['name'], x['weight'])