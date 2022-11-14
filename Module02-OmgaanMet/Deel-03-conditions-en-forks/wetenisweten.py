a = int(input("noem een getal"))
b = int(input("noem een getal"))


if a > b:
    max = a
    min = b
    print(f"a is het grootste getal:{max}")

elif a < b:
    min = a
    max = b
    print(f"a is het kleinste getal:{min}")

else:
    max = a
    min = a
    print('a en b zijn even groot')


print(f'Het minimum is{min}')
print(f'Het maximum is{max}')