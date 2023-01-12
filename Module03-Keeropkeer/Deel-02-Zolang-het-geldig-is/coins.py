# name of student: nawfal
# number of student: 99071376
# purpose of program: Bereken en geef wisselgeld in munten
# function of program: laat zien hoeveel geld je krijgt in munten
# structure of program: if , elif. While loop int float 

toPay = int(float(input('Amount to pay: ')) * 100)  # Hoeveel je moet betalen
paid = int(float(input('Paid amount: ')) * 100) # Hoeveel je hebt betaald
change = paid - toPay # Wisselgeld dat moet worden gegeven


if change > 0: # Als er wisselgeld moet worden gegeven
  coinValue = 500 # Waarde van de munt
  wisselgeld = ""
  
  while change > 0 and coinValue > 0: # Terwijl er nog wisselgeld moet worden gegeven en er nog grotere muntwaarden zijn
    nrCoins = change // coinValue # Bereken het aantal munten van de huidige waarde dat nodig is om het wisselgeld te geven
    if nrCoins > 0: # Als er munten van de huidige waarde moeten worden gegeven
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) 
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Vraag de gebruiker hoeveel munten van de huidige waarde zijn teruggegeven
      change -= nrCoinsReturned * coinValue # Trek de waarde van de teruggegeven munten van het wisselgeld af dat moet worden gegeven
      wisselgeld += (f'{nrCoinsReturned} of {coinValue} ')
    
    # Set the next coin value to check
    if coinValue == 500:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

  print(f'teruggegeven muntstukken: {wisselgeld}')

  if change > 0: 
    print('Change not returned: ', str(change) + ' cents') 
  else:
    print('done')