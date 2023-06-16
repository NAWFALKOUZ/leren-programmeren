def tafel(aantal):
    for x in range(1,11):
        print(x,'x',aantal,'=',x*aantal)
aantal = int(input("Welke tafel wil je leren? "))
tafel(aantal)